#!/usr/bin/env bash
# Shell script to set up environment and run the health tracker generator on Linux/macOS

# Define the virtual environment directory name
VENV_DIR="venv"

# Define the requirements
REQUIREMENTS="pandas openpyxl xlsxwriter"

# --- Helper function for error exiting ---
error_exit() {
    echo "Error: $1" >&2
    exit 1
}

# --- Check if python3 is available ---
echo "Checking for python3..."
if ! command -v python3 &> /dev/null; then
    error_exit "python3 command could not be found. Please install Python 3."
fi

# --- Check if the virtual environment directory exists ---
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR" || error_exit "Failed to create virtual environment."

    echo "Activating environment and installing requirements..."
    # Activate the environment for the current script session
    source "$VENV_DIR/bin/activate" || error_exit "Failed to activate virtual environment using source."

    echo "Installing packages: $REQUIREMENTS..."
    pip install $REQUIREMENTS || error_exit "Failed to install required Python packages."

    echo "Requirements installed successfully."
else
    echo "Found existing virtual environment. Activating..."
    # Activate existing environment
    source "$VENV_DIR/bin/activate" || error_exit "Failed to activate existing virtual environment using source."
fi

# --- Run the Python script ---
echo "Running the Python script (generate_tracker.py)..."
python3 generate_tracker.py || error_exit "Python script execution failed."

echo "Script finished successfully. Excel file should be generated."

# Deactivation is usually not needed here as the script exits,
# but if this were part of a larger script, you might add 'deactivate'
exit 0
