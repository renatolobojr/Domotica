#import raspi
from bottle import run, route, template, request, static_file

#raspi = raspi.Raspi() #instaciando um objeto da classe raspi.

@route('/')
def index():
    return template('index.html')

@route('/exemplo')
def example():
    return template('hello {{ nome}}!! Seja Bem Vindo!', nome = 'Renato')
    #return 'hello world'

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='img/')

@route('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

#  value = raspi.read_sensor()
#
#    raspi.change_led(False)
#
# https://dreamingecho.es/blog/internet-of-things-with-python-and-flask
# https://github.com/renatolobojr/flask-internet-of-things-app/tree/master/templates

run(host='0.0.0.0', port=8080, debug=True) #

