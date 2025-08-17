from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'SERVICERUNNING'

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
