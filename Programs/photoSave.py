# Import the necessary libraries
import cv2 
import os 
from decode.py import dni
from face_recognition.recognition-app.detector.py import result

# Set the file path for the source image
path = r'C:\Users\devandroid\Downloads\asdas.jpg'

# Set the directory for saving the image
directory = r'C:\Users\devandroid\Desktop' + dni

# Load the image using OpenCV
img = cv2.imread(path) 

# Make a folder to save the image in
try: 
    os.mkdir(directory) 
  
# Change the working directory to the specified directory for saving the image
os.chdir(directory) 

# Print the list of files in the directory before saving the image
print("Before saving")   
print(os.listdir(directory))   

# Save the image with the filename "cat.jpg"
filename = 'cat.jpg'
cv2.imwrite(filename, img) 

# Print the list of files in the directory after saving the image
print("After saving")  
print(os.listdir(directory))
