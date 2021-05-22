from tkinter import *
from PIL import ImageTk, Image

#Componenet 1 (Game Starter Window object) will be constructed through following class
class GameStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="dark blue"# to set it as background color for all the label widgets
        #Background image on Frame
        self.bg_image = Image.open("title.png") #need to use Image if need to resize 
        self.bg_image = self.bg_image.resize((750, 650), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image) 

        #widgets goes below
        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color)
        self.quiz_frame.grid()

        #image label below
        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the frame

        #label for spacing to fit image
        self.space=Label(self.quiz_frame, bg="black")
        self.space.grid(row=1,pady=50)

        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, column=2,padx=120, pady=200)
     
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="lawn green", command=self.name_collection)
        self.continue_button.grid(row=3, column=3,  padx=10, pady=10) 

         #cancel button
        self.cancel_button = Button(self.quiz_frame, text="Cancel", font=("Helvetica", "13", "bold"), bg="red", command=self.name_collection)
        self.cancel_button.grid(row=3,column=1,  padx=10, pady=10)        

        self.space=Label(self.quiz_frame)
        self.space.grid(row=10)

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