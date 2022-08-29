
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template ('public/about.html')

@app.route('/contact')
def contact():
    return render_template ('public/contact.html')


@app.route('/portfolio')
def portfolio():
    return render_template ('public/portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
