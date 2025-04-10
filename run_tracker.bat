@echo off
REM Batch script to set up environment and run the health tracker generator
REM Updated to ensure requirements are checked/installed even if venv exists.

REM Define the virtual environment directory name
set VENV_DIR=venv

REM Define the requirements
set REQUIREMENTS=pandas openpyxl xlsxwriter

REM Check if Python is available
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python does not seem to be installed or added to PATH.
    pause
    exit /b 1
)

REM Check if the virtual environment directory exists
if not exist "%VENV_DIR%\" (
    echo Creating virtual environment in '%VENV_DIR%'...
    python -m venv %VENV_DIR%
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo Virtual environment created.
) else (
    echo Found existing virtual environment.
)

REM Activate the environment (works for both new and existing venv)
echo Activating environment...
call "%VENV_DIR%\Scripts\activate.bat"
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment using activate.bat.
    pause
    exit /b 1
)

REM Ensure requirements are installed (pip will handle existing packages)
echo Ensuring required packages are installed: %REQUIREMENTS%...
pip install %REQUIREMENTS%
if %errorlevel% neq 0 (
    echo Error: Failed to install/verify required Python packages.
    pause
    exit /b 1
)
echo Requirements checked/installed successfully.

REM Run the Python script
echo Running the Python script (generate_tracker.py)...
python generate_tracker.py
if %errorlevel% neq 0 (
    echo Error: Python script execution failed.
    pause
    exit /b 1
)

echo Script finished successfully. Excel file should be generated.
pause
exit /b 0
