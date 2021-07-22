from flask import Flask
from flask import send_from_directory
from flask import render_template, request, redirect, url_for, flash, session, g
from flaskext.mysql import MySQL
from datetime import datetime
import os

app = Flask(__name__)

mysql = MySQL()

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


@app.route('/gestion', methods=['POST'])
def gestion():
     '''Desde acá se pueden crear y editar servicios'''
     sql = "SELECT * FROM `jazz` . `servicios`;"
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.execute(sql)
     servicios = cursor.fetchall()
     conn.commit()
     return render_template('servicios/gestion.html', servicios=servicios)


@app.route('/login', methods=['POST'])
def login():
     '''En esta página el administrador se loguea para poder ingresar al sistema de gestión'''
     _username = request.form['username']
     _password = request.form['password']

     datos_formulario = (_username, _password)

     conn = mysql.connect()
     cursor = mysql.conn.cursor()
     sql = "SELECT `username`, `password` FROM `jazz`.`usuarios` WHERE username =% AND password=%s;"
     cursor.execute(sql, datos_formulario)
     datos_bd = cursor.fetchall()

     if len(datos_bd)==1:
          return render_template('servicios/gestion.html')
     else:
          return redirect('/login')
          #Conexion con la bd y crecaion del cursor

     return render_template('servicios/login.html')



     '''if request.method == 'POST':

          #Obtener los campos del formulario
          _username = request.form['username']
          _password_candidate = request.form['password']

          #Conexion con la bd y crecaion del cursor
          sql = "SELECT * FROM `jazz`.`usuarios` WHERE username =%;"
          conn = mysql.connect()
          cursor = mysql.conn.cursor()

          #Obtener el usuario desde la bd
          result = cursor.execute(sql, _username)

          if result > 0:
               #Obtenemos el password guardado en la bd
               data = cursor.fetchone()
               password = data['password']

               #Comparamos los password'''






if __name__=='__main__':
    app.run(debug=True)