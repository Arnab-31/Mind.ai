from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result')
def result():
    return render_template('Result.html')

if __name__ == "__main__":
    app.run(debug=True)

