import os
import base64
from flask import Flask, flash, request, redirect, url_for
app = Flask(__name__)
@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        dni = json['dni']
        img_data = json['imagen']
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(img_data))
        return json
    else:
        return 'Content-Type not supported!'
app.run(host='0.0.0.0', port=80)
