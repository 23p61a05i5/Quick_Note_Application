from flask import Flask, render_template, request, redirect, url_for
from database import connect, init_db
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        title=request.form.get("title","").strip(); body=request.form.get("body","").strip()
        if title and body:
            with connect() as c: c.execute("INSERT INTO notes(title,body) VALUES(?,?)",(title,body))
        return redirect(url_for("index"))
    q=request.args.get("q","").strip()
    with connect() as c:
        notes=(c.execute("SELECT * FROM notes WHERE title LIKE ? OR body LIKE ? ORDER BY id DESC",(f"%{q}%",f"%{q}%")).fetchall() if q
               else c.execute("SELECT * FROM notes ORDER BY id DESC").fetchall())
    return render_template("index.html",notes=notes,q=q)
@app.post("/delete/<int:note_id>")
def delete(note_id):
    with connect() as c: c.execute("DELETE FROM notes WHERE id=?",(note_id,))
    return redirect(url_for("index"))
if __name__=="__main__": init_db(); app.run(debug=True)
