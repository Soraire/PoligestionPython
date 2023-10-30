import './Programs/decode.py'
import './Programs/photoSave.py'
from './Programs/face_recognition/recognition-app/detector.py' import recognize_faces
json=decode.py.run()
dni = recognize_faces(
    "./Programs/imageToSave.png",
     "hog",
    Path("Programs/face_recognition/recognition-app/output/encodings.pkl"),
)
