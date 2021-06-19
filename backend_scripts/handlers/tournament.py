from .server_handler import ServerHandler


"""
Square Customer Group Object Handler between the Square Client and Squre Online server
"""


class Tournament:
    def __init__(self, details):
        # Dicitonary object to compensate for overall JSONObject usage
        self.details = details


class TournamentHandler(ServerHandler):
    # TODO: Create proper variables to perform correct actions based on assignment of APIs in server
    CREATE_TOURNAMENT = "/tournament.create_new"
    GET_DETAILS = "/tournament.details"

    def __init__(self, access_token):
        super().__init__(access_token)
        self.tournament = None
        self.customer_groups = self.square.customer_groups

    # Create a new instance of customer
    @staticmethod
    def create_tournament(self, details):
        event_name = details["name"]
        if self.customer_groups.create_customer_group().is_success():
            self.tournament = Tournament(details)

        return self.tournament is not None

    # Get tournament details
    def get_details(self):
        return self.tournament.details
