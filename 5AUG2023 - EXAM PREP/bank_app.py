from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    VALID_CLIENTS = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")
        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) == self.capacity:
            return f"Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.TYPE_ == loan_type, self.loans))
        if client.TYPE_ == 'Student' and loan.TYPE_ != 'StudentLoan':
            raise Exception("Inappropriate loan type!")
        if client.TYPE_ == 'Adult' and loan.TYPE_ != 'MortgageLoan':
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except Student:
            raise Exception("No such client!")
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.TYPE_ == loan_type:
                counter += 1
                loan.increase_interest_rate()
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                counter += 1
                client.increase_clients_interest()
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        result = f"Active Clients: {len(self.clients)}\n" \
                 f"Total Income: {total_income:.2f}\n" \
                 f"Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}\n" \
                 f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
                 f"Average Client Interest Rate: {avg_client_rate:.2f}"

        return result
