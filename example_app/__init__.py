from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object('settings')

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute('select * from people')
    people = cursor.fetchall()
    return render_template('index.html', people=people)
