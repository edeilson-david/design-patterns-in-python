from src.behavioral.visitor.domain.cinema_cashier import CinemaCashier
from src.behavioral.visitor.domain.kids_ticket import KidsTicket
from src.behavioral.visitor.domain.student_ticket import StudentTicket
from src.commons.app_runner import AppRunner


class CinemaTicketApplication(AppRunner):

    def execute(self, args: list):
        cashier = CinemaCashier()
        student_ticket = StudentTicket()
        student_ticket.accept(cashier)

        kids_ticket = KidsTicket()
        kids_ticket.accept(cashier)


if __name__ == "__main__":
    AppRunner.run(CinemaTicketApplication, [])
