from flask import render_template, Flask, request, jsonify
import mimetypes

mimetypes.add_type("image/svg+xml", ".svg")

app = Flask(__name__)

from SpacedRepetition import SpacedRepetition

db = SpacedRepetition("learning_words", 7, 5)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


###### projects section - start ######


@app.route("/sr_get_all_boxes", methods=["POST"])
def sr_get_all_boxes():
    # Returns rank 3 tensor:
    # 0D: box number
    # 1D: record within box
    # 2D: value: 0 - Id, 1 - Name, 2 - Visible value/question, 3 - Hidden value/Answer, 4 - "Is in use", 5 - "Days in boxes"
    # For example: boxes_list[2][1][3] is record from 2 (starting from 0) box, 1 record, 3 value: Answer

    rec_request = request.get_json()
    print("request: " + str(rec_request))

    boxes_list = db.ReturnAllBoxes()

    return jsonify(boxes_list)


# this below is not used, but it is good example for handling dict data received from SpacedRepetition.py
@app.route("/sr_get_records", methods=["POST"])
def sr_get_records():
    output = request.get_json()

    records_list = db.ReturnAllRecords()
    print(records_list)
    dict = {}
    dict["name"] = records_list[1]
    dict["question"] = records_list[2]
    dict["answer"] = records_list[3]
    return dict


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/spaced_repetition")
def spaced_repetition():
    # SpacedRepetition API
    # import SpacedRepetition from SpacedRepetition
    # a=get_records()

    return render_template("spaced_repetition.html")


###### projects section - start ######

###### blogs section  - start ######
@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/drawing")
def drawing():
    return render_template("blog/drawing.html")


###### blogs section - end ######


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
