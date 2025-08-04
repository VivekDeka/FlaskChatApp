import cv2
 
# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#load the image
img = cv2.imread("ai_photo.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect face
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#Draw rectangels around faces
for(x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#Save the result
output_file = "detected_face.jpg"

cv2.imwrite(output_file, img)

print(f"Detected {len(face)} face(s). Output saved as {output_file}")