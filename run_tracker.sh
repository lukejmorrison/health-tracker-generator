#!/usr/bin/env bash
# Shell script to set up environment and run the health tracker generator on Linux/macOS
# Updated to ensure requirements are checked/installed even if venv exists.

# Define the virtual environment directory name
VENV_DIR="venv"

# Define the requirements
REQUIREMENTS="pandas openpyxl xlsxwriter"

# --- Helper function for error exiting ---
error_exit() {
    echo "Error: $1" >&2
    # Attempt to deactivate if venv was activated in this script session
    # Check if the deactivate function exists before calling it
    if command -v deactivate &> /dev/null; then
        echo "Deactivating environment before exit..."
        deactivate
    fi
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
    echo "Virtual environment created."
else
    echo "Found existing virtual environment."
fi

# --- Activate the environment (works for both new and existing venv) ---
echo "Activating environment..."
source "$VENV_DIR/bin/activate" || error_exit "Failed to activate virtual environment using source."

# --- Ensure requirements are installed (pip will handle existing packages) ---
echo "Ensuring required packages are installed: $REQUIREMENTS..."
pip install $REQUIREMENTS || error_exit "Failed to install/verify required Python packages."
echo "Requirements checked/installed successfully."

# --- Run the Python script ---
echo "Running the Python script (generate_tracker.py)..."
python3 generate_tracker.py || error_exit "Python script execution failed."

echo "Script finished successfully. Excel file should be generated."

# --- Deactivate environment ---
# Good practice, though exiting the script usually handles this.
if command -v deactivate &> /dev/null; then
    echo "Deactivating environment..."
    deactivate
fi

exit 0
