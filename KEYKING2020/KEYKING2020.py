import string
import random
from tkinter import *
from PIL import ImageTk,Image




root = Tk()

#--- IMAGE DECLARING
logo_image = ImageTk.PhotoImage(Image.open("E:\Python\SublimeText\KeyKing2020Files\KeyKingMain\KeyRingBanner1.png"))
lock_image = ImageTk.PhotoImage(Image.open("E:\Python\SublimeText\KeyKing2020Files\KeyKingMain\CrownLockal.png"))
RG_image = ImageTk.PhotoImage(Image.open("E:\Python\SublimeText\KeyKing2020Files\KeyKingMain\RGLOGOBLUE1024.png"))


#ESTABLIST MAIN WINDOW
root.title('KEYKING2020')
root.iconbitmap('E:\Python\SublimeText\KeyKing2020Files\KeyKingMain\darkcrown.ico')
width_of_window = 800
height_of_window = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width/2)- (width_of_window/2))
y_coordinate = int((screen_height/2)- (height_of_window/2))

root.geometry(f'{width_of_window}x{height_of_window}+{x_coordinate}+{y_coordinate}')
root.resizable(width=False,height=False)
#==============================================================================
#CREATE NEW INNER WINDOW
class WindowChange(Frame):
	def __init__(self,the_window):
		super().__init__()
		self["height"]=500
		self["width"]=800
		self["bg"]='grey22'
		self["borderwidth"]=5

def generate_password():
	global generated_label
	inner_login_box.place_forget()
	generated_box.place(x=48,y=56)


	quant = int(length_entry.get())
	lowlist = [item for item in string.ascii_lowercase]
	upplist = [item for item in string.ascii_uppercase]
	numlist = [item for item in string.digits]
	spezlist = [item for item in string.punctuation]
	selection_list = []

	if lowvar.get()==1:
		for item in lowlist:
			selection_list.append(item)
	if uppvar.get()==1:
		for item in upplist:
			selection_list.append(item)
	if numvar.get()==1:
		for item in numlist:
			selection_list.append(item)
	if specvar.get()==1:
		for item in spezlist:
			selection_list.append(item)

	password = ''.join([random.choice(selection_list) for item in range(quant)])
	
	last_label = Label(generated_box,text='Your Randomly Selected Password Is:',font='Arial 26',bg='grey33',fg='white')
	last_label.place(x=50,y=50)

	generated_label = Label(generated_box,text=password,font='Arial 28 bold',bg='grey33',fg='light blue')
	generated_label.place(relx=.5,rely=.5,anchor="center")

	home_button = Button(generated_box,text='Create New',font='Arial 12 bold',width=10,height=2,bg='grey55',fg='white',command=go_home)
	home_button.place(relx=.42,rely=.80)

def go_home():
	global generated_label
	generated_label.place_forget()
	length_entry.delete(0,'end')
	lowercase_letters.deselect()
	uppercase_letters.deselect()
	numbers_chars.deselect()
	special_chars.deselect()
	generated_box.place_forget()
	inner_login_box.place(x=48,y=56)


#OUTER LAYER
login_screen = WindowChange(root)
login_screen.pack()

kking_banner = Label(login_screen,image=logo_image,relief='raised',bg='grey44')
kking_banner.place(x=75,y=0)

RG_logo = Label(login_screen,image=RG_image,bg='grey22')
RG_logo.place(relx=0,rely=.94)

#--------------------------------------------------------------------------
#INNER LOGIN CONTAINER
inner_login_box = Frame(login_screen,height=400,width=700,bg='grey33',relief='groove',borderwidth=12)
inner_login_box.place(x=48,y=56)

lock_Label = Label(inner_login_box,image=lock_image,bg='grey33')
lock_Label.place(x=415,y=60)

paramaters_label = Label(inner_login_box,text='PASSWORD GENERATE OPTIONS',borderwidth=1,relief='solid',font="Arial 16 bold",bg='grey33',fg='white')
paramaters_label.place(x=35,y=60)

character_length_label = Label(inner_login_box,text='ENTER DESIRED CHARACTER LENGTH',font='Arial 12 bold',bg='grey33',fg='black')
character_length_label.place(x=48,y=110)

length_entry = Entry(inner_login_box,width=5)
length_entry.place(x=185,y=140)

lowvar = IntVar()
lowercase_letters = Checkbutton(inner_login_box,text='abcd....',font="Arial 12 bold",bg='grey33',variable=lowvar)
lowercase_letters.place(x=100,y=180)

uppvar = IntVar()
uppercase_letters = Checkbutton(inner_login_box,text='ABCD....',font="Arial 12 bold",bg='grey33',variable=uppvar)
uppercase_letters.place(x=220,y=180)

numvar = IntVar()
numbers_chars = Checkbutton(inner_login_box,text='1234....',font="Arial 12 bold",bg='grey33',variable=numvar)
numbers_chars.place(x=100,y=230)

specvar=IntVar()
special_chars = Checkbutton(inner_login_box,text='!@$%`...',font="Arial 12 bold",bg='grey33',variable=specvar)
special_chars.place(x=220,y=230)

generate_button = Button(inner_login_box,text='GENERATE PASSWORD',font='Arial 18 bold',fg='navy blue',borderwidth=5,relief='raised',command=generate_password)
generate_button.place(x=55,y=280)


#----------------------------------------------------------------------------
#FUNCTION FOR GATHERING PASSWORD PARAMETERS
# -----------------------------------------------------------------------------

generated_box = Frame(login_screen,height=400,width=700,bg='grey33',relief='groove',borderwidth=12)


root.mainloop()


#-------------DROP DOWN MENU BASE------------------------------
# main_menu = Menu(login_screen)
# root.config(menu=main_menu)
# subMenu = Menu(main_menu)
# main_menu.add_cascade(label="File")
# subMenu.add_command(label="New Project..")
# subMenu.add_command(label="New..")
# subMenu.add_separator()
# subMenu.add_command(label='Exit')

#-------------FILE PATH UI------------------
# file_loc = Label(inner_login_box,text='File Path',borderwidth=4,width=8,relief='raised',font='Arial 12',bg='grey22',fg='gold')
# file_loc.place(x=44,y=95)
# path_entry = Entry(inner_login_box,width=40)
# path_entry.place(x=130,y=98)

#----PASSWORD ENTRY UI------------------------
# pw_box = Label(inner_login_box,text='Password',borderwidth=4,relief='raised',font='Arial 12',bg='grey22',fg='gold')
# pw_box.place(x=45,y=55)
# password_entry = Entry(inner_login_box,width=40)
# password_entry.place(x=130,y=60)

# ATTEMPTED CHARACTER SELECTION ALGORITHM---------------
    # lowlist = [item for item in string.ascii_lowercase]
    # upplist = [item for item in string.ascii_uppercase]
    # numlist = [item for item in string.digits]
    # spezlist = [item for item in string.punctuation]

    # global var_1
    # global length_entry
    # global lowercase_letters
    # global uppercase_letters
    # global numbers_chars
    # global special_chars
    # passlist = []

    # quant = int(length_entry.get())

    # if lowercase_letters==True:
    # 	passlist.append(lowlist)
    # if uppercase_letters==True:
    # 	passlist.append(upplist)
    # if numbers_chars==True:
    # 	passlist.append(numlist)
    # if special_chars==True:
    # 	passlist.append(spezlist)


    # password = ''.join([random.choice(passlist) for item in range(quant)])
    # var_1.set(password)