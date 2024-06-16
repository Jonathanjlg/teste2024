from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import equipamento_form
from app.models.alpha import equipamento_model
from app import db
@app.route("/cadequipamentos",methods=["POST","GET"])
def cadastrar_equipamento():
      form = equipamento_form.EquipamentoForm()
      if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       equipamento = equipamento_model.Equipamento(nome=nome)
       try:
          #adicionar na sessão 
          db.session.add(equipamento)
          #salvar a sessão
          db.session.commit()
          if request.method == 'POST':
           return redirect(url_for('listar_equipamentos'))
       except:
         print("equipamento não cadastrado")
      return render_template("equipamento/form_equipamento.html",form=form)



@app.route("/listaequipamentos")
def listar_equipamentos():
    equipamentos = equipamento_model.Equipamento.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("equipamento/lista_equipamento.html", equipamentos=equipamentos)
