#create view
#url mapping
#run server
#passing values through url
#render html page
#connect to static files
from flask import Flask,render_template


AI=Flask(__name__)


@AI.route('/wish/<na>')
def wish(na):
    return f'Good Morning {na}'


@AI.route('/first')
def first():
    return render_template('flask.html',name='MOUNIKA REDDY',age=22)

if __name__=='__main__':
    AI.run(debug=True)