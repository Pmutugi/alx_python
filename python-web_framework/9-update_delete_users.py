from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
app.config['SQLALCHEMY_DATABASE_URI']= f'mysql://{db_username}:{db_password}@{"localhost"}/{db_name}'

###############################################################

db = SQLAlchemy(app)

############################  TO DO 2 ##############################
class User(db.Model):
    id = db.Column(db.integer,primary_key = True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)

def __repr__(self):
    return f"<User{self.username}>"
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"
@app.route('/',strict_slashes = False)
def index():
    return "Hello, ALX Flask!"
@app.route('/add_user',methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        new_user = User(name=name,email=email)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
        except:
            db.session.rollback()
            flash('Error: User with this email already exists', "error")
        return redirect(url_for("add_user"))
    else:
        return render_template("add_user.html")
@app.route('/users')
def users():
    all_users=User.query.all()
    return render_template('users.html',users=all_users)
# the below function involves deletion of users with and updates.
@app.route('/update_user/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        # code for handling POST request
        name = request.form.get('name')
        email = request.form.get('email')
        updated_user = User(name=name,email=email)
        
        try:
            db.session.delete(updated_user)
            db.session.commit()
            flash('User deleted successfully!', 'success')
        except:
            db.session.rollback()
            flash('Error: No user found', "error")
        return redirect(url_for("update_user"))
    else:
        return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)