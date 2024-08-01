#!/bin/bash

# Iterate over each directory in the current directory
for dir in */; do
  # Check if the directory contains a 'src' subdirectory
  if [[ -d "$dir/src" ]]; then
    echo "Running make in $dir/src/"
    # Run the make command in the src directory
    make -C "$dir/src/"
  else
    echo "No src directory in $dir, skipping."
  fi
done