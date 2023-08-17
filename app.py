from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

msg = {
    'status': '200',
    'msg'   : 'Hello Rasp',
    'IP'    : str(socket.gethostbyname(socket.gethostname())) 
}

#usando o metodo http e não o https://
@app.route('/teste', methods=['GET'])
def teste_msg():
    print(f'IP: {socket.gethostbyname(socket.gethostname())}')
    return jsonify(msg)

app.run(
    port  = 5000,
    host  = 'localhost',
    debug = True
)

# flask run --host=192.168.56.1 --port=5000