from bottle import Bottle, route, run
from sys import argv

app = Bottle()

@app.route('/')
def index():
    return('''
<h3>"hello Wooooorld"</h3>

''')
run(app)
