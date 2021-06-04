
from tkinter import *
from PIL import ImageTk, Image


#variables
names_list = []
#component 4: Dictionary collection of scenarios and options
scenario_options = {
        "s1" : "scenario 1",
        "s1_opt1" : "scenario 1 option 1",
        "s1_opt2" : "scenario 1 option 2",
        "s2" : "scenario 2",
        "s2_opt1" : "scenario 2 option 1",
        "s2_opt2" : "scenario 2 option 2",
        "s3" : "scenario 3",
        "s3_opt1" : "scenario 3 option 1",
        "s3_opt2": "scenario 3 option 2",
        "s4_end" : "scenario 4 end",
        "s5_end" : "scenario 5 end",
        "s6_end" : "scenario 6 end",
      }
    

#Componenet 1 (Game Starter Window object) will be constructed through following class
class GameStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="dark blue"# to set it as background color for all the label widgets
        #Background image 

        #entry box
        self.entry_box = Entry(parent)
        self.entry_box.place(x=350, y=400)
     
        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="lawn green", command=self.name_collection)
        self.continue_button.place(x=550, y=550)

         #cancel button
        self.cancel_button = Button(parent, text="Cancel", font=("Helvetica", "13", "bold"), bg="red")
        self.cancel_button.place(x=50, y=550) 

    #method in class to collect the name entered by user, destry widgets and create a StoryWindow object
    def name_collection(self):
        name=self.entry_box.get()
        names_list.append(name) #add name to names list declared at the beginning
        self.entry_box.destroy()
        self.continue_button.destroy()
        self.cancel_button.destroy()
        StoryWindow(root)

#Componenet 2 (Story wimdow object) will be constructed through following class
class StoryWindow:
  def __init__(self, parent):
      
      #Background image on Frame
      self.bg_img = Image.open("storm1y.png") #update my image file
      image = ImageTk.PhotoImage(self.bg_img) #update PhotoImage
      image_label.configure(image = image) #upadate the label
      image_label.image = image # keep a reference!        

      self.story_label = Label(parent, bg="purple3" , text= scenario_options["s1"])
      self.story_label.place(x=50, y=50)
      #option 1 Button
      self.option1_button = Button(parent, text="option 1", font=("Helvetica", "13", "bold"), bg="purple3",
      command=self.option1)
      self.option1_button.place(x=30, y=400, width=300, height=200)
      #option 2 Button
      self.option2_button = Button(parent, text="option 2", font=("Helvetica", "13", "bold"), bg="purple3",
        command=self.leaderboard_collection)
      self.option2_button.place(x=415, y=400, width=300, height=200)

  def option1 (self):
      #index to keep track where the player is in the story
      index = 1

      if index ==1 :
        self.story_label.config(text=scenario_options["s3"])
        self.option1_button.config(text=scenario_options["s3_opt1"])
        self.option2_button.config(text=scenario_options["s3_opt2"])
        index=3
      elif index ==2 :
        self.story_label.config(text=scenario_options["s3"])
        self.option1_button.config(text=scenario_options["s3_opt1"])
        self.option2_button.config(text=scenario_options["s3_opt2"])
        index=3
      elif index ==3 :
        self.story_label.config(text=scenario_options["s6_end"])
        self.option1_button.destroy()
        self.option2_button.destroy()
        self.leader_board_button = Button(parent, text="Leader Board")
        

            
  def leaderboard_collection (self):
      self.option1_button.destroy()
      self.option2_button.destroy()
      self.story_label.destroy()
      LeaderboardWindow(root)


#component 3: leader board 
class LeaderboardWindow:
  def __init__(self, parent):

    #Background image on Frame
    parent.geometry("550x650")
    self.bg_img = Image.open("Lb4.png") #update my image file
    self.bg_img = self.bg_img.resize((550, 650), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(self.bg_img) #update PhotoImage
    image_label.configure(image = image) #upadate the label
    image_label.image = image # keep a reference!     

     




#Program runs below
if __name__ == "__main__":
   root = Tk()
   root.title("Game Name")
   root.geometry("750x650")
   bg_image = Image.open("game10.png") #need to use Image if need to resize 
   bg_image = bg_image.resize((750, 650), Image.ANTIALIAS)
   bg_image = ImageTk.PhotoImage(bg_image) 
   #image label below
   image_label = Label(root, image=bg_image)
   image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the fram
   game_starter_window = GameStarter(root) #instantiation, making an instance (object) of the class
   root.mainloop()#so the window doesnt dissapear





