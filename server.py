from flask import *
app = Flask(__name__)




@app.route('/')
def main():
  return 'applicarion'



app.run('0.0.0.0',80)
