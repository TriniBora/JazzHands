from flask import Flask
from flask import send_from_directory
from flask import render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from datetime import datetime
import os


app = Flask(__name__)

mysql = MySQL()

CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_Db'] = 'jazz'
mysql.init_app(app)

@app.route('/')
def index():
     '''Visualización del index.html'''
     return render_template('servicios/index.html')


@app.route('/nails')
def services_nails():
     '''Se muestran en la página todos aquellos servicios cargados en la base de datos, cuyo spa sea "uñas"'''
     sql = "SELECT * FROM `jazz` . `servicios` WHERE spa = 'uñas';"
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute(sql)
     servicios_nails = cursor.fetchall()
     conn.commit()
     return render_template('servicios/nails.html', servicios_nails=servicios_nails)


@app.route('/browsandlashes')
def services_browsandlashes():
     '''Se muestran en la página todos aquellos servicios cargados en la base de datos, cuyo spa sea "cejas" o "pestañas'''
     sql = "SELECT * FROM `jazz` . `servicios` WHERE spa = 'cejas' OR spa = 'pestañas';"
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute(sql)
     servicios_browsandlashes = cursor.fetchall()
     conn.commit()
     return render_template('servicios/browsandlashes.html', servicios_browsandlashes=servicios_browsandlashes)

@app.route('/turnos')
def turnos():
     '''Muestra el formulario de turnos'''
     return render_template('servicios/turnos.html')

@app.route('/faq')
def faq():
     '''Muestra la seccion de preguntas frecuentes'''
     return render_template('servicios/faq.html')


@app.route('/gestion', methods=['POST', 'GET'])
def gestion():
     '''Desde acá se pueden crear y editar servicios'''
     sql = "SELECT * FROM `jazz` . `servicios`;"
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute(sql)
     servicios = cursor.fetchall()
     conn.commit()
     return render_template('servicios/gestion.html', servicios=servicios)


@app.route('/create')                # para el ruteo de create.html
def create():
    return render_template('servicios/create.html')


@app.route('/store',  methods=['POST'])     # cuando el formulario de create.hmtl hace el submit envia los datos a la pagina  /store
def  storage():                             
     _id=request.form['txtId']       # toma los datos que envio el formulario en txtNombre
     _spa=request.form['txtSpa']    # toma los datos del formulario
     _nombre=request.form['txtNombre']
     _proceso=request.form['txtProceso']
     _duracion=request.form['txtDuracion']
     _precio=request.form['txtPrecio']
     _foto=request.files['txtFoto']       # toma los datos del

     now=datetime.now()
     tiempo=now.strftime("%Y%H%M%S")

     if _foto.filename !='':
          nuevoNombreFoto=tiempo+_foto.filename   
          _foto.save("uploads/"+nuevoNombreFoto)

          sql="INSERT INTO `jazz`.`servicios` (`id`,`spa`,`nombre`,`proceso`,`duracion`,`precio`,`foto`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
          datos=(_id,_spa,_nombre,_proceso,_duracion,_precio,nuevoNombreFoto)  # crea la sentencia sql
          conn=mysql.connect()
          cursor=conn.cursor()
          conn.commit()

     cursor.execute(sql,datos)               # ejecuta la sentencia sql 
     conn.commit()
     return redirect('/') #Regresamos de donde vinimos


@app.route('/login', methods=['POST', 'GET'])
def login():
     '''En esta página el administrador se loguea para poder ingresar al sistema de gestión'''
     '''Funciona con username='admin' y password=admin' '''

     if request.method=='POST':
          _username = request.form['username']
          _password = request.form['password']
          datos = (_username, _password)
          conn = mysql.connect()
          cursor = conn.cursor()
          sql = "SELECT * FROM `jazz`.`usuarios` WHERE `username` =%s AND `password`=%s;"
          cursor.execute(sql, datos)
          users = cursor.fetchall()
          if len(users) == 1:
               return redirect(url_for('gestion'))
          else:
               return redirect(url_for('login'))

     return render_template('servicios/login.html')

@app.route('/destroy/<identificador>')
def destroy(identificador):
     '''Esta ruta se encarga de eliminar servicios'''
     datos = (identificador)
     conn = mysql.connect()
     cursor = conn.cursor()
     sql = "DELETE FROM `jazz` . `servicios` WHERE `id` =%s"
     cursor.execute(sql, datos)
     conn.commit()
     return redirect(url_for('gestion'))



if __name__=='__main__':
    app.run(debug=True)