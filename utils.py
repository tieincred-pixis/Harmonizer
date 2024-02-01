import os
from PIL import Image
import subprocess

def run_image_harmonization():
    """
    Runs the image harmonization command using Python's subprocess module.
    """
    command = [
        'python', '-m', 'demo.image_harmonization.run',
        '--example-path', './demo/image_harmonization/example'
    ]

    try:
        # Run the command
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command executed successfully.")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command.")
        print("Error:", e.stderr)

# Example usage
# run_image_harmonization()

def transfer_and_rename_images(input_folder, output_folder, new_names):
    """
    Copies images from the input folder to the output folder with new names.

    Parameters:
    - input_folder: str, path to the folder containing the input images.
    - output_folder: str, path to the folder where images will be saved.
    - new_names: list of str, new names for the images (including file extensions).
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Ensure the number of new names matches the number of image files
    if len(new_names) != len(image_files):
        raise ValueError("Number of new names must match the number of image files.")

    # Process each image
    for old_name, new_name in zip(image_files, new_names):
        # Define file paths
        old_file_path = os.path.join(input_folder, old_name)
        new_file_path = os.path.join(output_folder, new_name)

        # Open and save the image with the new name
        with Image.open(old_file_path) as img:
            img.save(new_file_path)


def save_image_multiple_times(source_image_path, target_folder, new_names):
    """
    Copies a single image and saves it multiple times in a target folder with specified names.

    Parameters:
    - source_image_path: str, path to the source image file.
    - target_folder: str, path to the folder where images will be saved.
    - new_names: list of str, names for the copies of the image (including file extensions).
    """
    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Open the source image
    with Image.open(source_image_path) as img:
        # Save the image multiple times with the new names
        for new_name in new_names:
            new_file_path = os.path.join(target_folder, new_name)
            img.save(new_file_path)