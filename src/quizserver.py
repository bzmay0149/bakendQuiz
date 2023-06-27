from flask import Flask, request
from flask_cors import CORS

from src.quiz_repository import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, world."

@app.route("/preguntas", methods=["GET"])
def all_preguntas():
    return read_all()

@app.route("/preguntas/<pregunta_id>", methods=["GET"])
def preguntas(pregunta_id):
    return read(pregunta_id)

@app.route("/preguntas", methods=["POST"])
def new_preguntas():
     data = request.get_json()
     create(data)
     return ""
 
@app.route("/preguntas/<id>", methods=["DELETE"])
def delete_pregunta(id):
      remove_pregunta(id) 
      return ""
  
@app.route("/preguntas/<pregunta_id>", methods=["PUT"])
def update_pregunta(pregunta_id):
    data = request.get_json()
    update_pregunta_data(pregunta_id, data)
    return ""


if __name__ == "__main__":
    app.run(debug=True)