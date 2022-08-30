
from flask import Flask, render_template, request


app = Flask(__name__)


##### rutas public #######

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


    ###### rutas ####
@app.route('/auth/login')
def login ():
    return render_template('auth/login.html')

@app.route('/auth/registrer')
def register():
     return render_template('auth/registrer.html')


############ aqui tengo el er
@app.route('/welcome', methods=['GET' , 'POST'])

def welcome():
    email = request.form['mail']
    password = request.form['password']
    access = {'email': email, 'password':password}

    return render_template('admin/index.html', user_access=access )



if __name__ == '__main__':
    app.run(debug=True)
