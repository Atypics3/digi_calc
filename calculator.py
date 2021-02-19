from tkinter import *
from tkinter import messagebox

#creating window function called into frame
class Window(Frame):
    #calculator won't work until the 2 underscores are in the function name
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        
#making result text on screen
        #background is , foreground is , height is 1 pixel tall, and width is 20 pixels wide
        self.resultField = Text(master, bg = '#FFFFFF', fg = '#000000',height = 15, width = 25)
        self.resultField.insert(INSERT, '0')
        self.resultField.grid(row = 0, columnspan = 4)

#making numbers and operation buttons
        b1 = Button(master, text = '1', command = lambda: self.notice(1))
        b2 = Button(master, text = '2', command = lambda: self.notice(2))
        b3 = Button(master, text = '3', command = lambda: self.notice(3))
        bplus = Button(master, text = '+', command = lambda: self.notice('+'))
        b4 = Button(master, text = '4', command = lambda: self.notice(4))
        b5 = Button(master, text = '5', command = lambda: self.notice(5))
        b6 = Button(master, text = '6', command = lambda: self.notice(6))
        bminus = Button(master, text = '-', command = lambda: self.notice('-'))
        b7 = Button(master, text = '7', command = lambda: self.notice(7))
        b8 = Button(master, text = '8', command = lambda: self.notice(8))
        b9 = Button(master, text = '9', command = lambda: self.notice(9))
        bmulti = Button(master, text = '*', command = lambda: self.notice('*'))
        b0 = Button(master, text = '0', command = lambda: self.notice(0))
        bleft = Button(master, text = '(', command = lambda: self.notice('('))
        bright = Button(master, text = ')', command = lambda: self.notice(')'))
        bdiv = Button(master, text = '/', command = lambda: self.notice('/'))
        
#aligning number and operations buttons
        b1.grid(row = 1, column = 0)
        b2.grid(row = 1, column = 1)
        b3.grid(row = 1, column = 2)
        bplus.grid(row = 1, column = 3)
        b4.grid(row = 2, column = 0)
        b5.grid(row = 2, column = 1)
        b6.grid(row = 2, column = 2)
        bminus.grid(row = 2, column = 3)
        b7.grid(row = 3, column = 0)
        b8.grid(row = 3, column = 1)
        b9.grid(row = 3, column = 2)
        bmulti.grid(row = 3, column = 3)
        b0.grid(row = 4, column = 0)
        bleft.grid(row = 4, column = 1)
        bright.grid(row = 4, column = 2)
        bdiv.grid(row = 4, column = 3)
        
#creating and alligning calculation/clear buttons
        bcalculate = Button(master, text = '=', command = self.displayRes)
        bclear = Button(master, text = 'Clear', command = self.clear)
        bcalculate.grid(row = 5, column = 0, columnspan = 2)
        bclear.grid(row = 5, column = 2, columnspan = 2)
        
    #defining notice function
    def notice(self, num):
        if self.resultField.get('0.0', END) == '0\n':
            self.resultField.delete('0.0', END)
        self.resultField.insert(INSERT, str(num))
        
    #defines clear function, deletes all text in textbox
    def clear(self):
        self.resultField.delete('0.0', END)
        self.resultField.insert(INSERT, '0')

    def displayRes(self):
        res = self.calculate(self.resultField.get('0.0', END)[:-1])
        self.resultField.delete('0.0', END)
        self.resultField.insert(INSERT, str(res))
        
    #defines calculation function
    def calculate(self, task):
        if task == 'ERROR':
            return 'ERROR'
        try:
            return(float(task))
        except ValueError:
            #checks for brackets
            if ')' in task:
                level = 0
                maxLevelStartIndex = 0
                maxLevelEndIndex = 0
                for i in range(0, len(task)):
                    if task(i) == '(':
                        level += 1
                        maxLevelStartIndex = i
                    if task(i) == ')':
                        level -= 1

                if level != 0:
                    messagebox.showerror('Error', 'ERROR, brackets dont match: %i layers too much in expression %s' %(level, task))
                    return 'Error'
                

                for i in range(maxLevelStartIndex, len(task)):
                    if task(i) == ')':
                        maxLevelEndIndex = i
                        break
                new_task = task[:maxLevelStartIndex] + str(self.calculate(task[maxLevelStartIndex + 1: maxLevelEndIndex])) + task[maxLevelEndIndex + 1:]
                return self.calculate(new_task)
            
            #if the calculation has addition:
            elif '+' in task:
                tesk = task.split('+')
                res = self.calculate(tesk[0])
                for t in tesk[1:]:
                    resk += self.calculate(t)
                return res
            
            #if the calculation has subtraction:
            elif '-' in task:
                tesk = task.split('-')
                res = self.calculate(tesk[0])
                for t in tesk[1:]:
                    res -= self.calculate(t)
                return res
            
            #if the calculation has multiplication
            elif '*' in task:
                tesk = task.split('*')
                res = self.calculate(tesk[0])
                for t in tesk[1:]:
                    res *= self.calculate(t)
                return res
            
            #if the calcuation has division
            elif '/' in task:
                tesk = task.split('/')
                res = self.calculate(tesk[0])
                for t in tesk[1:]:
                    try:
                        res /= self.calculate(t)
                    except ZeroDivisionError:
                        messagebox.showerror('Error', 'Error: division by 0')
                        return 'ERROR'
                return res
            else:
                messagebox.showerror('Error', 'Error: invalid expression')
                return 'Error'

#calls main loop           
root = Tk()
app = Window(root)
root.wm_title('Python Calculator')
root.mainloop()
