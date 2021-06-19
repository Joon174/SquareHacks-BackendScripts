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

    # Create a new instance of customer with JSONObject
    @staticmethod
    def create_tournament(self, details):
        event_name = details["name"]
        if self.customer_groups.create_customer_group().is_success():
            self.tournament = Tournament(details)

        return self.tournament is not None

    # 
    def register_participant(self, customer_details, tournament_id):
        result = False

        if self.create_participant(customer_details):
            """
            Pseudocode:
                - Get the tournament ID from the tournament handler and append it into the customer's group id
                - return true the participant is appended.
            """
            customer_details['group_ids'] = self.tournament['id']
            result = self.customer_groups.search_customers().is_success() 

        return result


    # Get tournament details
    def get_details(self):
        return self.tournament.details


    def generate_bracket(self):
        """
        Pseudocode:
            - Get the treelib structure used to represent the bracket structure
            - From treelib structure, create a JSONObject which FrontEnd has
              agreed to
            - return true if successful
        """
