from app.handlers import BaseWebSocketHandler


roots = [
    (r'/ws/1.0/', BaseWebSocketHandler),
]