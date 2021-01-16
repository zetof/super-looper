from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from threading import Thread
from time import sleep

class Osc_Interface(Thread):
    """
    Class used to creat an OSC client to send message to an external synthesiser listening to OSC messages
    """

    def __init__(self, client_host='127.0.0.1', client_port=57120, server_host='127.0.0.1', server_port=57130):
        """
        Class constructor
        :param host: URL used to reach OSC listener
        :param port: port used to reach OSC listener
        """

        # Initiate OSC client
        self._osc_client = udp_client.SimpleUDPClient(client_host, client_port)

        # Register a default dispatcher
        self._dispatcher = Dispatcher()
        self._dispatcher.set_default_handler(self._print_message)

        self._server_host = server_host
        self._server_port = server_port

        # Initiate OSC server
        self.start_server()

    def _print_message(address, *args):
        print(f"DEFAULT {address}: {args}")

    def start_server(self):
        self._running = True
        Thread.__init__(self)

    def run(self):
        self._server = BlockingOSCUDPServer((self._server_host, self._server_port), self._dispatcher)
        self._server.serve_forever()

    def stop(self):
        self._running = False
        self._server.shutdown()

    def is_running(self):
        return self._running

    def add_handler(self, trigger, handler):
        self._dispatcher.map('/' + trigger, handler)

    def send(self, osc_handler, msg):
        """
        Send an OSC message to a synthesiser listening to OSC messages
        :param url: used to trigger right instrument on synthesiser - most of the time this is instrument's name
        :param notes: an array containing notes to play in midi note format
        """
        self._osc_client.send_message('/' + osc_handler, msg)
