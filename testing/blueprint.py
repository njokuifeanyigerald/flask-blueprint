from flask import Blueprint, render_template

great = Blueprint("great", __name__, static_folder='static', template_folder='templates')

@great.route("/home")
@great.route("/")
def crazy():
    return render_template('crazy.html')
@great.route("/test")
def test():
    return "<h2>testing...</h2> <br> <p><b>hello #BlackLivesMatters</b></p>"