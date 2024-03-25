from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="../templates")
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

# データベース接続
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# モデル
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),)
    description = db.Column(db.Text)

@app.route("/")
def index():
    todos = ToDo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/create_new_task", methods=["GET"])
def new_task():
    return render_template("create_task.html")

@app.route("/create", methods=["POST"])
def create():
    title = request.form["title"]
    description = request.form["description"]
    new_todo = ToDo(title=title, description=description)
    db.session.add(new_todo)
    db.session.commit()
    flash("タスクを作成しました")
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = ToDo.query.get_or_404(id)
    if request.method == "GET":
        return render_template("edit.html", ToDo=todo)
    else:
        todo.title = request.form["title"]
        todo.description = request.form["description"]
        db.session.commit()
        flash("タスクを更新しました")
        return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo = ToDo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash("タスクを削除しました")
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=8000, debug=True)
