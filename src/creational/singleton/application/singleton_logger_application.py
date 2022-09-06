from src.commons.app_runner import AppRunner
from src.creational.singleton.domain.logger.console.console_logger import ConsoleLogger
from src.creational.singleton.domain.logger.elasticsearch.elasticsearch_logger import \
    ElasticsearchLogger


class SingletonLoggerApplication(AppRunner):

    def execute(self, args: list):
        print("ConsoleLogger example.")
        console_instance_1 = ConsoleLogger("ConsoleLogger1")
        console_instance_1.log("Hello!")

        console_instance_2 = ConsoleLogger("ConsoleLogger2")
        console_instance_2.log("I'm a ConsoleLogger...")

        console_instance_3 = ConsoleLogger("ConsoleLogger3")
        console_instance_3.log("And I'm an unique instance.")

        print("\nElasticsearchLogger example.")

        elasticsearch_instance_1 = ElasticsearchLogger("ElasticsearchLogger1")
        elasticsearch_instance_1.log("Hello!")

        elasticsearch_instance_2 = ElasticsearchLogger("ElasticsearchLogger2")
        elasticsearch_instance_2.log("I'm a ElasticsearchLogger...")

        elasticsearch_instance_3 = ElasticsearchLogger("ElasticsearchLogger3")
        elasticsearch_instance_3.log("And I'm an unique instance.")


if __name__ == "__main__":
    AppRunner.run(SingletonLoggerApplication, [])
