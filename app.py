from flask import Flask, jsonify, request
import subprocess
import os
import json

executer = os.getenv('EXECUTER') or 'python3'
file_name = os.getenv('FILE_NAME') or 'hello.py'
port = os.getenv('PORT') or 5001

app = Flask(__name__)

@app.route('/run', methods=['GET'])
def index():
  args = json.dumps(request.get_json())
  result = subprocess.run([executer, 'volumes/{}'.format(file_name), args], capture_output=True, text=True)
  return result.stdout

app.run(port=port, host='0.0.0.0', debug=True)