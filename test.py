import asyncio
import time
import uuid
from typing import NamedTuple, AsyncIterable, List, Type

import pytest as pytest

from core import Executor, Queue
from queue import SingleQueue, ParallelQueue


class SampleTask(NamedTuple):
    id: str


class SampleResult(NamedTuple):
    id: str


class SampleExecutor(Executor[SampleTask, SampleResult]):

    async def execute(self, task: SampleTask) -> SampleResult:
        await asyncio.sleep(0.05)
        return SampleResult(id=task.id)


async def sample_source(tasks: List[SampleTask]) -> AsyncIterable[SampleTask]:
    for task in tasks:
        await asyncio.sleep(0.00001)
        yield task


async def _test_queue(queue_type: Type[Queue], max_time: float):
    count = 100
    tasks = [SampleTask(id=str(uuid.uuid4())) for _ in range(0, count)]
    source = sample_source(tasks)
    queue = queue_type(SampleExecutor)
    start = time.time()
    results = await queue.execute(source)
    end = time.time() - start
    assert results is not None
    assert count == len(results)
    assert {task.id for task in tasks} == {result.id for result in results}
    assert max_time > end


@pytest.mark.asyncio
async def test_single_queue():
    await _test_queue(SingleQueue, 10)


@pytest.mark.asyncio
async def test_parallel_queue():
    await _test_queue(ParallelQueue, 0.5)
