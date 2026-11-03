from flask import Flask
app = Flask(__name__)

@app.route('/api/sa')
def hello():
    return "Hello from Service Robi CSK APP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
