from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    user = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    que = simpledialog.askstring(title="Question", prompt="Is the sky blue?")
    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct
    if que == "yes":
        user+=1

    #      // 4.  if the user's answer was correct, add one to their score
    que2 = simpledialog.askstring(title="Question", prompt="Is dirt brown")

    if que2 == "yes":
        user+=1

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    que3 = simpledialog.askstring(title="Question", prompt="Is grass green")
    #      // 2.  Ask the user a question

    #      // 3.  Use an if statement to check if their answer is correct
    if que3 == "yes":
        user += 1
    messagebox.showinfo(message=user)
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    window.mainloop()
    # Run the window's .mainloop() method
