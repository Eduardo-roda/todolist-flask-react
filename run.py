from flask import Flask,request,jsonify
from flask_mysqldb import MySQL 

app = Flask(__name__)

#CONFIG VALUES FOR MYSQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todolist'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#TABLE tarea
mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS tarea(
                    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    descripcion VARCHAR(255) NOT NULL,
                    estado VARCHAR(100) DEFAULT 'pendiente'
                );
                """)
    mysql.connection.commit()
    print("TABLA CREADA!!!")
    cursor.close()
    context = {
        'status':True,
        'content':'',
        'message':'Bienvenido a mi apirest con Flask'
    }
    
    return jsonify(context)

@app.route('/tarea')
def getTarea():
    cursor = mysql.connection.cursor()
    cursor.execute("select id,descripcion,estado from tarea")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    
    context = {
        'status':True,
        'content':data
    }
    
    return jsonify(context)

@app.route('/tarea',methods=['POST'])
def setTarea():
    descripcion = request.json['descripcion']
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
                   insert into tarea(descripcion)
                   values('"""+ descripcion +"""');
                   """)
    mysql.connection.commit()
    cursor.close()
    
    context = {
        'status':True,
        'content':'',
        'message':'registro exitoso'
    }
    
    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)