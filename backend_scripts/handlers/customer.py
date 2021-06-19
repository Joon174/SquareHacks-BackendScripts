from .server_handler import ServerHandler


class CustomerHandler(ServerHandler):
    # TODO: Create proper variables to perform correct actions based on assignment of APIs in server
    
    REGISTER = ".register"
    
    def __init__(self):
        super().__init__()
        self.register = REGISTER
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
