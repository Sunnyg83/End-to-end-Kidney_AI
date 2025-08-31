from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Vercel!'

@app.route('/api')
def api():
    return {'message': 'API is working!'}

if __name__ == '__main__':
    app.run()
