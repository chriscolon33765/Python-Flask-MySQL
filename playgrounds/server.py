from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("play.html")

@app.route("/play")
def play():
    return render_template("play.html", numb_boxes = 3)

@app.route("/play/<int:num>")
def box_num(num):
    return render_template("play.html", numb_boxes = num)

@app.route("/play/<int:num>/<color>")
def box_color(num, color):
    return render_template("play.html", numb_boxes=num, color=color)







if __name__ == "__main__":
    app.run(debug=True)