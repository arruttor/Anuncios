from app import create_app
from app.services.extensions import socketio
import socket


app = create_app()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    print(f"Servidor rodando em http://{ip}:5000")
    socketio.run(app, host='0.0.0.0', port=5000)