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

@app.route("/our-work")
def display_work():
    return render_template('our_work.html')

@app.route("/students")
def display_work():
    return render_template('students.html')

@app.route("/sponsors")
def display_work():
    return render_template('sponsors.html')

@app.route("/community")
def display_work():
    return render_template('community.html')

@app.route("/dancers")
def display_work():
    return render_template('dancers.html')

if __name__ == '__main__':
    app.run(debug=1)
