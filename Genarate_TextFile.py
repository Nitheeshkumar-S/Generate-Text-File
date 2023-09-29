from tkinter.filedialog import askdirectory
import datetime
import uuid
import os
import time
import tkinter

HEADING = "File Generator"
NOTE = "Enter below | No. of files you want to generate | Each file size is 1GB "
GEOMETRY = "400x200"
FILE_SIZE = 1024**3  # 1GB
NO_OF_FILE = 0


def get_entry(ui_window, entry):
    global NO_OF_FILE
    try:
        user_input = int(entry.get())
    except:
        tkinter.messagebox.showerror("Invalid Number", "Please enter a valid number")
        return None
    NO_OF_FILE = user_input
    ui_window.destroy()


if __name__ == "__main__":
    ui_window = tkinter.Tk()
    ui_window.geometry(GEOMETRY)
    heading = tkinter.Label(ui_window, font=("Helvetica", 14), width=400, text=HEADING)
    heading.config(bg="SeaGreen3", fg="LightYellow")
    heading.pack()
    label = tkinter.Label(ui_window, font=("Helvetica", 9), width=400, text=NOTE)
    label.config(bg="SeaGreen3", fg="LightYellow")
    label.pack()
    entry = tkinter.Entry(ui_window)
    entry.place(x=130, y=70)
    ui_button = tkinter.Button(
        ui_window,
        text="START",
        width=15,
        bg="LightYellow",
        fg="green",
        command=lambda: get_entry(ui_window, entry),
    )
    ui_button.place(x=130, y=130)
    ui_window.mainloop()
    folder_path = askdirectory()
    for i in range(1, NO_OF_FILE + 1):
        file_path = (
            folder_path
            + f'/{i}_Temp_File_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
        )
        file = open(file_path, "x")
        while int(os.path.getsize(file_path)) < FILE_SIZE:
            id = str(uuid.uuid4()) + "\n"
            file.write(id * 100000)
            time.sleep(10e-4)
        print(f"File Generated --> {i}GB --> {i/NO_OF_FILE*100}% completed")
        file.close
print("ALL Done")
