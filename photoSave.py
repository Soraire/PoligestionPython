# Import the necessary libraries
import cv2 
import os 

# Set the file path for the source image
path = r'C:\Users\Administrator.SHAREPOINTSKY\Downloads\dora.jpg'

# Set the directory for saving the image
directory = r'C:\Users\Administrator.SHAREPOINTSKY\Desktop\Work'

# Load the image using OpenCV
img = cv2.imread(path) 

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