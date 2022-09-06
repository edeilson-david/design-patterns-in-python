from threading import Thread

from src.commons.app_runner import AppRunner
from src.creational.singleton.domain.logger.console.console_logger_threads import ConsoleLoggerThreads
from src.creational.singleton.domain.logger.elasticsearch.elasticsearch_logger_threads import ElasticsearchLoggerThreads


class SingletonLoggerApplicationThreads(AppRunner):

    def execute(self, args: list):
        print("ConsoleLogger example.")

        console_process_1 = Thread(target=self.run_console_thread, args=("ConsoleLogger1", "Hello!"))
        console_process_2 = Thread(target=self.run_console_thread, args=("ConsoleLogger2", "I'm a ConsoleLogger..."))
        console_process_3 = Thread(target=self.run_console_thread, args=("ConsoleLogger3", "And I'm an unique instance."))

        console_process_1.start()
        console_process_2.start()
        console_process_3.start()

        print("ConsoleLogger example.")

        elasticsearch_process_1 = Thread(target=self.run_elasticsearch_thread, args=("ElasticsearchLogger1", "Hello!"))
        elasticsearch_process_2 = Thread(target=self.run_elasticsearch_thread, args=("ElasticsearchLogger2", "I'm a ElasticsearchLogger..."))
        elasticsearch_process_3 = Thread(target=self.run_elasticsearch_thread, args=("ElasticsearchLogger3", "And I'm an unique instance."))

        elasticsearch_process_1.start()
        elasticsearch_process_2.start()
        elasticsearch_process_3.start()

    @staticmethod
    def run_console_thread(logger_name, message):
        console_logger = ConsoleLoggerThreads(logger_name)
        console_logger.log(message)

    @staticmethod
    def run_elasticsearch_thread(logger_name, message):
        elasticsearch_logger = ElasticsearchLoggerThreads(logger_name)
        elasticsearch_logger.log(message)


if __name__ == "__main__":
    AppRunner.run(SingletonLoggerApplicationThreads, [])
