from src.behavioral.iterator.core.iterator import Iterator
from src.behavioral.iterator.domain.customer import Customer
from src.behavioral.iterator.domain.queue_customer import QueueCustomer


class QueueManager(Iterator):

    def __init__(self, queue: QueueCustomer):
        self._queue = queue
        self._current = None
        self._index = 0

    def has_next(self) -> bool:
        if self._queue is None:
            return False

        if 0 == len(self._queue.customers):
            return False

        if self._index == len(self._queue.customers):
            return False

        return True

    def get(self) -> Customer:
        self._current = self._queue.customers[self._index]
        self._index += 1
        return self._current
