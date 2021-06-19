from .server_handler import ServerHandler


class PaymentHandler(ServerHandler):
    # TODO: Create proper variables to perform correct actions based on assignment of APIs in server
    MAKE_PAYMENT = ".make_payment"

    def __init__(self):
        super().__init__()
        self.make_payment = MAKE_PAYMENT
        self.payments = self.square.payments

    @property
    def recv_cmds(self):
        return [self.make_payment]

    def step(self):
        result = self.payments.list_payments()

        if result.is_success():
            payments = result.body["payments"]

        elif result.is_error():
            payments = result.body["error"]
            raise Exception("Square Online server has returned an error for payments.")
