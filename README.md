# Symptom and Health Tracker Generator

## Description

This project contains a Python script (`generate_tracker.py`) that creates a structured Excel spreadsheet (`.xlsx`) designed to help document illness symptoms, track medical tests, manage medication history, and record family health history. The goal is to provide an organized way to gather data for discussions with healthcare providers.

It also includes helper scripts (`run_tracker.bat` for Windows, `run_tracker.sh` for Linux/macOS) for easier setup and execution.

## Features

The generated Excel workbook (`Symptom_and_Health_Tracker.xlsx`) includes the following sheets:

1.  **Visit Log Template:** A template sheet to be duplicated for each doctor's visit. It includes sections for:
    * Visit Details (Date, Doctor, Reason)
    * Current Symptoms (Detailed tracking: description, frequency, duration, severity, triggers, relief, impact)
    * Medication/Treatment Updates for the visit
    * Questions for the Doctor
    * Doctor's Assessment & Plan Notes
2.  **Symptom Timeline Summary:** A cumulative overview tracking major symptoms, when they started, and how they've progressed over time.
3.  **Test Results Log:** A log for all medical tests (blood work, scans, etc.), including dates, results summaries, and doctor interpretations.
4.  **Family History:** Records relevant medical conditions within the family.
5.  **Medications & Treatments History:** A comprehensive list of all medications and treatments tried, including dosage, duration, effectiveness, and side effects.

## Prerequisites

* [Python 3](https://www.python.org/downloads/) (Version 3.6 or higher recommended)
* [pip](https://pip.pypa.io/en/stable/installation/) (usually included with Python 3)
* [Git](https://git-scm.com/) (Optional, for version control)

## Setup and Installation (Manual)

These steps are for setting up manually using a terminal. Alternatively, use the helper scripts (`run_tracker.bat` or `run_tracker.sh`).

1.  **Clone the Repository (Optional):**
    ```bash
    git clone <your-repository-url>
    cd <repository-folder-name>
    ```
    Alternatively, download the `generate_tracker.py` script and optionally the helper scripts into a local folder.

2.  **Navigate to Project Directory:**
    Open your terminal or command prompt and change to the directory where you saved the script(s).
    ```bash
    cd /path/to/your/project/folder
    ```

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    # Use python3 on Linux/macOS, python on Windows if python3 isn't aliased
    python3 -m venv venv
    ```

4.  **Activate the Virtual Environment:** Choose the command based on your Operating System and Terminal:
    * **Windows PowerShell:**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
        *(If you encounter an Execution Policy error, run `Set-ExecutionPolicy RemoteSigned -Scope Process` in the same terminal, then try activating again).*
    * **Windows Command Prompt (cmd.exe):**
        ```cmd
        .\venv\Scripts\activate.bat
        ```
    * **Linux / macOS (bash, zsh, etc.):**
        ```bash
        source venv/bin/activate
        ```
    * *Success is indicated by `(venv)` appearing at the start of your terminal prompt.*

5.  **Install Dependencies:** Make sure the virtual environment is active before running:
    ```bash
    pip install pandas openpyxl xlsxwriter
    ```

## Usage

### Option 1: Using the Helper Scripts

1.  Save `generate_tracker.py` and the appropriate helper script (`run_tracker.bat` for Windows, `run_tracker.sh` for Linux/macOS) in the same folder.
2.  **On Windows:**
    * Double-click `run_tracker.bat`.
    * Follow the prompts. Press any key to close the window when finished.
3.  **On Linux / macOS:**
    * Open your terminal in the project folder.
    * Make the script executable (only need to do this once):
        ```bash
        chmod +x run_tracker.sh
        ```
    * Run the script:
        ```bash
        ./run_tracker.sh
        ```
4.  The scripts will automatically:
    * Create the virtual environment (`venv`) if it doesn't exist.
    * Activate the environment.
    * Install the required Python packages if the environment was just created.
    * Run the `generate_tracker.py` script.

### Option 2: Manual Execution (All Platforms)

1.  **Ensure Virtual Environment is Active:** Follow Step 4 in Setup if needed. You should see `(venv)` at the start of your terminal prompt.
2.  **Run the Script:**
    ```bash
    # Use python3 on Linux/macOS, python on Windows
    python3 generate_tracker.py
    ```
3.  **Output:** The script will create (or overwrite) the `Symptom_and_Health_Tracker.xlsx` file in the same directory.

### Using the Spreadsheet

* Open the generated `Symptom_and_Health_Tracker.xlsx` file.
* Fill in your historical data on the relevant sheets (Timeline, Tests, Family History, Meds History).
* **Before each doctor's visit:** Right-click the `Visit Log Template` sheet tab, select "Move or Copy...", check "Create a copy", and click OK. Rename the new sheet (e.g., "Visit 2025-04-15") and fill it out.

## Spreadsheet Structure

* **Visit Log Template:** Use as a blueprint for individual visit records. **Duplicate this sheet for each appointment.**
* **Symptom Timeline Summary:** High-level overview of your main symptoms over time.
* **Test Results Log:** Central place for all test results.
* **Family History:** Track genetic predispositions or relevant family conditions.
* **Medications & Treatments History:** Log what you've taken/tried and how it worked.

---

*This README provides instructions for setting up and running the script locally on Windows, Linux, and macOS.*
