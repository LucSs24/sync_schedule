import pandas as pd
from datetime import datetime

EXCLUDED_COURSES = {"O2", "O5", "O6", "O7"}

def parse_schedule(file_path: str):
    """
    Read the .ods schedule file and extract events,
    excluding the selected courses.
    """
    print(f"Lecture du fichier : {file_path}")

    df = pd.read_excel(file_path, engine="odf", header=1)

    events = []

    for index, row in df.iterrows():
        date_str = str(row['Date']).strip()

        if pd.isna(row['Date']) or date_str == 'nan':
            continue

        # Morning
        if pd.notna(row['Course']):
            course = str(row['Course']).strip()

            if course not in EXCLUDED_COURSES and course != 'nan':
                events.append({
                    'date': date_str,
                    'time': str(row['Time']).strip(),
                    'course': course,
                    'location': str(row['Where']).strip() if pd.notna(row['Where']) else "",
                    'professor': str(row['Who']).strip() if pd.notna(row['Who']) else ""
                })

        # Afternoon
        if pd.notna(row['Course.1']):
            course = str(row['Course.1']).strip()

            if course not in EXCLUDED_COURSES and course != 'nan':
                events.append({
                    'date': date_str,
                    'time': str(row['Time.1']).strip(),
                    'course': course,
                    'location': str(row['Where.1']).strip() if pd.notna(row['Where.1']) else "",
                    'professor': str(row['Who.1']).strip() if pd.notna(row['Who.1']) else ""
                })

    print(f"Extraction over : {len(events)}")
    return events
