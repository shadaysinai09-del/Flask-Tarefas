from flask import Flask, render_template, request, redirect, url_for, session
 
app = Flask(__name__)

app.secret_key = "minha chave secreta"

@app.route("/")
def index():
    if 'lista' not in session
        session['lista'] = []
    return render_template("index.html", lista=session['lista'])

@app.route("/add", methods=["POST"])    
def add():
    nome_tarefas = request.form["tarefas"]
    tarefas = session.get("tarefas", [])
    tarefas.append(nome_tarefas)
    session["tarefas"] = tarefas
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tarefas = session.get("tarefas", [])
    if 0 <= task_id < len(tarefas):
        tarefas.pop(task_id)  
    session["tarefas"] = tarefas

    return redirect(url_for("index"))      

if __name__ == "__main__":
    app.run(debug=True)    