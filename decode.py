import base64
with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data))
