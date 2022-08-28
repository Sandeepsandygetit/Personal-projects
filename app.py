from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,Boolean


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db = SQLAlchemy(app)



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def home():
    todo_list=Todo.query.all()
    return render_template("index.html",todo_list=todo_list)




@app.route("/add" , methods=["POST"])
def add():
    title=request.form.get("title")
    new_todo=Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home")





if __name__ == "__main__":
    db.create_all()
    new_todo=Todo(title="todo1" , complete=False)
    db.session.add(new_todo)
    db.session.commit()
    app.run(debug=True)