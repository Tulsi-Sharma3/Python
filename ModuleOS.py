import os

# Specify directory path
path = "/"

print("Contents of directory:")

# List all files and folders
for item in os.listdir(path):
    print(item)