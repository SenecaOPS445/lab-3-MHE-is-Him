#!/usr/bin/env python3
import subprocess

'''Lab 3 Task: Get free space on the root directory'''
# Author ID: mhamilton-edwards

def free_space():
    # Run the 'df' command, pipe it to 'grep' and then to 'awk'
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate()

    # Check for errors
    if error:
        return f"Error: {error.decode('utf-8').strip()}"

    # Decode and return the output
    return output.decode('utf-8').strip()  # Remove any extra whitespace or newlines

if __name__ == '__main__':
    print(free_space())  # This will print the available space on the root directory

