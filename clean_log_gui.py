import tkinter as tk
from tkinter import filedialog, messagebox
import clean_log

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select Google AI Studio Log File",
        filetypes=[("All Files", "*.*"), ("JSON Files", "*.json")]
    )
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        btn_start.config(state=tk.NORMAL)
        lbl_status.config(text="Ready to clean.")

def start_cleaning():
    file_path = entry_path.get()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a file first.")
        return
    
    lbl_status.config(text="Processing...")
    root.update()
    
    try:
        result = clean_log.clean_log(file_path)
        lbl_status.config(text="Done!")
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result)
    except Exception as e:
        lbl_status.config(text="Error!")
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Create main window
root = tk.Tk()
root.title("Google AI Studio Log Cleaner")
root.geometry("500x350")

# File Selection Frame
frame_file = tk.Frame(root, pady=10)
frame_file.pack(fill=tk.X, padx=10)

lbl_instruction = tk.Label(frame_file, text="Select your exported chat log file:")
lbl_instruction.pack(anchor=tk.W)

entry_path = tk.Entry(frame_file, width=50)
entry_path.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

btn_browse = tk.Button(frame_file, text="Browse...", command=select_file)
btn_browse.pack(side=tk.RIGHT)

# Action Frame
frame_action = tk.Frame(root, pady=10)
frame_action.pack(fill=tk.X, padx=10)

btn_start = tk.Button(frame_action, text="Start Cleaning", command=start_cleaning, state=tk.DISABLED, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_start.pack(fill=tk.X)

lbl_status = tk.Label(frame_action, text="Waiting for file...", fg="gray")
lbl_status.pack(pady=5)

# Output Frame
frame_output = tk.Frame(root, pady=10)
frame_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
# Actually let's just use padx/pady.

lbl_result = tk.Label(frame_output, text="Result:")
lbl_result.pack(anchor=tk.W)

text_output = tk.Text(frame_output, height=8)
text_output.pack(fill=tk.BOTH, expand=True)

root.mainloop()
