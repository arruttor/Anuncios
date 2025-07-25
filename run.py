import gevent.monkey
gevent.monkey.patch_all()

from app import create_app
from app.services.extensions import socketio
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)