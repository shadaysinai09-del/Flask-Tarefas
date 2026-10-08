from flask import Flask, render_template, request, redirect, url_for, session
 
app = Flask(__name__)

app.secret_key = "minha chave secreta"

@app.route("/")
def index():
    if 'lista' not in session:
        session['lista'] = []
    print(session['lista'] )    
    return render_template("index.html", lista=session['lista'])

@app.route("/add", methods=["POST"])    
def add():
    nome_tarefas = request.form["tarefa"]
    tarefas = session.get("lista", [])
    tarefas.append(nome_tarefas)
    session["tarefas"] = tarefas
    return redirect(url_for("index"))

@app.route("/delete/<int:indice>")
def delete(indice):
    tarefas = session.get("tarefas", [])
    tarefas.pop(indice)
    session["tarefas"] = tarefas

    return redirect(url_for("index"))      

if __name__ == "__main__":
    app.run(debug=True)    