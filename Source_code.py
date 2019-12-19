from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import os
import pygame

from pygame import  mixer


root = Tk()

#menu bar
menubar = Menu(root)
root.config(menu = menubar)

#submenu
submenu = Menu(menubar , tearoff=0)


menubar.add_cascade(label = "File",menu = submenu)

submenu.add_command(label = "Exit",command = root.destroy)

def about_us():
    tkinter.messagebox.showinfo('music player','this is a music player developed by tk!!')
submenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label = "Help",menu = submenu)
submenu.add_command(label = "About us", command = about_us)



mixer.init()

#root.geometry('750x750')
root.title("ganna")
root.iconbitmap(r'music.ico')

text = Label (root,text =  'click your favourite artist and listen to there hits!!')
text.pack(pady=20)








def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "music paused"

def play_music():

        try:
            paused
        except NameError:
            print("hey !! is this works")
            #statusbar['text'] = "playing music" +  ' - - ' + pygame.mixer.music.get_pos()


        else:
            mixer.music.unpause()
            statusbar['text'] = "music resumes!!"
def ani_music():
    c = queue()
    c.enq('01 - uturn.mp3')

    c.enq('02 - Aaluma-Doluma.mp3')

    c.enq('03 - Ethir Neechal.mp3')

    c.enq('04 - Chennai City Gangsta.mp3')

    c.enq('05 - Kanave Kanave.mp3')

    c.call()

def sid_music():
    s = queue()
    s.enq('01 - emai.mp3')

    s.enq('02 - inkem.mp3')

    s.enq('03 - Kannaana-Kanney.mp3')

    s.enq('04 - Thalli.mp3')

    s.enq('05 - Maate Vinadhuga.mp3')

    s.call()



def hip_music():
    h = queue()
    h.enq('01 - happynewyear.mp3')

    h.enq('02 - aathadi.mp3')

    h.enq('03 - meesaya murukku.mp3')

    h.enq('04 - neeyum.mp3')

    h.enq('05 - azhage.mp3')

    h.call()


def next_music():
    n = queue()

    n.next()





def set_vol(val):
    volume=int(val) /100
    mixer.music.set_volume(volume)


def rewind_music():
    pygame.mixer.music.rewind()
    statusbar['text'] = "music rewind!!"

def replay_music():
    pygame.mixer.music.play(-1)
    statusbar['text'] = "music replay!!"

class queue:
    def __init__(self):
        self.queue=[]
        self.limit=5
        self.x=0
    def enq(self,data):
        if (len(self.queue)==self.limit):
            print("queue overflow")
        else:
            self.queue.append(data)


    def call(self):
        print(self.queue)


        def music():
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.queue[self.x])
            pygame.mixer.music.play(0)
            statusbar['text'] = "playing music" + ' - - ' + self.queue[0]
            print('1')
            que()

        def que():
            pos = pygame.mixer.music.get_pos()
            if int(pos) == -1:
                self.x = self.x+1
                pygame.mixer.music.load(self.queue[self.x])
                pygame.mixer.music.play(0)
                print('2')
                statusbar['text'] = "playing music" + ' - - ' + self.queue[self.x]

            root.after(1, que)

        music()


    def deq(self):
        if (len(self.queue)==0):
            print("queue underflow")
        else:

            self.queue.pop(0)
    def next(self):
        pygame.mixer.music.stop()
        def que():

            pos = pygame.mixer.music.get_pos()
            if int(pos) == -1:
                self.x = self.x+1
                pygame.mixer.music.load(self.queue[self.x])
                pygame.mixer.music.play(0)
                print('2')
                #text = Label(root, text=self.queue[self.x])
                #text.pack(pady=20)
                statusbar['text'] = "playing music" + ' - - ' + self.queue[self.x]

            root.after(1, que)

        que()


    #def display(self):
        #for i in range(0,5):
            #texta = Label (root,text = self.queue[i])
            #texta.pack(side=TOP)
            #print(self.queue[i])








middleframe = Frame(root)
middleframe.pack(padx=20,pady=20)


aniphoto = PhotoImage(file='anirudh.png' )
anibtn = Button(middleframe, image=aniphoto, command=ani_music)
anibtn.pack(side=LEFT,padx=20)

sidphoto = PhotoImage(file='sidd.png' )
sidbtn = Button(middleframe, image=sidphoto, command=sid_music)
sidbtn.pack(side=LEFT,padx=20)

hipphoto = PhotoImage(file='hip.png' )
hipbtn = Button(middleframe, image=hipphoto, command=hip_music)
hipbtn.pack(side=LEFT,padx=20)




nextphoto = PhotoImage(file='next.png')
nextbtn = Button(middleframe, image=nextphoto,command=next_music)
nextbtn.pack(side=RIGHT,padx=20)

playphoto = PhotoImage(file='play.png')
playbtn = Button(middleframe, image=playphoto,command=play_music)
playbtn.pack(side=RIGHT,padx=20)

pausephoto = PhotoImage(file='pause.png')
pausebtn = Button(middleframe, image=pausephoto,command = pause_music)
pausebtn.pack(side= RIGHT,padx=20)

rewindphoto = PhotoImage(file='rewind.png')
rewindbtn = Button(middleframe, image=rewindphoto,command = rewind_music)
rewindbtn.pack(side= RIGHT,padx=20)

replayphoto = PhotoImage(file='replay.png')
replaybtn = Button(middleframe, image=replayphoto,command = replay_music)
replaybtn.pack(side= RIGHT,padx=20)

scale = Scale(root,from_=0,to=100, orient =HORIZONTAL , command= set_vol)
scale.set(75)
mixer.music.set_volume(0.7)
scale.pack(pady=20)

statusbar = Label(root,text = "Welcome to Ganna ..",relief = SUNKEN, anchor =W)
statusbar.pack(side = BOTTOM, fill = X)




root.mainloop()
