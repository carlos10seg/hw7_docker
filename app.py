# flask_web/app.py
from flask import Flask, render_template
from file_manager import FileManager
app = Flask(__name__)

@app.route('/')
def list_names():
    fileManager = FileManager()
    return render_template("fileContent.html", content = fileManager.get_file_content())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')