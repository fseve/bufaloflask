from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html')
