from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo! Ini adalah aplikasi yang berjalan di Render PaaS."

if __name__ == '__main__':
    app.run()