import ./Programs/decode.py
import ./Programs/photoSave.py
from ./Programs/face_recognition/recognition-app/detector.py import recognize_faces
json=decode.py.run()
recognize_faces(
    ./Programs/imageToSave.png,
     "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
)
