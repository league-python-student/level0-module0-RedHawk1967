from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable above
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        ask =simpledialog.askinteger(title="title", prompt="Guess the number (1-100)")
        # 4. Ask the user for a guess using a pop-up window, and save their response

        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if ask == random_num:
            sys.exit()
        # 7. if the guess is high
        if ask > random_num:
            messagebox.showinfo(message="thats too high")
            # 8. Tell them it's too high
        # 9. Else if the guess is low
        else:
            messagebox.showinfo(message="thats too low")
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(message="you lost")
    window.mainloop()
