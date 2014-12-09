__author__ = 'inozemcev'

import signal
import time

import tornado
import tornado.ioloop as loop
import tornadoredis

import tornado.httpserver as httpserver

from django.core.management.base import BaseCommand, CommandError

from game.tornado.service import MainHandler, SocketHandler


import logging
logger = logging.getLogger('tornado_commander')

class Command(BaseCommand):

    args = '[port_number]'
    help = 'Starts the Tornado application for message handling.'

    def sig_handler(self, sig, frame):
        """Catch signal and init callback"""
        tornado.ioloop.IOLoop.instance().add_callback(self.shutdown)

    def shutdown(self):
        """Stop server and add callback to stop i/o loop"""
        self.http_server.stop()

        msg = 'Tornado Launcher. IOLoop.instance stop'
        logger.debug(msg)

        io_loop = tornado.ioloop.IOLoop.instance()
        io_loop.add_timeout(time.time() + 2, io_loop.stop)

    def handle(self, *args, **options):

        application = tornado.web.Application([
            (r"/", MainHandler),
            (r"/game", SocketHandler),
        ])

        port = 8002
        address =  "127.0.0.1"

        self.http_server = httpserver.HTTPServer(application)
        self.http_server.listen(port, address=address)

        # Init signals handler
        signal.signal(signal.SIGTERM, self.sig_handler)

        # This will also catch KeyboardInterrupt exception
        signal.signal(signal.SIGINT, self.sig_handler)


        msg = 'Tornado Launcher. IOLoop.instance start'
        logger.debug(msg)
        loop.IOLoop.instance().start()
