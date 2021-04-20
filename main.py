from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def homeBack():
    return render_template('index.html')


@app.route('/related.html')
def related():
    return render_template('related.html')

@app.route('/contactMe.html')
def contactMe():
    return render_template('contactMe.html')


if __name__ == '__main__':
    app.run(debug = True)