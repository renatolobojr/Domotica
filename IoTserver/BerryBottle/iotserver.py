from bottle import run, route, template, request, static_file

@route('/')
def index():
    return template('index.html')

@route('/exemplo')
def example():
    return template('hello {{ nome}}!! Seja Bem Vindo!', nome = 'Renato')
    #return 'hello world'

@route('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


run(host='0.0.0.0', port=8080, debug=True)
