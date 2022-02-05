import tornado.ioloop
import tornado.web
from tornado.log import app_log, enable_pretty_logging
from app.roots import roots


enable_pretty_logging()
HOST = "0.0.0.0"
PORT = 8000

if __name__ == "__main__":
    app = tornado.web.Application(roots)
    app.listen(port=PORT, address=HOST)
    app_log.info(f'tornado is listening on {HOST}:{PORT}')
    tornado.ioloop.IOLoop.current().start()