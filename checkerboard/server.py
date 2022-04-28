from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:num_boxes1>")
def pic_boxes(num_boxes1):
    return render_template("index.html", num_boxes1=num_boxes1)

# @app.route("/<int:num_boxes1>/<int:num_boxes2>")
# def pic_boxes2(num_boxes2):
#     return render_template("index.html", num_boxes2=num_boxes2)




if __name__ == "__main__":
    app.run(debug=True)