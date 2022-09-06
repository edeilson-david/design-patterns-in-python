from src.behavioral.command.domain.email.email_notifier import EmailNotifier
from src.behavioral.command.domain.executor import Executor
from src.behavioral.command.domain.slack.slack_notifier import SlackNotifier
from src.behavioral.command.domain.sms.sms_notifier import SMSNotifier
from src.commons.app_runner import AppRunner


class NotificatorApplication(AppRunner):

    def execute(self, args: list):

        msg = {"subject": "Uhuuuul! Prepare yourself! Black friday is coming!"}
        slack = SlackNotifier(msg)
        email = EmailNotifier(msg)
        sms = SMSNotifier(msg)

        executor = Executor()
        executor.execute(slack)
        executor.execute(email)
        executor.execute(sms)


if __name__ == "__main__":
    AppRunner.run(NotificatorApplication, [])
