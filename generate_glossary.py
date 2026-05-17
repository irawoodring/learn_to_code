import sqlite3

# Configuration
DB_NAME = "glossary.db"
TABLE_NAME = "glossary"
OUTPUT_FILE = "glossary.md"

# Connect to SQLite database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Read all records
cursor.execute(f"""
    SELECT term, definition, code
    FROM {TABLE_NAME}
    ORDER BY term COLLATE NOCASE
""")

rows = cursor.fetchall()

# Create markdown output
with open(OUTPUT_FILE, "w", encoding="utf-8") as md_file:

    md_file.write("# Glossary\n\n")

    for term, definition, code_flag in rows:

        # Wrap in backticks if integer column == 1
        if code_flag == 1:
            formatted_term = f"**`{term}`**"
        else:
            formatted_term = f"**{term}**"

        md_file.write(f"{formatted_term}\n\n")
        md_file.write(f"{definition}\n\n")

# Cleanup
conn.close()

print(f"Markdown glossary exported to '{OUTPUT_FILE}'")
