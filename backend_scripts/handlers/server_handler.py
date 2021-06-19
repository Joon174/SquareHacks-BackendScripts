from square.client import Client


# General listener for messages from any server
class ServerHandler:
    def __init__(self, client_ip, token=None):
        self.client_ip = client_ip

        if token:
            try:
                self.square = Client(access_token=access_token)
            except:
                raise Exception("Invalid token, cannot create Square Client.")

    @property
    def recv_cmds(self):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError


# Main Manager to be run in the script. Will handle all interfaces
class CallbackManager:
    def __init__(self, callbacks):
        self._callbacks = {}
        if isinstance(callbacks, str):
            callbacks = [
                callbacks,
            ]

        for runner in callbacks:
            self._callbacks = callbacks[runner]

    def run(self):
        for runner in self.callbacks:
            self._callbacks.step()

    # Cleanly exits all communications with server to prevent any premature ACK or other errors
    def stop(self):
        pass

    def cleanup(self):
        self.stop()
