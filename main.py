from tkinter import *


# creating a calculator class
class Calculator:

    # constructor, called when a object is created and is initialized by the class's attributes
    # i.e) title in main.title
    def __init__(self, main):

        self.main = main  # assigns a reference (main) to app's main window

        main.title("A Digital Calculator")  # sets a title

        self.eq = Entry(main, width=50, borderwidth=6)  # creates a line where we display a equation

        self.eq.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # assigns a pos. for equation line in app

        # executes the createButton() method
        self.createButton()

    # another method that creates the buttons for the calculator
    def createButton(self):
        # creating a button one by one with their respective value using addButton()
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('C')
        b_equal = self.addButton('=')

        # arranging the buttons into a orderly list (just like a actual calculator)
        row_1 = [b7, b8, b9, b_add]
        row_2 = [b4, b5, b6, b_sub]
        row_3 = [b1, b2, b3, b_mult]
        row_4 = [b_clear, b0, b_equal, b_div]

        # assigning each button to a specific position on the GUI
        r = 1;  # counter for counting rows (where one row already exists for display purposes)
        # for rows 1-4...
        for row in [row_1, row_2, row_3, row_4]:
            c = 0  # counter for counting columns
            for button in row:  # for each button in a row...
                button.grid(row=r, column=c, columnspan=1)  # populates the row/column with a button
                c += 1  # increments for each iteration
            r += 1  # also increments for each iteration

    # creates and returns a tkinter button object used for the GUI
    def addButton(self, value):
        # creates a button in the Calculator class,
        # with the value (as text) displayed on the button,
        # and its width being 9 pixels wide.
        # GUI now knows what value goes with each button when it's clicked
        return Button(self.main, text=value, width=9, command=lambda: self.clickButton(str(value)))

    # programs the actions that'll be performed in the calculator after a button click
    def clickButton(self, value):
        curr_eq = str(self.eq.get())  # gets the content from the equation line and stores it in a string

        if value == 'C':  # if "C" is clicked, then the screen is cleared
            self.eq.delete(-1, END)

        elif value == '=':  # if the user didn't click it,
            # and if the user clicked "=", then compute the answer and display it
            ans = str(eval(curr_eq))  # evaluates and stores into a ans(wer) variable
            self.eq.delete(-1, END)  # delete whatever's in the equation line
            self.eq.insert(0, ans)  # inserts the answer into equation line

        else:  # if user clicked any other button (0-9, + -, etc.), then add it to the equation line
            self.eq.delete(0, END)
            self.eq.insert(0, curr_eq + value)


# when executed, creates the calculator window and makes the calculator function right
if __name__ == '__main__':  # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    root = Tk()  # creating our main window

    my_gui = Calculator(root)  # basically creates a GUI by telling Calculator() to use root

    root.mainloop()  # tells the app to wait for user interaction and updates the app accordingly
