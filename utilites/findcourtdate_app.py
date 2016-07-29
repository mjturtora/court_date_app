from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/the-time')
def the_time():
     cur_time = str(datetime.now())
     return cur_time + ' is the current time!  ...YEAH!'

if __name__ == '__main__':
    app.run()
