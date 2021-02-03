from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
if __name__ == '__main__':

    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    ask = simpledialog.askstring(title= "question", prompt="Do you know how to write code")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if ask == "yes":
        messagebox.showinfo(message= "YOU WILL RULE THE WORLD")
    else:
         messagebox.showinfo(message= "SIGN UP FOR CLASS AT THE LEAGUE OF AMAZING PROGRAMERS")

    window.mainloop()
            # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
