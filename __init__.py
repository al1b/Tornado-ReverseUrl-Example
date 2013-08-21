import os
import tornado.ioloop
import tornado.web
import tornado.template
from tornado.web import URLSpec as URL


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.render('index.html')
        

class PageHandler(tornado.web.RequestHandler):
        def get(self, page_name):
            self.render('page.html', page_name=page_name)
            

# Map url patterns to handlers            
application = tornado.web.Application([
    URL(r"/", MainHandler, name='main'),
    URL(r"/page/(.*?)", PageHandler, name='page'),
])

# Application settings
application.settings['template_path'] = os.path.join(os.path.dirname(__file__), 'templates')
application.settings['autoescape'] = None


if __name__ == '__main__':
    application.listen(8083)
    tornado.ioloop.IOLoop.instance().start()