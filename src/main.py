from flask import Flask, jsonify
import datetime 
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great human! Keep at it! 🔥',
        'env': 'python-template-test-4',
        'app_name': 'python-template-test-4'
    }), 200

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

@app.route('/api/v1/about')
def about():
    return jsonify({ 'message': 'learning devops'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
