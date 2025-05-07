from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1>Learning devops is fun and intresting for me.</h1>'

app.run(host='0.0.0.0',port=7000)
