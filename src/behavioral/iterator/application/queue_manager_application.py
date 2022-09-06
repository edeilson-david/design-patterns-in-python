import time

from src.behavioral.iterator.domain.customer import Customer
from src.behavioral.iterator.domain.password_generator import PasswordGenerator
from src.behavioral.iterator.domain.queue_customer import QueueCustomer
from src.behavioral.iterator.domain.queue_manager import QueueManager
from src.commons.app_runner import AppRunner


class QueueManagerApplication(AppRunner):

    def execute(self, args: list):
        customer_1 = Customer("James", PasswordGenerator.generate())
        customer_2 = Customer("Eddie", PasswordGenerator.generate())
        customer_3 = Customer("Jane", PasswordGenerator.generate())

        queue = QueueCustomer()
        queue.add(customer_1)
        queue.add(customer_2)
        queue.add(customer_3)

        manager = QueueManager(queue)
        while manager.has_next():
            customer = manager.get()
            print(f"Passwd: {customer.passwd} | Customer: {customer.name}")
            print(f"Cashier: 'Hello, {customer.name}. Can I help you?'")
            print(f"Customer: 'Yes...'")
            time.sleep(5)

        print("End of service.")


if __name__ == "__main__":
    AppRunner.run(QueueManagerApplication, [])
