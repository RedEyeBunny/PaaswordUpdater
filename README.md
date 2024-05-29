# AutoPass Application

## Overview
**AutoPass** is a simple GUI application developed using Python and Tkinter, designed to manage and retrieve website credentials. It allows users to add and look up details such as website name, URL, login ID, password, pin, and email. The data is stored in a MySQL database.

## Requirements
- Python 3.x
- Tkinter (usually comes with Python)
- MySQL Server
- `mysql-connector-python` library

## Setup
1. **Install MySQL Server:**
   - Download and install MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/).
   - Create a database named `sec`.
   - Create a table named `info` in the `sec` database using the following SQL command:
     ```sql
     CREATE TABLE info (
         website_name VARCHAR(255),
         website_url VARCHAR(255),
         login_id VARCHAR(255),
         password VARCHAR(255),
         pin VARCHAR(255),
         email VARCHAR(255)
     );
     ```

2. **Install Python Libraries:**
   - Ensure you have `mysql-connector-python` installed. You can install it using pip:
     ```sh
     pip install mysql-connector-python
     ```

## Configuration
Update the database connection details in the script:
```python
db = sqltor.connect(
    host='localhost',
    user='your_mysql_username',
    password='your_mysql_password',
    database='sec'
)
```
### For linux users 
1. Install the __Autokey__ application.
2. Copy and paste the script in sample scripts sectionand give the script a good name.
3. Set a hotkey for the script like ```<ctrl> + <shift> + <q>``` or something of your choice.
4. Happy password browsing!

### For windows users
1. Install the __Autohotkey__ application.
2. Create a new script in Autohotkey-
     ```
     AutoHotkey script to run a Python script-
     Run, python.exe "C:\path\to\your_script.py"
    ```
     python.exe is your python interpreter.
3. To define a hotkey, for example crtl+alt+p type-``` ^!p```.
4. So this is how your script should look like finally -
     ```
     ; Define the hotkey Ctrl+Alt+O
     ^!p::
         Run, python.exe "C:\path\to\another_script.py"
         return
     ```
5. Happy password browsing!
