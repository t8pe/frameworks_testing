import web

urls = (
    '/', 'index'
    
)

class index:
    def GET(self):
        return "Hello world! It's webpy! Or is it web.py? We'll never know."

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run
