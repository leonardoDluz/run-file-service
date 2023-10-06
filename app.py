from flask import Flask, request
import subprocess
import os
import json

executer = os.getenv('EXECUTER')
file_name = os.getenv('FILE_NAME')
port = os.getenv('PORT')

app = Flask(__name__)

@app.route('/run', methods=['GET'])
def index():
  args = json.dumps(request.get_json())
  result = subprocess.run([executer, 'volumes/{}'.format(file_name), args], capture_output=True, text=True)
  return result.stdout

app.run(port=port, host='0.0.0.0', debug=True)