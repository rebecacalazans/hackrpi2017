from flask import *
app = Flask(__name__)




@app.route('/')
def main():
  return 'application'



app.run('0.0.0.0',1337)
