#!/bin/bash

# Check if correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

SOURCE_DIR="$1"
DEST_DIR="$2"

# Create a tar.gz archive of the source directory
TAR_FILE="backup_$(date +%Y%m%d_%H%M%S).tar.gz"

# -c: create, -z: compress, -v: verbose, -f tar_file_name, -C change_dir, .: all_files_folder
tar -czvf "$TAR_FILE" -C "$SOURCE_DIR" .

# Move the tar file to the destination directory
mv "$TAR_FILE" "$DEST_DIR"

# Change to the destination directory
cd "$DEST_DIR" || exit

# Extract the tar file
tar -xzvf "$TAR_FILE"

# Remove the tar file after extraction
rm "$TAR_FILE"

echo "Files copied and extracted successfully."
