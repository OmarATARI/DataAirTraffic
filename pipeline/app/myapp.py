from flask import (Flask, request, jsonify)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only
#from flask_script import Manager
from database import session
from models import Flight
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
   
app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pxl:password@localhost/airtraffic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#manager = Manager(app)

@app.route('/')
def hello():
    return 'hello'

@app.route('/getdata')
def get():
    try:
      flights = session.query(Flight).all()
      return jsonify([e.serialize() for e in flights])
    except Exception as e:
	    return(str(e))

@app.route('/diag')
def build_plot():
  try:
    img = io.BytesIO()
    names = session.query(Name).all()
    data = [e.serialize() for e in names]

    used_data = {'names': [], 'occurences': [], 'gender': []}
    for d in data:
      used_data['names'].append(d['name'])
      used_data['occurences'].append(d['occurences'])
      used_data['gender'].append(d['gender'])

    df = pd.DataFrame(used_data, columns=['occurences','names', 'gender'])
    df["gender"].value_counts().plot(kind='pie')
    
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

  except Exception as e:
    return(str(e))

@app.route('/nuage')
def build_cloud():
  try:
    img = io.BytesIO()
    names = session.query(Name).all()
    data = [e.serialize() for e in names]

    used_data = {'names': [], 'occurences': [], 'gender': []}
    for d in data:
      used_data['names'].append(d['name'])
      used_data['occurences'].append(d['occurences'])
      used_data['gender'].append(d['gender'])

    df = pd.DataFrame(used_data, columns=['occurences','names', 'gender'])
    df.plot(x ='occurences', y='names', kind = 'scatter')
    
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

  except Exception as e:
    return(str(e))

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')