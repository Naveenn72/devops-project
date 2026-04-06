from flask import Flask, jsonify, render_template_string
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <html>
    <head>
        <title>DevOps Dashboard</title>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                background: linear-gradient(270deg, #667eea, #764ba2, #6dd5ed);
                background-size: 600% 600%;
                animation: gradientBG 10s ease infinite;
                color: white;
                text-align: center;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            h1 {
                margin-top: 30px;
                animation: fadeIn 2s ease-in-out;
            }

            .container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                margin-top: 30px;
            }

            .card {
                background: white;
                color: black;
                margin: 15px;
                padding: 20px;
                width: 250px;
                border-radius: 15px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
                transition: transform 0.3s, box-shadow 0.3s;
                animation: slideUp 1s ease;
            }

            .card:hover {
                transform: scale(1.08);
                box-shadow: 0px 0px 30px rgba(0,0,0,0.6);
            }

            @keyframes slideUp {
                from { transform: translateY(50px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }

            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            .status {
                color: green;
                font-weight: bold;
                animation: blink 1.5s infinite;
            }

            @keyframes blink {
                50% { opacity: 0.3; }
            }
        </style>
    </head>
    <body>

        <h1>🚀 DevOps CI/CD Dashboard</h1>

        <div class="container">

            <div class="card">
                <h3>📦 Application</h3>
                <p>Flask App in Docker</p>
            </div>

            <div class="card">
                <h3>⚙️ Status</h3>
                <p class="status">✔ Running</p>
            </div>

            <div class="card">
                <h3>🌐 Host</h3>
                <p>{{hostname}}</p>
            </div>

            <div class="card">
                <h3>⏰ Time</h3>
                <p>{{time}}</p>
            </div>

            <div class="card">
                <h3>🔗 API</h3>
                <p>/api</p>
            </div>

            <div class="card">
                <h3>❤️ Health</h3>
                <p>/health</p>
            </div>

        </div>

    </body>
    </html>
    """, hostname=socket.gethostname(), time=datetime.datetime.now())

@app.route('/api')
def api():
    return jsonify({
        "message": "DevOps API is working",
        "status": "success"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)