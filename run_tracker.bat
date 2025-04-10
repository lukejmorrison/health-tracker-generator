@echo off
REM Batch script to set up environment and run the health tracker generator

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

    echo Activating environment and installing requirements...
    REM Use 'call' to run the activate script and return control here
    call "%VENV_DIR%\Scripts\activate.bat"
    if %errorlevel% neq 0 (
        echo Error: Failed to activate virtual environment using activate.bat.
        pause
        exit /b 1
    )

    echo Installing packages: %REQUIREMENTS%...
    pip install %REQUIREMENTS%
    if %errorlevel% neq 0 (
        echo Error: Failed to install required Python packages.
        pause
        exit /b 1
    )
    echo Requirements installed successfully.
) else (
    echo Found existing virtual environment. Activating...
    REM Activate existing environment
    call "%VENV_DIR%\Scripts\activate.bat"
     if %errorlevel% neq 0 (
        echo Error: Failed to activate existing virtual environment using activate.bat.
        pause
        exit /b 1
    )
)

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
