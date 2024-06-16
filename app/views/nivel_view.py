from app import app, db
from flask import render_template, redirect, url_for, request
from app.forms import nivel_form
from app.models.alpha import nivel_model

@app.route("/cadnivel", methods=["POST", "GET"])
def cadastrar_nivel():
    form = nivel_form.NivelForm()
    if form.validate_on_submit():
        nome = form.nome.data
        nivel = nivel_model.Nivel(nome=nome)
        try:
            db.session.add(nivel)
            db.session.commit()
            return redirect(url_for('listar_niveis'))
        except:
            print("Nível não cadastrado")
    return render_template("nivel/form_nivel.html", form=form)

@app.route("/listaniveis")
def listar_niveis():
    niveis = nivel_model.Nivel.query.all()
    return render_template("nivel/lista_nivel.html", niveis=niveis)
@app.route("/listanivel/<int:id>")
def listar_nivel(id):
    nivel = nivel_model.Nivel.query.filter_by(id=id).first()  # Consulta todos os registros na tabela Nivel
    return f"id:{nivel.id} nome:{nivel.nome}"

@app.route('/excluir_nivel/<int:nivel_id>', methods=['GET'])
def confirmar_exclusao_nivel(nivel_id):
    nivel = nivel_model.Nivel.query.get(nivel_id)
    return render_template('nivel/lista_nivel.html', nivel=nivel)

@app.route('/excluir_nivel/<int:nivel_id>', methods=['POST'])
def excluir_nivel(nivel_id):
    nivel = nivel_model.Nivel.query.get(nivel_id)
    db.session.delete(nivel)
    db.session.commit()
    return redirect(url_for('listar_niveis'))

if __name__ == '__main__':
    app.run(debug=True)

