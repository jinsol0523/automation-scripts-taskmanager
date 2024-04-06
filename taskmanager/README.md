# Task Manager

## Overview
Task Manager is a simple graphical task management application written in Python. It provides an intuitive user interface for managing tasks efficiently.

## Features
- **Graphical User Interface (GUI)**: The application features a Tkinter-based GUI, allowing users to interact with the task manager through buttons, input fields, and pop-up dialogs.
- **Create Task**: Users can create a new task by providing a task name and due date.
- **View Tasks**: Users can view all existing tasks along with their due dates.
- **Edit Task**: Users can edit an existing task's name or due date.
- **Remove Task**: Users can remove an existing task from the list.
- **Data Persistence**: Tasks are saved to a JSON file (`tasks.json`) for persistence across sessions.

## Requirements
- Python 3.x
- `tkinter` library (for graphical user interface)
- JSON file for storing tasks

## Usage
1. **Installation**: No installation required. Simply download the Python script (`task_manager.py`) and ensure you have Python installed on your system.
2. **Running the Application**:
    - Open a terminal or command prompt.
    - Navigate to the directory where `task_manager.py` is located.
    - Run the script by executing the command:
        ```
        python task_manager.py
        ```
3. **Using the Application**:
    - Upon running the script, the Task Manager GUI will appear.
    - Use the buttons provided in the GUI to perform various actions such as creating, viewing, editing, and removing tasks.

## Examples
- **Creating a Task**: Users can enter task details in the provided input fields and click the "Create Task" button to create a new task.
- **Viewing Tasks**: Users can click the "View Tasks" button to see a list of all existing tasks.
- **Editing and Removing Tasks**: Users can select a task from the list and click the "Edit Task" or "Remove Task" button to make changes or delete the task.

## Contributing
Contributions are welcome! If you have any suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
