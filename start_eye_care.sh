#!/bin/bash

# 20-20-20 Eye Care App Startup Script
# This script activates the virtual environment and starts the app

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Change to the app directory
cd "$SCRIPT_DIR"

# Activate the virtual environment
source eye_care_env/bin/activate

# Start the eye care app
python3 eye_care_app.py