#Story line game
#Safe Shammout 2021

from tkinter import *  # for GUI and widgets
from PIL import ImageTk, Image  # for Images
from tkinter import messagebox  # for error messages (diagnose and recover)

# variables

names_list = []  # list to store names for leader board


# Componenet 1 (Game Starter Window object) will be constructed through following class

class GameStarter:

    def __init__(self, parent):  # constructor, The __init__() function is called automatically every time the class is being used to create a new object.

        background_color = 'dark blue'  # to set it as background color for all the label widgets

        # entry box

        self.entry_box = Entry(parent)
        self.entry_box.place(x=350, y=400)

        # continue button

        self.continue_button = Button(parent, text='Continue',
                font=('Helvetica', '13', 'bold'), bg='lawn green',
                command=self.name_collection)
        self.continue_button.place(x=550, y=550)

         # cancel button

        self.cancel_button = Button(parent, text='Cancel',
                                    font=('Helvetica', '13', 'bold'),
                                    bg='red', command=self.cancel)
        self.cancel_button.place(x=50, y=550)

    # method in class to collect the name entered by user, destry widgets and create a StoryWindow object

    def name_collection(self):
        name = self.entry_box.get()
        if name == '':
            messagebox.showerror('Name is required!',
                                 'Please enter your name')
        elif len(name) > 15:

                            # toi make sure user inputs between 1-15 characters

            messagebox.showerror('limit error',
                                 'please enter a name between 1 and 15 characters'
                                 )
        elif name.isnumeric():
            messagebox.showerror('Name error',
                                 'Name can only consist of letters'
                                 )
        elif  not name.isalpha():
                messagebox.showerror('test',
                'name cant consist of symbols')
        else:
            names_list.append(name)  # add name to names list declared at the beginning
            self.entry_box.destroy()
            self.continue_button.destroy()
            self.cancel_button.destroy()
            StoryWindow(root)

    # cancel method

    def cancel(self):
        root.destroy()


# Componenet 2 (Story wimdow object) will be constructed through following class

class StoryWindow:
  
    def __init__(self, parent):

          # component 4: Dictionary collection of scenarios and options
          
          self.scenario_options = {
              's1': 'You went on a trip overseas with your friends and you have decided to go by ship. Everything was going well until the welcoming cheerful sun slowly faded away. The sky turned pitch black, the only light source other than the torch you and your friends now share is the flashes of the lightning. The waves start to play around with your ship. It seems the sea has rejected you and any moment the ship will top over. The compass stopped working and it seems that there is no way of communicating with the outside world.there is no reception. The ship has drifted off course and no one, not even the captain knows where you are. You are stuck in the middle of nowhere with no help from the outside world. Everyone is panicking and the captain is nowhere to be seen.....',
              's1_opt1': 'Stay on the ship.',
              's1_opt2': """Use one of the lifeboats\n and abandon the ship.""",
              's2': 'Now you and your friends have set off in the life boat, but it seems the situation has gotten worse, you have drifted too far off. You are in the middle of the sea with limited food and drinking water. The fierce sea does not seem to be calming down and everyone is just hoping that things can get better. All of a sudden an island has been spotted.',
              's2_opt1': 'Go to the island.',
              's2_opt2': '''The island looks too sketchy 
          you think that there isnt a safe 
          place to set shore, So wait.''',
              's3': "With the waves tossing you around randomly you hit the jackpot and land on an island. You have no idea how you got here but you're thankful. After setting ashore you are greeted by a creature that you have never seen before..It is so hairy that you can't tell the front of its head from the back, and it speaks human language, English. You are really shocked, amazed and mostly petrified by what you're seeing, doubting your own consciousness, have you lost it? \n The creature tells you that it can help you out.",
              's3_opt1': 'Trust the creature',
              's3_opt2': '''This creature is freaky as hell
          and this is so suspicious,
          go back to the ship and 
          sail away immediately''',
              's4_end': "The waves get more violent than ever, fortunately you land on an island, but this island is not the one you've seen before. Its a whole different island. Much smaller than the one you have seen before. You set up a camp until you realise this is your new home, with no contact to the outside world, with no idea as to where you are. You are the only habitants to this island. You have lived here for about 4 years, as long as you remember but you are not really sure, as days passed and you lost track\n you lose, GAME OVER",
              's5_end': 'After setting sail and running away from that creature you are now lost in the ocean, back to square 1. Luckily out of nowhere the storm suddenly ends. The rescue team that has been sent out has finally found you',
              's6_end': 'The creature explains to you the situation, gives you food supplies and also gives you a whole new ship. It turned out to be a really friendly creature. It helped you set sail and you arrive safely to your original destination',
              }

        # Background image on Frame

          self.bg_img = Image.open('storm1y.png')  # update my image file
          image = ImageTk.PhotoImage(self.bg_img)  # update PhotoImage
          image_label.configure(image=image)  # upadate the label
          image_label.image = image  # keep a reference!

          self.story_label = Message(
              parent,
              bg='MediumPurple4',
              text=self.scenario_options['s1'],
              bd=6,
              fg='white',
              font=('Helvetica', '13', 'bold'),
              )
          self.story_label.place(x=100, y=20, width=570, height=400)

        # option 1 Button

          self.option1_button = Button(
              parent,
              text=self.scenario_options['s1_opt1'],
              font=('Helvetica', '13', 'bold'),
              bg='white',
              activebackground='RoyalBlue3',
              wraplength=0,
              command=self.option1,
              )
          self.option1_button.place(x=30, y=500, width=320, height=100)

        # option 2 Button

          self.option2_button = Button(
              parent,
              text=self.scenario_options['s1_opt2'],
              font=('Helvetica', '13', 'bold'),
              bg='white',
              activebackground='RoyalBlue3',
              command=self.option2,
              )
          self.option2_button.place(x=415, y=500, width=320, height=100)

        # exit button to take to LeaderboardWindow

          self.leader_board_button = Button(parent, text='Exit',
                  font=('Helvetica', '13', 'bold'), bg='red',
                  command=self.leaderboard_collection)
          self.leader_board_button.place(x=355, y=620)

        # index to keep track where the player is in the story

          self.index = 1

        # points was coming with error in leaderboard method that its referenced without assignment
        # adding it here in the constructor solved the issue

          self.points = 0

    def option1(self):

      # using or operator is more efficient than repeating conditions

        if self.index == 1 or self.index == 2:
            self.story_label.config(text=self.scenario_options['s3'])
            self.option1_button.config(text=self.scenario_options['s3_opt1'])
            self.option2_button.config(text=self.scenario_options['s3_opt2'])
            if self.index == 1:
                self.points += 400
            else:
                self.points += 75
            self.index = 3
        else:
            self.points += 150
            self.story_label.config(text=self.scenario_options['s6_end'])
            print (self.points)
            self.option1_button.destroy()
            self.option2_button.destroy()

        # self.leader_board_button = Button(parent, text="Leader Board", command=self.leaderboard_collection)
     # elif index ==2 :
       # self.story_label.config(text=scenario_options["s3"])
        # self.option1_button.config(text=scenario_options["s3_opt1"])
       # self.option2_button.config(text=scenario_options["s3_opt2"])
        # index=3

  # option 2 button method

    def option2(self):
        if self.index == 1:
            self.points += 250
            self.story_label.config(text=self.scenario_options['s2'])
            self.option1_button.config(text=self.scenario_options['s2_opt1'])
            self.option2_button.config(text=self.scenario_options['s2_opt2'])
            self.index = 2
        elif self.index == 2:
            self.points += -250
            self.story_label.config(text=self.scenario_options['s4_end'])
            self.option1_button.destroy()
            self.option2_button.destroy()
        else:

         # self.leader_board_button = Button(parent, text="Leader Board", command=self.leaderboard_collection)

            self.points += 100
            self.story_label.config(text=self.scenario_options['s5_end'])
            self.option1_button.destroy()
            self.option2_button.destroy()

          # self.leader_board_button = Button(parent, text="Leader Board", command=self.leaderboard_collection)

    def leaderboard_collection(self):
        self.option1_button.destroy()
        self.option2_button.destroy()
        self.story_label.destroy()
        self.leader_board_button.destroy()

      # save information to a file

        name = names_list[0]
        file = open('leader_board.txt', 'a')  # open file or create if its first time in append mode
        if name == 'safe_erase':
            file = open('leader_board.txt', 'w')  # this clears the data in file
        else:
            file.write(str(self.points))  # turn into string as will be displayed as text in a label
            file.write(' - ')
            file.write(name + '\n')
            file.close()

      # To dispolay name and score in seperate labels

        leaders = LeaderboardWindow(root)  # create an instance of LeaderboardWindow so we can edit its labels
        input_file = open('leader_board.txt', 'r')  # open in read mode
        line_list = input_file.readlines()  # read the lines in text file
        line_list.sort()  # sort them score is first so according to score
        print(line_list)  # test sorting working
        top = []  # list to store only top 5
        leader_list = line_list[-5:]  # take last 5 index in list (as want highest)
        print(leader_list)  # testing the last 5 is working
        for line in leader_list:
            points = line.split(' - ')
            top.append((int(points[0]), points[1]))  # this is a list containing tuples (top)
        file.close()
        top.sort()
        top.reverse()
        print(top)  # for testing (list is sorted after testing so good)
        for i in range(len(top)):
            leaders.name_lbl.config(text=top[0][1])  # leaders is the object from leaderboardWindow class
            leaders.score_lbl.config(text=top[0][0])
            leaders.name2_lbl.config(text=top[1][1])
            leaders.score2_lbl.config(text=top[1][0])
            leaders.name3_lbl.config(text=top[2][1])
            leaders.score3_lbl.config(text=top[2][0])
            leaders.name4_lbl.config(text=top[3][1])
            leaders.score4_lbl.config(text=top[3][0])
            leaders.name5_lbl.config(text=top[4][1])
            leaders.score5_lbl.config(text=top[4][0])


# component 3: leader board

class LeaderboardWindow:

    def __init__(self, parent):

    # Background image on Frame

        parent.geometry('550x650')
        self.bg_img = Image.open('Lb4.png')  # update my image file
        self.bg_img = self.bg_img.resize((550, 650), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(self.bg_img)  # update PhotoImage
        image_label.configure(image=image)  # upadate the label
        image_label.image = image  # keep a reference!

        self.name_lbl = Label(parent, text='name', font=('Helvetica',
                              '13', 'bold'), height=3, width=15)
        self.name_lbl.place(x=50, y=100)

      # option 2 Button

        self.score_lbl = Label(parent, text='score', font=('Helvetica',
                               '13', 'bold'), height=3, width=15)
        self.score_lbl.place(x=300, y=100)

        self.name2_lbl = Label(parent, text='name2', font=('Helvetica',
                               '13', 'bold'), height=3, width=15)
        self.name2_lbl.place(x=50, y=200)

      # option 2 Button

        self.score2_lbl = Label(parent, text='score2', font=('Helvetica'
                                , '13', 'bold'), height=3, width=15)
        self.score2_lbl.place(x=300, y=200)

        self.name3_lbl = Label(parent, text='name3', font=('Helvetica',
                               '13', 'bold'), height=3, width=15)
        self.name3_lbl.place(x=50, y=300)

      # option 2 Button

        self.score3_lbl = Label(parent, text='score3', font=('Helvetica'
                                , '13', 'bold'), height=3, width=15)
        self.score3_lbl.place(x=300, y=300)

        self.name4_lbl = Label(parent, text='name4', font=('Helvetica',
                               '13', 'bold'), height=3, width=15)
        self.name4_lbl.place(x=50, y=400)

      # option 2 Button

        self.score4_lbl = Label(parent, text='score4', font=('Helvetica'
                                , '13', 'bold'), height=3, width=15)
        self.score4_lbl.place(x=300, y=400)

        self.name5_lbl = Label(parent, text='name5', font=('Helvetica',
                               '13', 'bold'), height=3, width=15)
        self.name5_lbl.place(x=50, y=400)

      # option 2 Button

        self.score5_lbl = Label(parent, text='score5', font=('Helvetica'
                                , '13', 'bold'), height=3, width=15)
        self.score5_lbl.place(x=300, y=400)


# Program runs below

if __name__ == '__main__':
    root = Tk()
    root.title('Lost in Time')
    root.geometry('750x650')
    bg_image = Image.open('game10.png')  # need to use Image if need to resize
    bg_image = bg_image.resize((750, 650), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)

   # image label below

    image_label = Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the fram
    game_starter_window = GameStarter(root)  # instantiation, making an instance (object) of the class
    root.mainloop()  # so the window doesnt dissapear
