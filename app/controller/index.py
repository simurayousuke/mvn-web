from app import app
from flask import render_template
from app import DBSession
from app.models import M2Dependency as temp
from app.models import M2IndexBak as tt


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    session = DBSession()
    try:
        data = session.execute('SELECT * FROM "m2_dependency" WHERE id > :id1 AND id < :id2', {'id1': 10, 'id2':20})
        # data = session.query(temp).join(tt, tt.artifact_id == temp.id).filter(temp.index_id > 100).limit(5)
        # fetchone(),fetchall()
    finally:
        session.close()
    return render_template('index.html', data=data)
