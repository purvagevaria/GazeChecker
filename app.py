from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Run the focus1.py script
    process = subprocess.Popen(['python', 'focus1.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return render_template('index.html', stdout=stdout.decode(), stderr=stderr.decode())

if __name__ == '__main__':
    app.run(debug=True)
