from flask import Flask, render_template, send_file


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Error_connection.html')

if __name__ == "__main__":
    app.run(debug=False)


# ===============================================
# flask  run --host=0.0.0.0 " this for all users "
# ===============================================
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "<h1>Hello, World!</h1>"
# ===============================================
# from flask import Flask
# from markupsafe import escape

# app = Flask(__name__)

# @app.route('/<name>')
# def hello(name):
#     return f"<h1>Hello, {escape(name)}!</h1>"
# ===============================================

# folder templates for files web

# ===============================================

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def index(name=None):
#     return render_template('hello.html', name=name)