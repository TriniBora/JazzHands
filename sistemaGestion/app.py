from flask import Flask
from flask import send_from_directory
from flask import render_template, request, redirect, url_for, flash
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


@app.route('/login')
def login():
     '''En esta página el administrador se loguea para poder ingresar al sistema de gestión'''
     return render_template('servicios/login.html')


if __name__=='__main__':
    app.run(debug=True)