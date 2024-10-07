from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_bcrypt import Bcrypt
from flask import session

user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()

@user_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = current_app.connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT Contraseña FROM usuario WHERE email=%s", (email,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result['Contraseña'], password):
                    session['user_email'] = email
                    return redirect(url_for('user_bp.inicio'))
                else:
                    return redirect(url_for('user_bp.login'))
        except Exception as e:
            return str(e)
    return render_template('login.html')

@user_bp.route('/inicio', methods=['GET', 'POST'])

def inicio():
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT piloto.Nombre_Piloto, piloto.Num_Identificación, piloto.Fecha_Nacimiento, equipo.Nombre_Equipo, aviones.Nombre_Avion
                FROM piloto
                JOIN equipo ON piloto.ID_Equipo = equipo.ID
                JOIN aviones on piloto.ID_Aviones = aviones.ID
            """)
            team_pilot = cursor.fetchall()
    except Exception as e:
        return str(e)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM equipo")
            team = cursor.fetchall()

            cursor.execute("SELECT * FROM aviones")
            planes = cursor.fetchall()

            cursor.execute("SELECT * FROM circuito")
            race = cursor.fetchall()
    except Exception as e:
        return str(e)
    
    return render_template('index.html', team_pilot=team_pilot, team=team, planes=planes, race=race)

@user_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    connection = current_app.connection
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        fecha_n = request.form['fecha']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO usuario (Nombre, Email, Contraseña, Fecha_Nacimiento) VALUES (%s, %s, %s, %s)", (name, email, hashed_password, fecha_n))
                connection.commit()
            return redirect(url_for('user_bp.login'))
        except Exception as e:
            return str(e)
    return render_template('registro_usuarios.html')

@user_bp.route('/piloto', methods=['GET', 'POST'])
def piloto():
    connection = current_app.connection
    if request.method == 'POST':
        name = request.form['name']
        cedula = request.form['cedula']
        fecha = request.form['fecha']
        equipo = request.form['equipo']
        avion = request.form['avion']
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO piloto (Nombre_Piloto, Num_Identificación, Fecha_Nacimiento, ID_Equipo, ID_Aviones) VALUES (%s, %s, %s, %s, %s)", (name, cedula, fecha, equipo, avion))
                connection.commit()
            return redirect(url_for('user_bp.inicio'))
        except Exception as e:
            return str(e)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, Nombre_Equipo FROM equipo")
            equipos = cursor.fetchall()
    except Exception as e:
        return str(e) 
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, Nombre_Avion FROM aviones")
            aviones = cursor.fetchall()
    except Exception as e:
        return str(e)
        
    return render_template('registro_piloto.html', equipos=equipos, aviones=aviones)

@user_bp.route('/equipo', methods=['GET', 'POST'])
def equipo():
    connection = current_app.connection
    if request.method == 'POST':
        name = request.form['name']
        personas = request.form['people']
        mecanicos = request.form['mecanic']
        try: 
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO equipo (Nombre_Equipo, Personas_Equipo, Mecanicos_Equipo) VALUES (%s, %s, %s)", (name, personas, mecanicos))
                connection.commit()
            return redirect(url_for('user_bp.inicio'))
        except Exception as e:
            return str(e)
    return render_template('registro_equipos.html')

@user_bp.route('/circuito', methods=['GET', 'POST'])
def circuito():
    connection = current_app.connection
    if request.method == 'POST':
        name = request.form['name']
        maxim = request.form['cantidad']
        km = request.form['kilometros']
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO circuito (Nombre_Circuito, Cantidad_Max_Participantes, Km_Circuito) VALUES (%s, %s, %s)", (name, maxim, km))
                connection.commit()
            return redirect(url_for('user_bp.inicio'))
        except Exception as e:
            return str(e)
    return render_template('registro_circuito.html')

@user_bp.route('/avion', methods=['GET', 'POST'])
def avion():
    connection = current_app.connection
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        silla = request.form['place']
        km = request.form['recorrido']
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO aviones (Nombre_Avion, Numero_Avion, Cantidad_Asientos, Km_Recorridos) VALUES (%s, %s, %s, %s)", (name, number, silla, km))
                connection.commit()
            return redirect(url_for('user_bp.inicio'))
        except Exception as e:
            return str(e)
    return render_template('registro_aviones.html')



