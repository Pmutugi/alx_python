'''WEB SERVER: dynamic routes in flask framework'''
from flask import Flask , render_template
app = Flask(__name__)

        
@app.route("/",strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'
@app.route("/c/<text>")
def c_route (text):
    formated = text.replace('_', ' ')
    return f"C {formated}"
@app.route("/python/<text>")
@app.route('/python/')
def python(text='is cool'):
    formated = text.replace('_', ' ')
    return  f"Python {formated}"
@app.route('/number/<int:n>')
def integer (n):
    return f'{n} is a number'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

   
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)      