import cv2
import os
from natsort import natsorted


def images_to_video(images_folder, output_video_path, image_prefix="frame", fps=30):
    # Get the list of image files in the folder
    image_files = [f for f in os.listdir(images_folder) if f.endswith(".png")]
    image_files = natsorted(image_files)  # Sort the files in natural order

    if not image_files:
        print("No image files found in the specified folder.")
        return

    # Read the first image to get dimensions
    first_image_path = os.path.join(images_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    height, width, _ = first_image.shape

    # Define the video writer
    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )  # You can use other codecs like 'XVID' or 'MJPG'
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write each image to the video
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    # Release the video writer
    video_writer.release()


if __name__ == "__main__":
    # Replace 'input_images' with the folder containing your images
    input_images_folder = "./generated_images"

    # Replace 'output_video.mp4' with the desired output video file path
    output_video_path = "output_video.mp4"

    # Set the frames per second (fps) for the output video
    output_fps = 15

    images_to_video(input_images_folder, output_video_path, fps=output_fps)
