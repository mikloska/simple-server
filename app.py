from flask import Flask, render_template

app=Flask(__name__)

@app.route('/yo/<name>')
def yo(name):
    return render_template('page.html',name=name)
def index():
    return render_template('index.html')
@app.route('/yo')
def page():
    return render_template('page.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')


# site is http://127.0.0.1:5000
