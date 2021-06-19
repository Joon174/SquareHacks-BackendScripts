from .server_handler import ServerHandler


"""
Square Customer Object Handler between the Square Client and Square Online server
"""


class CustomerHandler(ServerHandler):
    # TODO: Create proper variables to perform correct actions based on assignment of APIs in server

    REGISTER = "/participant.register"

    def __init__(self):
        super().__init__()
        self.register = REGISTER
        self.flask = Flask("Customer")
        self.customers = self.square.customers

    @property
    def recv_cmds(self):
        return [self.register]

    def step(self):
        result = self.customers.list_customers()
        if result.is_success():
            customers = result.body["customers"]

        elif result.is_error():
            customers = result.body["customers"]
            raise Exception("Square Online server has returned an error for payments.")

    # Create a new customer (participant) for each payment performed
    @staticmethod
    def create_participant(self, customer_details):
        participant_info = {}
        for detail in customer_details:
            participant_info[detail] = detail

        return self.customers.create_customer(body).is_success()

    def register_participant(self, customer_details, paid, tournament_avail):
        if self.tournament is None:
            raise Exception("Cannot find any tournament listings in Square Database")

        if self.create_participant(customer_details) and paid and tournamen_avail:
            pass
