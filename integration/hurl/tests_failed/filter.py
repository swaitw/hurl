from app import app
from flask import Response


@app.route("/error-filter")
def error_filter():
    return Response(
        """{
          "file":"5L2g5aW95LiW5",
          "text_encoded":"PDw_Pz8-Pg",
          "id":"123x",
          "status": true,
          "list": [1,2,3],
          "empty_list": [],
          "number": 42
}
""",
        mimetype="application/json",
    )
