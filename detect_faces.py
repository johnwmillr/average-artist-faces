import cv2
import matplotlib.pyplot as plt
import os

# Create the haar cascade
cascPath = "./FaceDetect/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Paths to all images
image_paths = list(map(lambda x: "./data/images/" + x, os.listdir("data/images")))
image_paths = [path for path in image_paths if path.rsplit("/")[-1] not in [".DS_Store", ".", ".."]]

def main():
    # Read the image
    for imagePath in image_paths[:10]:
        try:
            artist = imagePath.split("_", 3)[3].replace("_", " ")
            artist.rsplit(".")[0]
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
            title = f"({artist}) Found {len(faces)} face{'' if len(faces) == 1 else 's'}"
            cv2.imshow(title, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
            print(imagePath)

if __name__ == "__main__":
    main()
