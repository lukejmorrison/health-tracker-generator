# generate_tracker.py
import pandas as pd
import os  # Import the os module to handle paths
import sys # Import sys to check python version if needed

print("Script started...")

# Define the output filename
output_filename = 'Symptom_and_Health_Tracker.xlsx'
# Define the directory where the script is located
# Use sys.argv[0] for potentially better compatibility when run via batch file
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# Create the full path for the output file
output_filepath = os.path.join(script_dir, output_filename)

print(f"Attempting to save Excel file to: {output_filepath}")

try:
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # Provide the direct file path instead of a buffer.
    with pd.ExcelWriter(output_filepath, engine='xlsxwriter') as writer:

        # --- Sheet 1: Visit Log Template ---
        print("Creating 'Visit Log Template' sheet...")
        visit_log_data = {
            'Visit Detail': ['Visit Date:', 'Doctor Name:', 'Reason for Visit:'],
            'Information': ['', '', '']
        }
        df_visit_details = pd.DataFrame(visit_log_data)
        # Write without header and index for this specific layout part
        df_visit_details.to_excel(writer, sheet_name='Visit Log Template', index=False, startrow=0, header=False)

        # Add space (write an empty DataFrame)
        pd.DataFrame([[]]).to_excel(writer, sheet_name='Visit Log Template', index=False, header=False, startrow=df_visit_details.shape[0] + 1)

        # Current Symptoms Table
        symptoms_data = {
            'Symptom': ['Example: Sinus Congestion', 'Example: Headache', 'Example: Swollen Feet'],
            'Description': ['Pressure in sinuses, difficulty breathing through nose', 'Dull ache behind eyes', 'Noticeable puffiness, especially ankles'],
            'First Noticed': ['Approx. 2 years ago', 'Approx. 2 years ago', 'Approx. 3 months ago'],
            'Frequency': ['Comes and goes, 5-6 times in last 2 years', 'Almost daily, worse during sinus episodes', 'Off and on, maybe few times a week'],
            'Duration': ['Lasts 2-3 weeks per episode', 'Varies, few hours to all day', 'Lasts most of the day when it occurs'],
            'Severity (1-10)': [6, 5, 4],
            'Triggers': ['Weather changes?', 'Sinus congestion', 'Sitting/standing long periods?'],
            'Relief': ['Decongestants (partial)', 'Pain reliever (partial)', 'Elevating feet'],
            'Impact on Daily Life': ['Fatigue, missed work days', 'Difficulty concentrating', 'Discomfort'],
            'Notes': ['Seems worse than typical colds', 'Tension-like', 'No pain, just swelling']
        }
        df_symptoms = pd.DataFrame(symptoms_data)
        # Add empty rows for user input
        empty_symptoms = pd.DataFrame([[''] * len(symptoms_data.keys())] * 5, columns=symptoms_data.keys())
        df_symptoms_full = pd.concat([df_symptoms, empty_symptoms], ignore_index=True)
        # Write the symptoms table with header
        df_symptoms_full.to_excel(writer, sheet_name='Visit Log Template', index=False, startrow=df_visit_details.shape[0] + 3)

        # Calculate next starting row dynamically
        start_row_meds_header = df_visit_details.shape[0] + 3 + df_symptoms_full.shape[0] + 1

        # Add space and header for Medications Update
        pd.DataFrame([['Current Medications/Treatments Update:']]).to_excel(writer, sheet_name='Visit Log Template', index=False, header=False, startrow=start_row_meds_header)
        meds_update_data = {
            'Medication/Treatment': [''],
            'Change (New/Stopped/Dose Adj.)': [''],
            'Date of Change': [''],
            'Reason/Effect': ['']
        }
        df_meds_update = pd.DataFrame(meds_update_data)
        empty_meds = pd.DataFrame([[''] * len(meds_update_data.keys())] * 3, columns=meds_update_data.keys())
        df_meds_update_full = pd.concat([df_meds_update, empty_meds], ignore_index=True)
        # Write meds update table with header
        df_meds_update_full.to_excel(writer, sheet_name='Visit Log Template', index=False, startrow=start_row_meds_header + 2)

        # Calculate next starting row
        start_row_questions_header = start_row_meds_header + 2 + df_meds_update_full.shape[0] + 1

        # Add space and header for Questions
        pd.DataFrame([['Questions for Doctor This Visit:']]).to_excel(writer, sheet_name='Visit Log Template', index=False, header=False, startrow=start_row_questions_header)
        questions_data = {
            'Question': ['Example: Could we investigate my immune system, perhaps IgG levels?', 'Example: What could be causing the swollen feet?', ''],
            'Doctor\'s Answer/Notes': ['', '', '']
        }
        df_questions = pd.DataFrame(questions_data)
        df_questions.to_excel(writer, sheet_name='Visit Log Template', index=False, startrow=start_row_questions_header + 2)

        # Calculate next starting row
        start_row_plan_header = start_row_questions_header + 2 + df_questions.shape[0] + 1

        # Add space and header for Doctor's Plan
        pd.DataFrame([['Doctor\'s Assessment & Plan from This Visit:']]).to_excel(writer, sheet_name='Visit Log Template', index=False, header=False, startrow=start_row_plan_header)
        plan_data = {
            'Assessment / Plan Notes': [''] * 5 # Provide empty rows for notes
        }
        df_plan = pd.DataFrame(plan_data)
        df_plan.to_excel(writer, sheet_name='Visit Log Template', index=False, startrow=start_row_plan_header + 2)

        # Add instructions note via xlsxwriter
        worksheet = writer.sheets['Visit Log Template']
        # Position the textbox relative to the last written data if possible, or fixed position
        worksheet.insert_textbox('K1', # Adjusted position to avoid overlap
                                 'Instructions:\n\n1. Right-click the "Visit Log Template" tab below.\n2. Select "Move or Copy".\n3. Check "Create a copy".\n4. Click "OK".\n5. Rename the new sheet with the visit date (e.g., "Visit Log - 2025-04-15").\n6. Fill out the details for that specific visit on the new sheet.',
                                 {'width': 400, 'height': 120, 'x_offset': 10, 'y_offset': 10, 'font': {'color': 'red', 'size': 9}})

        # Adjust column widths for Template Sheet - adjust indices based on final columns
        worksheet.set_column('A:A', 20) # Symptom / Question / Med Name / Detail Header
        worksheet.set_column('B:B', 40) # Description / Answer / Change / Info
        worksheet.set_column('C:C', 20) # First Noticed / Date
        worksheet.set_column('D:D', 30) # Frequency / Reason
        worksheet.set_column('E:E', 15) # Duration
        worksheet.set_column('F:F', 15) # Severity
        worksheet.set_column('G:G', 20) # Triggers
        worksheet.set_column('H:H', 20) # Relief
        worksheet.set_column('I:I', 30) # Impact
        worksheet.set_column('J:J', 30) # Notes


        # --- Sheet 2: Symptom Timeline Summary ---
        print("Creating 'Symptom Timeline Summary' sheet...")
        timeline_data = {
            'Symptom': ['Example: Recurrent Sinus Colds', 'Example: Headaches', 'Example: Dry Cough', 'Example: Swollen Feet'],
            'First Noticed / Started': ['Approx. 2 years ago', 'Approx. 2 years ago', 'Approx. 2 years ago', 'Approx. 3 months ago'],
            'Progression / Key Notes': ['Approx. 5-6 episodes in 2 years, each lasting 2-3 weeks. Unusual frequency for me.', 'Almost daily, seem linked to sinus issues.', 'Persistent, lingering cough, worse at night.', 'Intermittent, no pain. Similar to father\'s experience.']
        }
        df_timeline = pd.DataFrame(timeline_data)
        empty_timeline = pd.DataFrame([[''] * len(timeline_data.keys())] * 5, columns=timeline_data.keys())
        df_timeline_full = pd.concat([df_timeline, empty_timeline], ignore_index=True)
        df_timeline_full.to_excel(writer, sheet_name='Symptom Timeline Summary', index=False)
        worksheet_timeline = writer.sheets['Symptom Timeline Summary']
        worksheet_timeline.set_column('A:A', 25) # Symptom
        worksheet_timeline.set_column('B:B', 25) # First Noticed
        worksheet_timeline.set_column('C:C', 60) # Progression

        # --- Sheet 3: Test Results Log ---
        print("Creating 'Test Results Log' sheet...")
        tests_data = {
            'Test Name': ['Example: Complete Blood Count (CBC)', 'Example: Basic Metabolic Panel (BMP)', 'Example: IgG4 Level (if ordered)'],
            'Date Ordered': ['YYYY-MM-DD', 'YYYY-MM-DD', 'YYYY-MM-DD'],
            'Date Performed': ['YYYY-MM-DD', 'YYYY-MM-DD', 'YYYY-MM-DD'],
            'Results Summary': ['e.g., Within normal limits', 'e.g., Sodium slightly low', 'e.g., Value and reference range'],
            'Doctor\'s Notes / Interpretation': ['', '', ''],
            'Reference Range': ['Provided on report', 'Provided on report', 'Provided on report'],
            'Report Location (Optional)': ['e.g., MyChart portal, Folder X', '', '']
        }
        df_tests = pd.DataFrame(tests_data)
        empty_tests = pd.DataFrame([[''] * len(tests_data.keys())] * 10, columns=tests_data.keys())
        df_tests_full = pd.concat([df_tests, empty_tests], ignore_index=True)
        df_tests_full.to_excel(writer, sheet_name='Test Results Log', index=False)
        worksheet_tests = writer.sheets['Test Results Log']
        worksheet_tests.set_column('A:A', 30) # Test Name
        worksheet_tests.set_column('B:B', 15) # Date Ordered
        worksheet_tests.set_column('C:C', 15) # Date Performed
        worksheet_tests.set_column('D:D', 40) # Results Summary
        worksheet_tests.set_column('E:E', 40) # Doctor's Notes
        worksheet_tests.set_column('F:F', 20) # Reference Range
        worksheet_tests.set_column('G:G', 30) # Report Location

        # --- Sheet 4: Family History ---
        print("Creating 'Family History' sheet...")
        family_history_data = {
            'Condition / Illness': ['Example: Heart Issues', 'Example: Swollen Feet (related to meds?)', 'Example: Allergies'],
            'Relation': ['Father', 'Father', 'Mother'],
            'Details / Notes': ['Specific condition if known', 'Mentioned it occurred while on heart medication', 'Seasonal allergies']
        }
        df_family_history = pd.DataFrame(family_history_data)
        empty_family = pd.DataFrame([[''] * len(family_history_data.keys())] * 5, columns=family_history_data.keys())
        df_family_history_full = pd.concat([df_family_history, empty_family], ignore_index=True)
        df_family_history_full.to_excel(writer, sheet_name='Family History', index=False)
        worksheet_family = writer.sheets['Family History']
        worksheet_family.set_column('A:A', 30) # Condition
        worksheet_family.set_column('B:B', 15) # Relation
        worksheet_family.set_column('C:C', 50) # Details

        # --- Sheet 5: Medications & Treatments History ---
        print("Creating 'Medications & Treatments History' sheet...")
        meds_history_data = {
            'Medication / Treatment': ['Example: Amoxicillin', 'Example: Fluticasone Nasal Spray', 'Example: Ibuprofen'],
            'Dosage / Frequency': ['500mg 3x/day', '2 sprays/nostril daily', '400mg as needed'],
            'Start Date': ['YYYY-MM-DD', 'YYYY-MM-DD', 'Ongoing'],
            'End Date': ['YYYY-MM-DD', '', ''],
            'Reason Prescribed': ['Sinus Infection', 'Sinus Congestion/Allergies', 'Headaches'],
            'Effectiveness': ['Resolved infection', 'Helped somewhat with congestion', 'Temporary relief of headache'],
            'Side Effects Noted': ['None', 'Occasional nosebleed', 'None']
        }
        df_meds_history = pd.DataFrame(meds_history_data)
        empty_meds_hist = pd.DataFrame([[''] * len(meds_history_data.keys())] * 10, columns=meds_history_data.keys())
        df_meds_history_full = pd.concat([df_meds_history, empty_meds_hist], ignore_index=True)
        df_meds_history_full.to_excel(writer, sheet_name='Medications & Treatments History', index=False)
        worksheet_meds = writer.sheets['Medications & Treatments History']
        worksheet_meds.set_column('A:A', 30) # Med Name
        worksheet_meds.set_column('B:B', 25) # Dosage
        worksheet_meds.set_column('C:C', 15) # Start Date
        worksheet_meds.set_column('D:D', 15) # End Date
        worksheet_meds.set_column('E:E', 30) # Reason
        worksheet_meds.set_column('F:F', 30) # Effectiveness
        worksheet_meds.set_column('G:G', 30) # Side Effects

    print(f"Successfully created Excel file: {output_filename}")

except ImportError as ie:
     print(f"Error: Missing required library - {ie}. Please install required libraries.")
     print("You may need to run: pip install pandas openpyxl xlsxwriter")
except Exception as e:
    print(f"An error occurred: {e}")
    # Consider adding more specific error handling if needed

print("Script finished.")
