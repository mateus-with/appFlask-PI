from flask.views import MethodView
from flask import jsonify, request
from config import db

class OlaController(MethodView):
    def get(self):
        return "ola mundo"

class AddDocumentController(MethodView):
    def post(self):
        data = request.json
        db.my_collection.insert_one(data)
        return jsonify({"message": "Documento adicionado com sucesso!"}), 201

class GetDocumentsController(MethodView):
    def get(self):
        documents = list(db.my_collection.find())
        for document in documents:
            document['_id'] = str(document['_id'])  # Converte ObjectId para string
        return jsonify(documents), 200

def register_routes(app):
    app.add_url_rule('/ola', view_func=OlaController.as_view('ola_route'))
    app.add_url_rule('/add', view_func=AddDocumentController.as_view('add_document'))
    app.add_url_rule('/get', view_func=GetDocumentsController.as_view('get_documents'))
