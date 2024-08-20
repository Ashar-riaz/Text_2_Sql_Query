import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def respones(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    combined_input = f"{prompt}\n{question}"
    response = model.generate_content(combined_input)
    return response.text

def sql_query(sql, db):
    # Clean up the SQL query by removing code block formatting
    sql = sql.strip().strip('```sql').strip('```')
    
    # Display the SQL query in the UI
    st.write("Generated SQL Query:")
    st.code(sql, language='sql')
    
    # Execute the cleaned SQL query
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.OperationalError as e:
        st.error(f"SQL error: {e}")
        rows = []
    finally:
        conn.commit()
        conn.close()

    # Display the query results in the UI
    st.write("Query Results:")
    if rows:
        for row in rows:
            st.write(row)
    else:
        st.write("No results found.")
    
    return rows

# Example usage
question = st.text_input("Enter your question:")
prompt = '''You are an expert in converting English questions to sql querry!
The SQL database has the name is car and the following columns - Make and model,
Price, Mileage (mpg), Repair record 1978, Headroom (in.), Trunk space (cu. ft.),
Weight (lbs.), Length (in.), Turn circle (ft.), Displacement (cu. in.), Gear ratio, Car origin

Example: Tell me the name of car which mileage is larger then 20, the sql command will be something like this
SELECT Make and model FROM car WHERE Mileage (mpg)> 20;
I provide more question then give the sql query'''

if st.button("Generate SQL Query"):
    response = respones(question, prompt)
    data = sql_query(response, "automobile.db")
