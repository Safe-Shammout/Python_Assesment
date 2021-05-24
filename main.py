from tkinter import *
from PIL import ImageTk, Image

#Componenet 1 (Game Starter Window object) will be constructed through following class
class GameStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="dark blue"# to set it as background color for all the label widgets
        #Background image on Frame
        self.bg_image = Image.open("game10.png") #need to use Image if need to resize 
        self.bg_image = self.bg_image.resize((750, 650), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image) 

        #widgets goes below  

        #image label below
        self.image_label= Label(parent, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the frame

        #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=350, y=475)
     
        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="lawn green", command=self.name_collection)
        self.continue_button.place(x=650, y=650)

         #cancel button
        self.cancel_button = Button(parent, text="Cancel", font=("Helvetica", "13", "bold"), bg="red")
        self.cancel_button.place(x=50, y=650) 


    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.image_label.destroy()
        self.entry_box.destroy()
        self.continue_button.destroy()
        self.cancel_button.destroy()

#Program runs below
if __name__ == "__main__":
    root = Tk()
    root.title("Game Name")
    root.geometry("800x800")
    game_starter_window = GameStarter(root) #instantiation, making an instance (object) of the class
    root.mainloop()#so the window doesnt dissapear