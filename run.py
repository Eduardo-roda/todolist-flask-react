from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'status': True,
        'content':'',
        'message':'Bienvenido a mi apirest con Flask'
    }

    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)