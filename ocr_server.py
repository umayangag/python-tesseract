# -*- coding: utf-8 -*-

import io
import requests
from flask import Flask
from flask_restful import Api, Resource
from flask import request
from waitress import serve
from urllib.parse import quote

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
        url = quote(url, safe='/')
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        print(text)
        return text


class HealthCheck(Resource):
    def get(self):
        return "health is okay", 200


api.add_resource(OCR, "/extract")
api.add_resource(HealthCheck, "/health")
serve(app, port=8082)  # Change port number for production
