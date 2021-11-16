from typing import AsyncIterable, Generic, TypeVar, Type, List

T = TypeVar("T")
R = TypeVar("R")


class Executor(Generic[T, R]):

    async def execute(self, task: T) -> R:
        raise NotImplementedError


class Queue(Generic[T, R]):

    def __init__(self, executor_type: Type[Executor[T, R]]):
        self._executor_type = executor_type

    def _build_executor(self) -> Executor[T, R]:
        return self._executor_type()

    async def execute(self, source: AsyncIterable[T]) -> List[R]:
        raise NotImplementedError
