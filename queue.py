from typing import AsyncIterable, List
from core import Queue, T, R
import asyncio


class SingleQueue(Queue):

    async def execute(self, source: AsyncIterable[T]) -> List[R]:
        executor = self._build_executor()
        results = []
        async for task in source:
            results.append(await executor.execute(task))
        return results


class ParallelQueue(Queue):

    def __init__(self, executor_type, workers=10):
        super().__init__(executor_type)
        self.queue = asyncio.Queue()
        self.results = []
        self.workers_n = workers

    async def worker(self):
        while not self.queue.empty():
            self.results.append(self.queue.get_nowait())
            self.queue.task_done()

    async def execute(self, source: AsyncIterable[T]) -> List[R]:
        async for s in source:
            self.queue.put_nowait(s)

        workers = [asyncio.create_task(self.worker()) for _ in range(self.workers_n)]
        await asyncio.gather(self.queue.join(), *workers)

        return self.results
