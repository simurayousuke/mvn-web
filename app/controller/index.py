from app import app
from flask import render_template
from app import DBSession
from app.models import User


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    session = DBSession()
    # data = session.execute('SELECT * FROM "user" WHERE "user".id = 1 ').first()
    data = session.query(User).filter(User.name == '刘安聪').first()
    session.close()

    return render_template('index.html', user=data)
