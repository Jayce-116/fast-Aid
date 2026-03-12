import sqlite3
import os

db_path = "C:/Users/LENOVO/fast_aid_backend/app/fast_aid.db"

if not os.path.exists(db_path):
    print(f"Database not found at {db_path}")
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Tables in database:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f" - {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        for col in columns:
            print(f"   - {col[1]} ({col[2]})")
            
    print("\nSample data from guides:")
    try:
        cursor.execute("SELECT * FROM guides LIMIT 1;")
        row = cursor.fetchone()
        print(row)
    except Exception as e:
        print(f"Error reading guides: {e}")
        
    conn.close()
