import tkinter as tk
import random
import turtle


#Function to draw the heart
def drawheart():
    root = turtle.Screen()
    root.title("Drawing a heart for u ❤️")
    root.bgcolor("white")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red")
    t.speed(3)

    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)  
    t.right(140)
    t.circle(50, 200)  
    t.forward(133)
    t.end_fill()

    t.penup()
    t.goto(0, -50)
    t.color("black")
    t.write("¡made with love for me! M...", align="center", font=("Arial", 16, "bold"))
    t.hideturtle()

    
    root.mainloop()

#Function to accept the love
def ActionYes():
    
    menuMain.withdraw()

    
    global menuYes
    menuYes = tk.Toplevel()
    menuYes.title("Jumping Love")
    menuYes.configure(bg="#FFDEE9")
    menuYes.geometry("300x200")
    menuYes.resizable(False, False)
    
    
    messageYes = tk.Label(menuYes, text="Thank You For Choose Be My Love", font=("Arial", 14))
    messageYes.pack(pady=20)
    
    
    buttonYes = tk.Button(menuYes, text="Draw Heart ❤️", command=drawheart, width=15, cursor="hand2")
    buttonYes.pack(pady=20)

    buttonClose = tk.Button(menuYes, text="Close", command=menuYes.destroy, width=10, cursor="hand2")
    buttonClose.pack(pady=20)

#Function to move the menu of the love
def ActionNo():
    
    
    screenwide = menuMain.winfo_screenwidth()
    screentall = menuMain.winfo_screenheight()

    
    new_x = random.randint(0, screenwide - menuMain.winfo_width())
    new_y = random.randint(0, screentall - menuMain.winfo_height())

    
    menuMain.geometry(f"+{new_x}+{new_y}")

#Function to open the menu of the love
def open_menu():
    rootMain.withdraw()


    global menuMain
    menuMain = tk.Toplevel()
    menuMain.title("Jumping Love")
    menuMain.configure(bg="#FFDEE9")
    menuMain.geometry("")
    menuMain.resizable(False,False)
    
    firstmessage = tk.Label(menuMain, text="You Wanna Be My GirlFriend?", font=("Arial", 14))
    firstmessage.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    
    buttonYes = tk.Button(menuMain, text="Yes", command=ActionYes, width=10, cursor="hand2")
    buttonYes.grid(row=13, column=1, sticky="ew", padx=10, pady=5)
    
    buttonNo = tk.Button(menuMain, text="No", command=ActionNo, width=10,  cursor="hand2")
    buttonNo.grid(row=13, column=0, sticky="w", padx=10, pady=5)

    menuMain.mainloop()




#Root of the main window
rootMain = tk.Tk()
rootMain.title("Main")
rootMain.geometry("")
rootMain.resizable(False, False)

messageWelcome = tk.Label(rootMain, text="Welcome To Jumping Love", font=("Arial", 14))
messageWelcome.pack(pady=20)

buttonStart = tk.Button(rootMain, text="Start", command=open_menu, width=10, cursor="hand2")
buttonStart.pack(pady=20)

groupLabel = tk.Label(rootMain, text="Click Start", anchor='s')
groupLabel.pack(side=tk.BOTTOM, pady=10)

rootMain.mainloop()