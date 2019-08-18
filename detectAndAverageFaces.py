from facer import facer
import sys
import time

# https://janakiev.com/til/python-background/

args = sys.argv
if len(args) != 2:
    print()
    print("Wrong number of command-line arguments")
    print("Usage: $python detectAndAverageFaces.py path-to-image-dir")
    print()
    exit()

t_start = time.time()
path_to_images = sys.argv[1]
print(f"PATH TO PROCESS:\n\t{path_to_images}")

# Load the images
images = facer.load_images(path_to_images, verbose=True)
# n = 15
# images = {key:val for key, val in zip(list(images.keys())[:n], list(images.values())[:n])}

# Detect landmarks for each face
t0 = time.time()
landmarks, faces = facer.detect_face_landmarks(images, verbose=True)
elapsed = (time.time() - t0) / 60
print(f"Detecting landmarks took {elapsed:.2f} minutes.")

# Average the faces together
t0 = time.time()
fn = f"average_face_{path_to_images.strip('/').rsplit('/', 1)[-1]}.jpg"
facer.create_average_face(faces, landmarks, output_file=fn, save_image=True, output_dims=(600, 600))
elapsed = (time.time() - t0) / 60
print(f"Averaging faces took {elapsed:.2f} minutes.")

# Say goodbye
elapsed = (time.time() - t_start) / 60
print(f"\nAll done. Total time elapsed: {elapsed:.2f} minutes.")
