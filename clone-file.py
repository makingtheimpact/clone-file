"""
clone-file.py: A script that clones a file in a directory and all subdirectories.

Version: 1.0
Author: Making The Impact LLC
Email: melissa@makingtheimpact.com
License: GPL 2.0 or later
Credits: Thanks to Jane Doe for the math formula
Dependencies: os, shutil module
Requirements: Python 3.6 or higher
Date: 2024-02-15
History: 
    - 2024-02-15: Initial version

Notes: 
Use this plugin to clone an index.php file into all the directories of your WordPress plugin. 

This script takes a file you specify and clones it. It creates a copy of it inside every directory, including subdirectories.

""" 

import os
import shutil

def clone_file(src_file_dir, filename, target_dir):
    """
    Copies the src_file to the target_dir if the filename does not already exist there.
    
    Args: 
        src_file_dir (string): Path to the source file without file name.
        filename (string): The name of the file you want to clone.
        target_dir (string): Path to the root directory where the file should be copied.
        
    Returns: 
        none
    """

    # Set the source file to source directory and filename
    src_file = os.path.join(src_file_dir, filename)
    # Check if source file exists
    if not os.path.exists(src_file):
        print(f"Error: Source file ({src_file}) does not exist.")
        return
    
    # Loop through all directories inside target directory
    for dirpath, dirnames, filenames in os.walk(target_dir):
        # Check if file already exists
        index_path = os.path.join(dirpath, filename)
        # If the file doesn't already exist in the directory
        if not os.path.exists(index_path): # Try to clone the file 
            try: 
                shutil.copy(src_file, index_path)
                print(f"Copied {filename} to {dirpath}")
            except Exception as e: # If failed, output error
                print(f"Error copying file {filename}: {e}")
                
    print('Cloning complete!')

def prompt_user(): 
    """
    Prompts the user for the source file location, source file name, and target directory.
    
    Args: 
        none
        
    Returns: 
        src_dir (string): The file path where the source file is located.
        src_filename (string): The file name and extension of the file.
        tar_dir (string): The directory where the file is to be cloned.
    """
    
    # Get user input for the source file and target directory
    src_dir = str(input('Source File Path Directory: '))
    src_filename = str(input('Source Filename: '))
    tar_dir = str(input('Target Directory: '))
    
    return src_dir, src_filename, tar_dir
    
def main():
    """
    This function prompts the user for the source file and target directory information, then clones the file.
    
    Args: 
        none
        
    Returns: 
        none
    """
    
    print('*** Clone File Script ***\n')
    print('Instructions: To clone a file, first enter in the directory path where the source file is located - DO NOT include the filename with the directory path. Once you do that, you will be prompted to enter in the source filename.\n')
    print('Next, enter in the target root target directory where you want the file to be copied. Once you submit this, the script will begin cloning the file into the root directory and all its subdirectories.\n')
    
    srcpath, thefile, targetdir = prompt_user()
    print('\nBeginning the cloning process...')
    clone_file(srcpath, thefile, targetdir)
    
main()