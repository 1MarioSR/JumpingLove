import tkinter as tk


def open_menu():
    rootMain.withdraw()


    global menuMain
    menuMain = tk.Toplevel()
    menuMain.title("Jumping Love")
    menuMain.geometry("")
    menuMain.resizable(False,False)
    
    firstmessage = tk.Label(menuMain, text="You Wanna Be My GirlFriend?", font=("Arial", 14))
    firstmessage.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    
    buttonYes = tk.Button(menuMain, text="Yes", command=print("hola"), width=10)
    buttonYes.grid(row=13, column=1, sticky="ew", padx=10, pady=5)
    
    buttonNo = tk.Button(menuMain, text="No", command=print("hola"), width=10)
    buttonNo.grid(row=13, column=0, sticky="w", padx=10, pady=5)

    menuMain.mainloop()




#Root of the main window
rootMain = tk.Tk()
rootMain.title("Main")
rootMain.geometry("")
rootMain.resizable(False, False)

messageWelcome = tk.Label(rootMain, text="Welcome To Jumping Love", font=("Arial", 14))
messageWelcome.pack(pady=20)

buttonStart = tk.Button(rootMain, text="Start", command=open_menu, width=10)
buttonStart.pack(pady=20)

groupLabel = tk.Label(rootMain, text="Click Start", anchor='s')
groupLabel.pack(side=tk.BOTTOM, pady=10)

rootMain.mainloop()