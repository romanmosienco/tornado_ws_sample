from tornado.websocket import WebSocketHandler
from tornado.log import app_log


class BaseWebSocketHandler(WebSocketHandler):
    def open(self):
        app_log.info(f"WebSocket opened on: {self.request.remote_ip}")

    def on_message(self, message):
        self.write_message(f"Message: {message}, From: {self.request.remote_ip}")

    def on_close(self):
        app_log.info(f"WebSocket closed on: {self.request.remote_ip}")