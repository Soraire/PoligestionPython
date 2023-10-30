import .
from ./Programs/face_recognition/recognition-app/detector.py import recognize_faces
recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
)
