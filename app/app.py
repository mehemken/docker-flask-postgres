import time
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy


DBUSER = 'marco'
DBPASS = 'foobarbaz'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'testdb'


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'foobarbaz'


db = SQLAlchemy(app)


class students(db.Model):
    apiid = db.Column('api_id', db.Integer, primary_key=True )
    id = db.Column(db.String(255))
    name = db.Column(db.String(255))
    symbol = db.Column(db.String(255))
    platforms = db.Column(db.String(255))
    contract = db.Column(db.String(255))
    
    def __init__(self,id, name,symbol, platforms,contract):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.platforms = platforms
        self.contract = contract


def database_initialization_sequence():
    db.create_all()
    test_rec = students(
              'John Doe',
            'Los Angeles',
            'btc',
            '123 Foobar Ave',
            '123 Foobar Ave')

    db.session.add(test_rec)
    db.session.rollback()
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['id'] or not request.form['symbol']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(
                      request.form['id'],
                      request.form['name'],
                      request.form['symbol'],
                      request.form['platforms'],
                      request.form['contract'])
            db.session.add(student)
            db.session.commit()
            flash('Record was succesfully added')
            return redirect(url_for('home'))
    return render_template('show_all.html', students=students.query.all())


if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
