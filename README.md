# Text 2 SQL Query

## Overview
This project integrates various tools and libraries to process and manipulate data, generate responses, and potentially include features like creative content generation. The focus is on handling automobile-related data, which is initially stored in an Excel file and then converted into an SQLite database. A web interface is provided via Streamlit.

## Features
- **Streamlit Web Interface:** A user-friendly interface to interact with the application.
- **Excel to SQLite Conversion:** Converts data from an Excel file into an SQLite database using a provided script.
- **SQLite Database:** Stores and manages automobile-related data.
- **Google Generative AI:** Utilized for generating creative responses or content.
- **Environment Configuration:** The `.env` file stores sensitive information and necessary configurations.

## Installation

### Prerequisites
- Python 3.8+
- SQLite
- Pandas

### Setup

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/your-repository.git](https://github.com/Ashar-riaz/Text_2_Sql_query.git
    cd Text_2_Sql_query
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirement.txt
    ```

4. **Set up environment variables:**
    - Rename `.env.example` to `.env` and add your credentials and configurations.

5. **Convert Excel to SQLite Database:**
    - Ensure that `automobile_dataset.xlsx` is in the project directory.
    - Use the `sql.py` to check the database:
      ```bash
      import pandas as pd
      df = pd.read_excel('automobile_dataset.xlsx')
      # Connect to SQLite database and store DataFrame as a SQL table
      conn = sqlite3.connect('automobile.db')
      df.to_sql('car', conn, if_exists='replace', index=False)
      ```
    - This script will create the `automobile.db` file.

6. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

7. **Access the application:**
    - The Streamlit app will be available at the URL provided in your terminal.

## Usage

### Web Interface
- The application provides a web interface via Streamlit. Users can interact with the data, generate content, and view results directly from the browser.

### Database Management
- The `automobile.db` file contains automobile-related data converted from the Excel file. You can manage this database using SQLite tools.

### Configuration
- Ensure that the `.env` file is properly configured with all necessary API keys and environment variables.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to the contributors of the open-source libraries used in this project.

## Demo 
![Screenshot 2024-08-20 231508](https://github.com/user-attachments/assets/3835cf44-e0c4-45e4-8aa6-924f76cab824)



