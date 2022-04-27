from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    if "counter" not in session:
         session["counter"]=0
    else:
        session["counter"]+=1
    return render_template("index.html")

@app.route("/button1")
def button_counter():
    return redirect("/")

@app.route("/button2")
def button_reset():
    session.pop("counter")
    return redirect("/")











if __name__ == "__main__":
    app.run(debug=True)