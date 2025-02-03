#!/bin/bash

# Ensure Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed."
    exit 1
fi

# Install required packages if not already installed
python3 -c "import gradio" 2>/dev/null || python3 -m pip install gradio

# Run the test interface
python3 test_generated_code.py