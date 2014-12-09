__author__ = 'inozemcev'
import tornado.web as web
import tornado.websocket as websocket

import logging
logger =  logging.getLogger('tornado_commander')


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class SocketHandler(websocket.WebSocketHandler):

    def open(self):
        logger.debug('SocketHandler::Open')

    def on_close(self):
        logger.debug('SocketHandler::Close')


    def handle_request(self, response):
        logger.debug('Socket_handler::handle_request')
        pass

    def on_message(self, message):
        logger.debug('SocketHandler::onmessage')
        logger.debug(len(message))
        logger.debug(message)