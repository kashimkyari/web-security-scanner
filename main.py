# main.py
from flask import Flask, render_template, request
from scanner import WebScanner

app = Flask(__name__)
scanner = WebScanner()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    scan_results = scanner.scan(url)
    return render_template('results.html', results=scan_results)

if __name__ == '__main__':
    app.run(debug=True)
