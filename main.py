from flask import Flask, render_template

app = Flask(__name__)

menu = ["Setup", "First App", "Contacts"]

@app.route('/')
def index():
    return render_template('index.html', title="Main Page", menu=menu)

@app.route('/about')
def about():
    return render_template('index.html', title="About Website", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)