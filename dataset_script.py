import os
import shutil

def label_extraction(img_name):
    '''
    This function will extract age from image name and return the class index by performing integer division (by 25).
    Args:
        img_name: The name of the image.
    Returns:
        class_index: An integer representing the age class.
    '''
    # Extract age 
    age = int(img_name.split("_")[0])
    print(age)
    
    # Class index by dividing by 25
    class_index = age // 25
    
    return class_index

def organize_images_by_class(source_dir):
    # List all files in the source directory
    for img_name in os.listdir(source_dir):

        if img_name!='.DS_Store':
            print(img_name)
        # Ensure the file is an image based on extension
            # Extract class index from the image name
            
            class_index = label_extraction(img_name)
            
            # Create a class directory if it doesn't exist
            class_dir = os.path.join(source_dir, str(class_index))
            os.makedirs(class_dir, exist_ok=True)
            
            # Define the source and destination file paths
            src_file = os.path.join(source_dir, img_name)
            dst_file = os.path.join(class_dir, img_name)
            
            # Move the image to the class directory
            shutil.move(src_file, dst_file)

if __name__ == "__main__":
    # Path to the directory containing the images
    source_directory = "new_imageset"
    
    # Organize images by class
    organize_images_by_class(source_directory)
