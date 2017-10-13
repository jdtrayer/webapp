from flask import Flask
import socket
app = Flask(__name__)


@app.route("/")
def hello():
    return "<br>Hello Brian from %s at IP address %s!"%(socket.gethostname(),socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)

