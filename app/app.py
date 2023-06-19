from flask import render_template, Flask, request, jsonify
import mimetypes

mimetypes.add_type("image/svg+xml", ".svg")

app = Flask(__name__)

from spaced_repetition.SpacedRepetition import SpacedRepetition

sr = SpacedRepetition(dataset_name="test_quotes")


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

    sr.EoD_Rotation()
    rec_request = request.get_json()
    print("request: " + str(rec_request))

    boxes_list = sr.ReturnAllBoxes()

    return jsonify(boxes_list)


# this below is not used, but it is good example for handling dict data received from SpacedRepetition.py
@app.route("/sr_get_records", methods=["POST"])
def sr_get_records():
    output = request.get_json()

    sr.EoD_Rotation()

    records_list = sr.ReturnAllRecords()
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

    return render_template("projects/spaced_repetition.html")


###### projects section - start ######

###### blogs section  - start ######
@app.route("/blog")
def blog():
    lst_blog_pages = [
            {'name': "Learning",
             'list':
                [
                    {'url': "engineers_memoir", 'name': "Becoming an engineer"},
                    {'url': "drawing", 'name': "Learning to draw"},
                ]
             },
            {'name': "Making sense",
             'list':
                [
                    {'url': "fear_of_existence", 'name': "Fear of existence"}, 
                    {'url': "dionysiac_architects", 'name': "Dionysiac Architects"}, 
                    {'url': "mystory", 'name': "Childhood aspirations"}, 
                ]
            },
            ]
    return render_template("blog.html", lst_blog_pages=lst_blog_pages)


###### blogs section - end ######


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
    me-page

