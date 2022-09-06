from typing import List, Any

from src.behavioral.iterator.core.iterable import Iterable
from src.behavioral.iterator.domain.customer import Customer


class QueueCustomer(Iterable):

    def __init__(self) -> None:
        self._customers = list()

    def add(self, customer: Customer):
        self._customers.append(customer)

    @property
    def customers(self) -> Any:
        return self._customers
