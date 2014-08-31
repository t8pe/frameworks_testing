from bottle import route, run, template, redirect, request, response, Bottle



route('/hello')
def hello():
    name = request.cookies.username or 'Guest'
    return template('Hello {{name}}', name=name)

route('/hello/<name>')
def index(name):
    return template('<i>Hello {{name}}</i>!', name=name)


@app.route('/goodbye/<name>')
def index(name):
    if name:
        return template("Goodbye {{name}}, I didn't like you anyway!", name=name)
    else:
        return template("Oh fine then.")

@app.route('/wrong')
def wrong():
    redirect('hello/fuckwit')

run(reloader=True)
