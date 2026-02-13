#!/bin/bash

echo "Starting Bible Scramble Web Application..."
echo "========================================"
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "Error: app.py not found. Please run this script from the web directory."
    exit 1
fi

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Flask not found. Installing Flask..."
    pip3 install flask
fi

echo "Starting web server on http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py