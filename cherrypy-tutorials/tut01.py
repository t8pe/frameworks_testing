import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World, you sexy thing!"

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
