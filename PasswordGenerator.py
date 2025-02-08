from tkinter import * 
import random 

root = Tk() 
root.geometry("900x800") 
root.configure(bg="#F0F0F0") 

passwrd = StringVar() 
passlen = IntVar() 
passlen.set(0) 
include_Uletters = BooleanVar() 
include_Lletters = BooleanVar() 
include_digits = BooleanVar() 
include_special_chars = BooleanVar() 
 
def generate():   
    characters = [] 
    if include_Uletters.get(): 
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 
    if include_Lletters.get(): 
        characters.extend('abcdefghijklmnopqrstuvwxyz') 
    if include_digits.get(): 
        characters.extend('0123456789') 
    if include_special_chars.get(): 
        characters.extend('.:,!@#$%^&*()_') 
    if not characters: 
        passwrd.set("Please select at least one option!") 
        return 
    
    password = "".join(random.choice(characters) for _ in range(passlen.get())) 
    passwrd.set(password) 
    display_password_as_labels(password) 
 
def display_password_as_labels(password): 
    # Clear any existing labels 
    for widget in char_frame.winfo_children(): 
        widget.destroy() 
      
    for i, char in enumerate(password): 
        label = Label(char_frame, text=char, font=("Helvetica", 18), relief="solid", padx=5, pady=5, bg="#F0F0F0") 
        label.place(x=i * 30, y=0) 
        label.bind("<Button-1>", on_drag_start) 
        label.bind("<B1-Motion>", on_drag_motion) 

def on_drag_start(event): 
    widget = event.widget 
    widget._drag_start_x = event.x 
    widget._drag_start_y = event.y 

def on_drag_motion(event): 
    widget = event.widget 
    x = widget.winfo_x() - widget._drag_start_x + event.x 
    y = widget.winfo_y() - widget._drag_start_y + event.y 
    widget.place(x=x, y=y) 
    update_password_from_labels() 
  
def update_password_from_labels(): 
    labels = sorted(char_frame.winfo_children(), key=lambda label: label.winfo_x()) 
    password = "".join([label.cget("text") for label in labels]) 
    passwrd.set(password) 

Label(root, text="Password Generator", font=("Comic Sans MS", 40, "bold"), bg="#F0F0F0").pack() 
Label(root, text="Enter the length of the password", font=("Comic Sans MS", 20, "bold italic"), bg="#F0F0F0").pack() 
Entry(root, textvariable=passlen, font=("Helvetica", 17), width=30).pack(pady=10) 
Label(root, text="Choose what you want to include in your password", font=("Comic Sans MS", 20, "bold italic"), bg="#F0F0F0").pack() 

Checkbutton(root, text="Include Uppercase Letters", variable=include_Uletters, font=("Helvetica", 14), bg="#F0F0F0").pack(pady=5) 
Checkbutton(root, text="Include Lowercase Letters", variable=include_Lletters, font=("Helvetica", 14), bg="#F0F0F0").pack(pady=5) 
Checkbutton(root, text="Include Digits", variable=include_digits, font=("Helvetica", 14), bg="#F0F0F0").pack(pady=5) 
Checkbutton(root, text="Include Special Characters", variable=include_special_chars, font=("Helvetica", 14), bg="#F0F0F0").pack(pady=5) 

Button(root, text="Generate Password", command=generate, font=("Helvetica", 16), height=1, bg="#F0F0F0").pack(pady=15)  

char_frame = Frame(root, width=700, height=50, bg="#F0F0F0") 
char_frame.pack(pady=10) 

Entry(root, textvariable=passwrd, font=("Helvetica", 17), width=35).pack(pady=3) 

Button(root, text="Regenerate Password", command=generate, font=("Helvetica", 16), height=1, bg="#F0F0F0").pack(pady=1) 

root.mainloop()

