import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import lcs_process
import time

def upload_file(text_input, type):
    file_path = filedialog.askopenfilename(
        title="Choose File " + type,
        filetypes=[("Text Files", "*.txt")]
    )
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                code_content = file.read()
                text_input.delete("1.0", tk.END)
                text_input.insert(tk.END, code_content)
        except Exception as e:
            messagebox.showerror("Error", f"Fail read file: {e}")


def test_print_output(input, output):
    output.delete("1.0", 'end-1c')
    output.insert("1.0", input)


def process_files(s1, s2, output):
    str1 = str(s1)
    str2 = str(s2)
    start = time.perf_counter()
    lcs_value = lcs_process.lcs(s1, s2)
    end = time.perf_counter()
    runtime = end-start
    max_length = max(len(s1), len(s2)) + 1

    output_text = (
        "str1 = " + s1 + "\n"
        "str2 = " + s2 + "\n"
        "LCS = " + str(lcs_value) + "\n"
        "Runtime = " + str(runtime) + "\n"
        "Score = " + str(lcs_value/max_length) + "\n"
        )
    output.delete("1.0", 'end-1c')
    output.insert("1.0", output_text)
    

def run_app():
    # INIT
    root = tk.Tk()
    root.title("Plagiarism Detection Tool")
    root.geometry("1200x600")
    

    # FRAME INPUT
    frame_input = tk.Frame(root, padx=10, pady=5)
    frame_input.pack(fill="both", expand=True)
    
    label_input_a = tk.Label(frame_input, text="File A", font=("Arial", 10, "bold"))
    label_input_a.pack(anchor="w")

    text_input_a = tk.Text(frame_input, height=10)
    text_input_a.pack(side="top", fill="x", padx=5, expand=True)
    
    label_input_b = tk.Label(frame_input, text="File B", font=("Arial", 10, "bold"))
    label_input_b.pack(anchor="w")

    text_input_b = tk.Text(frame_input, height=10)
    text_input_b.pack(side="top", fill="x", padx=5, expand=True)


    # FRAME BUTTONS
    frame_buttons = tk.Frame(root, padx=10)
    frame_buttons.pack(fill="x")
    
    btn_upload_a = tk.Button(frame_buttons, text="Upload File A", 
                           command=lambda: upload_file(text_input_a, "A")
                           )
    btn_upload_a.pack(side="left", padx=5)

    btn_upload_b = tk.Button(frame_buttons, text="Upload File B", 
                           command=lambda: upload_file(text_input_b, "B")
                           )
    btn_upload_b.pack(side="left", padx=5)
    
    input_from_a = "alp"
    input_from_b = text_input_b.get('1.0', 'end-1c')
    
    btn_process = tk.Button(frame_buttons, text="Process Files", bg="lightblue", 
                            # command=lambda: process_files(input_from_a, input_from_b, text_output)
                            command=lambda: test_print_output(input_from_a, text_output)
                            
                            )
    btn_process.pack(side="right", padx=5)
    

    # FRAME OUTPUT
    frame_output = tk.Frame(root, padx=10, pady=10)
    frame_output.pack(fill="both", expand=True)
    
    label_output = tk.Label(frame_output, text="Result:", font=("Arial", 10, "bold"))
    label_output.pack(anchor="w")

    text_output = tk.Text(frame_output, height=10)

    scrollbar = ttk.Scrollbar(frame_output, orient="vertical", command=text_output.yview)
    text_output.configure(yscroll=scrollbar.set)

    text_output.pack(side="left", fill="both", padx=5, expand=True)
    scrollbar.pack(side="right", fill="y")
    

    root.mainloop()


if __name__ == "__main__":
    run_app()