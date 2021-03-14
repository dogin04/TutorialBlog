
from flask import Flask, render_template

app = Flask(__name__)

from app.models import Content, User


@app.route("/")
def index():
    contents = Content.query.join(User).all()
    return render_template("index.html", contents=contents)


@app.route("/content/<content_id>")
def content(content_id):
    content = Content.query.filter_by(id=content_id).join(User).all()[0]
    return render_template("content.html", content=content)

