from tkinter import *


#Componenet 1 (Game Starter Window object) will be constructed through following class
class GameStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="dark blue"# to set it as background color for all the label widgets

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Game Name", font=("Tw Cen MT","18","bold"),bg=background_color)
        self.heading_label.grid(row=0, column=2, padx=20) 
    
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.grid(row=1, column=2, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, column=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="lawn green", command=self.name_collection)
        self.continue_button.grid(row=3, column=3,  padx=20, pady=20) 

         #cancel button
        self.cancel_button = Button(self.quiz_frame, text="Cancel", font=("Helvetica", "13", "bold"), bg="red", command=self.name_collection)
        self.cancel_button.grid(row=3,column=1,  padx=10, pady=10)        


    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.quiz_frame.destroy()
    



#Program runs below
if __name__ == "__main__":
    root = Tk()
    root.title("Game Name")
    game_starter_window = GameStarter(root) #instantiation, making an instance (object) of the class
    root.mainloop()#so the window doesnt dissapear