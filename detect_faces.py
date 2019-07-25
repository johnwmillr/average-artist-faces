import cv2
import matplotlib.pyplot as plt
import os

# Create the haar cascade
cascPath = "./FaceDetect/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Paths to all images
image_paths = list(map(lambda x: "./data/images/" + x, os.listdir("data/images")))

def main():
    # Read the image
    for imagePath in image_paths[:10]:
        try:
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            print(f"Found {len(faces)} face{'' if len(faces) == 1 else 's'}!")

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            title = f"Found {len(faces)} face{'' if len(faces) == 1 else 's'}"
            cv2.imshow(title, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    print("hi")
    main()
