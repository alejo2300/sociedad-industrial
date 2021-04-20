from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/related')
def agenda():
    return render_template('related.html')

@app.route('/contactMe')
def catalogo():
    return render_template('contactMe.html')

if __name__ == '__main__':
    app.run(debug = True)
