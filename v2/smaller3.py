from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html', username="anhpham")

@app.route('/smaller3')
def smaller3():
    return 'smaller3'

@app.route('/faq')
def faq():
    return 'faq'

@app.route('/zodiac')
def zodiac():
    return 'zodiac'

@app.route('/message3')
def message3():
    return 'message3 - under developement'

@app.route('/news')
def news():
    return 'news - under development'

if __name__ == "__main__":
    app.run(debug=True)