import './Programs/decode.py'
from './Programs/photoSave.py' import saving
from './Programs/face_recognition/recognition-app/detector.py' import recognize_faces
json=decode.py.run()
dni = recognize_faces(
    "./Programs/imageToSave.png",
     "hog",
    Path("Programs/face_recognition/recognition-app/output/encodings.pkl"),
)
if dni == "Unknown":
    return: "New"
else:
    saving(dni)
    return: "Done"
