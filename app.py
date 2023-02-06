import json
import tkinter as tk
from tkinter import filedialog
from datetime import datetime


# Function to open a file dialog to select the JSON file and load the data
def load_file():
    # Open the file dialog to select the JSON file
    file_path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")])

    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)

    return data


def convert_datetime_created(date_time_str):
    # Parse the date-time string using the datetime library
    date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Format the datetime object to "day-month-year hour-minutes" format
    formatted_date_time = date_time_obj.strftime("%d-%m-%Y %H:%M")

    return formatted_date_time


def convert_datetime_due(date_time_str):
    # Convert the date time string to a datetime object
    dt = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%SZ')

    # Format the datetime object as day-month-year hour-minutes
    formatted_date_time = dt.strftime("%d-%m-%Y %H-%M")

    return formatted_date_time


# Function to extract the desired fields from the tasks
def extract_fields(tasks):
    # Create a list to store the desired fields
    completed_fields = []

    # Add the headers to the list
    completed_fields.append("Task Title")
    completed_fields.append(" , ")
    completed_fields.append("Created")
    completed_fields.append(" , ")
    completed_fields.append("Due")
    completed_fields.append(" , ")
    completed_fields.append("Status")
    completed_fields.append("\n")

    # Loop through the tasks and add the completed ones to the list
    for item in tasks:
        if item["status"] == "completed":
            completed_fields.append(item["title"])
            completed_fields.append(" , ")

            # Convert the "created" time to the desired format
            time_formated_created = convert_datetime_created(item["created"])
            completed_fields.append(time_formated_created)

            completed_fields.append(" , ")

            # Convert the "due" time to the desired format
            time_formated_due = convert_datetime_due(item["due"])
            completed_fields.append(time_formated_due)

            completed_fields.append(" , ")
            completed_fields.append(item["status"])
            completed_fields.append("\n")

    return completed_fields

# Function to extract the list1 tasks from the JSON data and display them in the text widget


def extract_fields_list1():
    data = load_file()
    all_tasks = data["items"]
    list1_tasks = all_tasks[1]["items"]
    completed_fields = extract_fields(list1_tasks)
    result_text_csv.delete("1.0", tk.END)
    for item in completed_fields:
        result_text_csv.insert(tk.END, item)

# Function to extract the list2 tasks from the JSON data and display them in the text widget


def extract_fields_list2():
    data = load_file()
    all_tasks = data["items"]
    list2_tasks = all_tasks[2]["items"]
    completed_fields = extract_fields(list2_tasks)
    result_text_csv.delete("1.0", tk.END)
    for item in completed_fields:
        result_text_csv.insert(tk.END, item)


# Create the main window
root = tk.Tk()
root.title("JSON Field Extractor")

# Create the button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create the 'Extract list1' button
extract_button_list1 = tk.Button(
    button_frame, text="Extract List1", command=extract_fields_list1)
extract_button_list1.grid(row=0, column=1, padx=10)

extract_button_list2 = tk.Button(
    button_frame, text="Extract list2", command=extract_fields_list2)
extract_button_list2.grid(row=0, column=2, padx=10)

# Create the text widget to display the results
result_text_csv = tk.Text(root, height=30, width=100)
result_text_csv.pack(side=tk.LEFT, fill=tk.Y)


# Create the scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the text field to use the scrollbar
result_text_csv.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text_csv.yview)

# Start the main event loop
root.mainloop()
