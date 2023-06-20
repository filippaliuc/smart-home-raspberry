import os
import random
import shutil
import sys

def extract_photos(source_dir, destination_dir, num_photos):
    # Get a list of all image files in the source directory
    image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    
    # Check if the number of photos in the source directory is less than the desired number
    if len(image_files) < num_photos:
        print("Number of photos in the directory is less than the desired number.")
        return
    
    # Randomly select num_photos files from the list
    selected_files = random.sample(image_files, num_photos)
    
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Copy the selected files to the destination directory
    for file in selected_files:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)
        shutil.copyfile(source_path, destination_path)
        print(f"Copied {file} to {destination_dir}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python extract_photos.py source_directory destination_directory num_photos")
        sys.exit(1)
    
    source_directory = '/home/filippaliuc/Desktop/Programare/PetRecognition/kagglecatsanddogs_5340/PetImages/Cat'
    destination_directory = '/home/filippaliuc/Desktop/Programare/PetRecognition/kagglecatsanddogs_5340/Cat'
    number_of_photos = int(sys.argv[1])

    extract_photos(source_directory, destination_directory, number_of_photos)
