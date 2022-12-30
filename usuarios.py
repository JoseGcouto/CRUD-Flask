from flask import Blueprint
from flask import render_template, request
from models import Usuario
from database import db
from flask import redirect

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['GET','POST'])
def create():
  if request.method=='GET':
    return render_template('usuarios_create.html')

  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')

    if senha == csenha:
      u = Usuario(nome, email, senha)
      db.session.add(u)
      db.session.commit()
      return 'Dados cadastrados com sucesso'
    else:
      return 'confirme a senha corretamente'

@bp_usuarios.route('/recovery')
def recovery():
  usuarios = Usuario.query.all()
  return render_template('usuarios_recovery.html', usuarios=usuarios)

@bp_usuarios.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
  u = Usuario.query.get(id)
  
  if request.method=='GET':
    return render_template('usuarios_update.html', u = u)

  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    u.nome = nome
    u.email = email
    db.session.add(u)
    db.session.commit()
    return redirect('/usuarios/recovery')

@bp_usuarios.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
  u = Usuario.query.get(id)
  if request.method=='GET':
    return render_template('usuarios_delete.html', u = u)

  if request.method=='POST':
    db.session.delete(u)
    db.session.commit()
    return 'Dados deletados com sucesso'