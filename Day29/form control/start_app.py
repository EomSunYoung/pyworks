from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/output', methods=['POST'])
def output():
    uid = request.form['uid']   # name 값을 가져옴
    passwd = request.form['passwd']
    return render_template('output.html', uid=uid, passwd=passwd)

app.run()