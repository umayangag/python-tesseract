# -*- coding: utf-8 -*-

import io
import requests
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import request
from waitress import serve
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

app = Flask(__name__)
api = Api(app)


class OCR(Resource):
    def get(self):
        url = request.args.get('url')
        if url is None or url == "":
            return {"error": "invalid input"}, 500
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        return pytesseract.image_to_string(img)


class HealthCheck(Resource):
    def get(self):
        return "health is okay", 200


api.add_resource(OCR, "/extract")
api.add_resource(HealthCheck, "/health")
serve(app, port=8081)  # Change port number for production
