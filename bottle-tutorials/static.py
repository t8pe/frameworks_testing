from bottle import static_file, run, route, abort
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='')

@route('/wrong')
def wrong():
    redirect("/hello/fred")
    
run(host='localhost', port=5000 )
