
from tkinter import *  #for GUI and widgets
from PIL import ImageTk, Image #for Images
from tkinter import messagebox  #for error messages (diagnose and recover)

#variables
names_list = [] #list to store names for leader board
#component 4: Dictionary collection of scenarios and options
scenario_options = {
        "s1" : "You went on a trip overseas with your friends and you have decided to go by ship. Everything was going well until the welcoming cheerful sun slowly faded away. The sky turned pitch black, the only light source other than the torch you and your friends now share is the flashes of lightning. The waves start to play around with your ship. It seems the sea has rejected you and any moment the ship will tip over.The compass stopped working and it seems that there is no way of communicating with the outside world. There is no reception. The ship has drifted off course and no one, not even the captain knows where you are. You are stuck in the middle of nowhere with no help from the outside world. Everyone is panicking and the captain is nowhere to be seen. No one knows how to steer the ship.",
        "s1_opt1" : "Stay on the ship.",
        "s1_opt2" :  """Use one of the lifeboats\n and abandon the ship.""",
        "s2" : "Now you and your friends have set off in the life boat, but it seems the situation has gotten worse, you have drifted too far off. You are in the middle of the sea with limited food and drinking water. The fierce sea does not seem to be calming down and veryone is just hoping that things can get better. All of a sudden an island has been spotted. Bursting with excitement and joy..." ,
        "s2_opt1" : "Go to the island.",
        "s2_opt2" : "The island looks too sketchy \n you think that there isnt a safe \n place to set shore, So wait.",

        "s3" : "scenario 3",
        "s3_opt1" : "scenario 3 option 1",
        "s3_opt2": "scenario 3 option 2",
        "s4_end" : "The waves get more violent than ever, fortunately you land on a island, but this island isnt the one youve seen before. Its a whole different island. Much smaller than the one you have seen before. U set camp until u realise this is your new home, with no contact to the outside world, with no idea as to where you are. You are the only habitants to this island. You have lived here for about 4 years, as long as u remember but you arent really sure, as days passed and you lost track\n you lose, GAME OVER",
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
        self.cancel_button = Button(parent, text="Cancel", font=("Helvetica", "13", "bold"), bg="red", command=self.cancel)
        self.cancel_button.place(x=50, y=550) 

    #method in class to collect the name entered by user, destry widgets and create a StoryWindow object
    def name_collection(self):
        name=self.entry_box.get()
        if name == "":
          messagebox.showerror("Name is required!","Please enter your name")
        elif len(name) >15: #toi make sure user inputs between 1-15 characters
            messagebox.showerror("limit error","please enter a name between 1 and 15 characters")
        else:
         names_list.append(name) #add name to names list declared at the beginning
         self.entry_box.destroy()
         self.continue_button.destroy()
         self.cancel_button.destroy()
         StoryWindow(root)

    #cancel method
    def cancel(self):
      root.destroy()

#Componenet 2 (Story wimdow object) will be constructed through following class
class StoryWindow:

  def __init__(self, parent):
  
      #Background image on Frame
      self.bg_img = Image.open("storm1y.png") #update my image file
      image = ImageTk.PhotoImage(self.bg_img) #update PhotoImage
      image_label.configure(image = image) #upadate the label
      image_label.image = image # keep a reference!        

      self.story_label = Message(parent, bg="slateblue" , text= scenario_options["s1"], bd=6, fg="white", font=("Helvetica", "13", "bold"))
      self.story_label.place(x=100, y=20, width=550, height=400)
      #option 1 Button
      self.option1_button = Button(parent, text= scenario_options["s1_opt1"], font=("Helvetica", "13", "bold"), bg="slateblue",  wraplength= 0,
      command=self.option1)
      self.option1_button.place(x=30, y=500, width=320, height=100)
      #option 2 Button
      self.option2_button = Button(parent, text=scenario_options["s1_opt2"], font=("Helvetica", "13", "bold"), bg="slateblue",
        command=self.option2)
      self.option2_button.place(x=415, y=500, width=320, height=100)
      #index to keep track where the player is in the story
      self.index=1

  def option1 (self): 
      #using or operator is more efficient than repeating conditions
      if (self.index == 1 or self.index == 2):
        self.story_label.config(text=scenario_options["s3"])
        self.option1_button.config(text=scenario_options["s3_opt1"])
        self.option2_button.config(text=scenario_options["s3_opt2"])
        self.index=3
      else:
        self.story_label.config(text=scenario_options["s6_end"])
        self.option1_button.destroy()
        self.option2_button.destroy()
        #self.leader_board_button = Button(parent, text="Leader Board")
     # elif index ==2 :
       # self.story_label.config(text=scenario_options["s3"])
        #self.option1_button.config(text=scenario_options["s3_opt1"])
       # self.option2_button.config(text=scenario_options["s3_opt2"])
        #index=3

  #option 2 button method
  def option2 (self):
        if self.index ==1 :
          self.story_label.config(text=scenario_options["s2"])
          self.option1_button.config(text=scenario_options["s2_opt1"])
          self.option2_button.config(text=scenario_options["s2_opt2"])
          self.index=2
        elif self.index ==2 :
          self.story_label.config(text=scenario_options["s4_end"])
          self.option1_button.destroy()
          self.option2_button.destroy()
          #self.leader_board_button = Button(parent, text="Leader Board")
        else :
          self.story_label.config(text=scenario_options["s5_end"])
          self.option1_button.destroy()
          self.option2_button.destroy()
         # self.leader_board_button = Button(parent, text="Leader Board")
        
            
  def leaderboard_collection (self):
      self.option1_button.destroy()
      self.option2_button.destroy()
      self.story_label.destroy()
      LeaderboardWindow(root)
#TO HERE

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





