'''WEB SERVER: dynamic routes in flask framework'''
from flask import Flask
app = Flask(__name__)

        
@app.route("/",strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'
@app.route("/C/<text>",strict_slashes=False)
def Text (text):
    return f' C is {text}'

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)