from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/history")
def my_history():
    return render_template('history.html')

@app.route("/exec-board")
def display_execs():
    return render_template('exec_board.html')

if __name__ == '__main__':
    app.run(debug=1)
