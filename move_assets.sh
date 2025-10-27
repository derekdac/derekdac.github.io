#!/bin/bash
mkdir -p assets
for dir in wp-content/uploads/*; do
  mv "$dir" assets/
done
