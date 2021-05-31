
from tkinter import *
from PIL import ImageTk, Image


#variables
names_list = []


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
        self.image_label = Label(parent, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the frame

        #entry box
        self.entry_box = Entry(parent)
        self.entry_box.place(x=350, y=400)
     
        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="lawn green", command=self.name_collection)
        self.continue_button.place(x=550, y=550)

         #cancel button
        self.cancel_button = Button(parent, text="Cancel", font=("Helvetica", "13", "bold"), bg="red")
        self.cancel_button.place(x=50, y=550) 


    def name_collection(self):
        name=self.entry_box.get()
        names_list.append(name) #add name to names list declared at the beginning
        self.image_label.destroy()
        self.entry_box.destroy()
        self.continue_button.destroy()
        self.cancel_button.destroy()
        StoryWindow(root)

#Componenet 2 (Story wimdow object) will be constructed through following class



class StoryWindow:
  def __init__(self, parent):

    background_color = "blue"
  
    #frame to place widgets on
    self.story_frame = Frame (parent, bg = background_color)
    self.story_frame.grid()

#Background image on Frame
    self.bg_image = Image.open("storm.png") #need to use Image if need to resize 
    self.bg_image = self.bg_image.resize((650, 550), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image) 


    self.bg_image = Label(self.story_frame, image=self.bg_image)
    self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)


    self.story1_label = Label( self.story_frame, text="Testing how long the story can be I wan to write a lot to see if a label can handle too much writing,\n \n\n so if my story is big, like few lines big, it will show or not on the frame?????\n\n\n")
    self.story1_label.grid(row=1, padx=50, pady=50)



#option 1 Button
    self.option1_button = Button(parent, text="option 1", font=("Helvetica", "13", "bold"), bg="purple3")
    self.option1_button.place(x=30, y=400, width=300, height=200)

#option 2 Button
    self.option2_button = Button(parent, text="option 2", font=("Helvetica", "13", "bold"), bg="purple3")
    self.option2_button.place(x=415, y=400, width=300, height=200)

     




#Program runs below
if __name__ == "__main__":
   root = Tk()
   root.title("Game Name")
   root.geometry("750x650")
   game_starter_window = GameStarter(root) #instantiation, making an instance (object) of the class
   root.mainloop()#so the window doesnt dissapear





