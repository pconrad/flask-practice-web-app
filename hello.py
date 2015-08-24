import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2')
def renderPage2():
    return render_template('page2.html')

@app.route('/page3')
def renderPage3():
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=54321)
