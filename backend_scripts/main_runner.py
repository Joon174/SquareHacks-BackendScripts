from backend_scripts.handlers import *


access_token = 'EAAAEMvISJNUM0tgCl7gagI5kh45nOPfLPzGA3GlZ60g8AGC59iRzqez7MImG0U_'


if __name__ == '__main__':
    tournament = TournamentHandler(access_token)
    customer = CustomerHandler(access_token)

    CallbackManager([tournament, customer])

