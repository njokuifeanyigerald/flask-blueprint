from flask import Flask, render_template, request
from testing.blueprint import great

app = Flask(__name__)
app.register_blueprint(great, url_prefix="/go")

app.debug=True
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
