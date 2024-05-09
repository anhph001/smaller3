from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def main():
    return 'main route'

if __name__ == "__main__":
    app.run(debug=True)