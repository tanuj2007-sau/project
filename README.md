# Meeting Scheduler with Reminders

## Project Title

**Meeting Scheduler with Reminders**

## Overview of the Project

This project is a Python-based command-line application that allows
users to easily schedule, view, delete, and track upcoming meetings.\
It stores meeting data in a simple text file and provides reminders for
meetings occurring within the next 24 hours.

## Features

-   Add new meetings with date and time validation\
-   View all scheduled meetings sorted by date\
-   Delete specific meetings\
-   Check upcoming meetings within the next 24 hours\
-   Persistent storage using a text file (`bucket.txt`)\
-   Simple and user-friendly command-line interface

## Technologies / Tools Used

-   **Python 3**\
-   **Datetime module** for date/time processing\
-   **File Handling** (TXT storage)\
-   **Command-line Interface (CLI)**

## Steps to Install & Run the Project

1.  Ensure Python 3 is installed on your system.\

2.  Download the project source code.\

3.  Place the script and `bucket.txt` (optional) in the same folder.\

4.  Open a terminal/command prompt in the project directory.\

5.  Run the program using the command:

    ``` bash
    python filename.py
    ```

6.  Use the menu options displayed to interact with the system.

## Instructions for Testing

-   Test adding meetings using valid and invalid inputs (e.g., past
    dates, incorrect formats).\
-   Try viewing meetings to ensure they are sorted correctly.\
-   Add multiple meetings and test deleting them by selecting their
    index.\
-   Add meetings within the next 24 hours and verify the reminder
    feature works correctly.\
-   Ensure `bucket.txt` is created and updated properly after
    operations.
