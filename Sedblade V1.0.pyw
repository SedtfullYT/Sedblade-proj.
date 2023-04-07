import random
import tkinter

wts=open("settings.txt","r")
global fs
fs=int(wts.read())
print(fs)
wts.close()

def boxer():
    global cclass
    cclass="Hard mode"
    gameplay()
def kickboxer():
    global cclass
    cclass="Normal mode"
    gameplay()
def wrestler():
    global cclass
    cclass="Easy mode"
    gameplay()

def menug():
    global menu
    menu=tkinter.Tk()
    menu.title("Sedblade")
    menu.geometry("500x500")
    menu.configure(background="Black", cursor="dot")
    
    print("Game initialised.\n")

    def togglefullscreen():
        global fs
        if fs==1:
            fs-=1
            fsy.configure(text="Disabled")
            menu.attributes("-fullscreen",False)
            print("Fullscreen disabled")
            wts=open("settings.txt","w")
            wts.write("0")
            wts.close()
            
        elif fs==0:
            fs+=1
            fsy.configure(text="Enabled")
            menu.attributes("-fullscreen",True)
            print("Fullscreen enabled")
            wts=open("settings.txt","w")
            wts.write("1")
            wts.close()


    title=tkinter.Label(menu, text="🆂🅴🅳🅱🅻🅰🅳🅴", font=("Blackadder ITC",  59, "underline", "bold"),pady=1, bg="black", fg="white")
    boxert=tkinter.Button(menu, text="Hard mode", command=boxer, pady=5, width=23, bg="black", font=("20"), fg="white")
    kickboxert=tkinter.Button(menu, text="Normal mode",command=kickboxer, pady=5, width=23, bg="black", font=("20"), fg="white")
    wrestlert=tkinter.Button(menu, text="Easy mode",command=wrestler, pady=5, width=23, bg="black", font=("20"), fg="white")
    mexit=tkinter.Button(menu, text="Exit", command=exit)
    settings=tkinter.Label(menu, text="Settings", font=("Kristen ITC", 27, "bold"),bg="Black", fg="white")
    flscrn=tkinter.Label(menu, text="Fullscreen",font=("Kristen ITC", 14, "bold"), bg="Black", fg="white")
    runss=tkinter.Label(menu, text="Thanks for playing. This is my first game so please don't roast me too much lol",font=("Kristen ITC", 14, "underline"), bg="Black", fg="white")
    logoss=tkinter.Label(menu, text="(ง︡'-'︠)ง",font=("Kristen ITC", 70, "bold"), bg="Black", fg="white")
    fsy=tkinter.Button(menu, text="ON/OFF", command=togglefullscreen)
    
    if fs==0:
        menu.attributes("-fullscreen",False)
        fsy.configure(text="Disabled")
    elif fs==1:
        menu.attributes("+fullscreen",True)
        fsy.configure(text="Enabled")

    mexit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    title.pack(side=tkinter.TOP)
    boxert.pack()
    kickboxert.pack()
    wrestlert.pack()
    runss.pack(side=tkinter.BOTTOM)
    logoss.pack()
    settings.pack(side=tkinter.BOTTOM)
    flscrn.pack(side=tkinter.BOTTOM)
    fsy.pack(side=tkinter.BOTTOM)
    menu.mainloop()
    

def gameplay():
    global menu
    menu.destroy()
    window=tkinter.Tk()
    window.title("Sedblade - Match")
    window.geometry("640x480")
    window.configure(background="Black", cursor="dot")
    if fs==0:
        window.attributes("-fullscreen",False)
    elif fs==1:
        window.attributes("+fullscreen",True)


    global basehp
    global health
    global cclass
    global tdmgp
    global tdmg
    tdmg=0
    tdmgp=0
    if cclass=="Hard mode":
        pmodifier=0.5
        kmodifier=0.5
        gmodifier=0.25
        health=100
        basehp=100
    elif cclass=="Normal mode":
        pmodifier=0.5
        kmodifier=1.5
        gmodifier=0.25
        health=125
        basehp=125
    elif cclass=="Easy mode":
        pmodifier=0.5
        kmodifier=0.5
        gmodifier=2
        health=210
        basehp=210

    global ehealth
    ehealth=int(round(health*1.25))
    global emodifier
    emodifier=1.3
    global ebasehp
    ebasehp=ehealth

    global pwin
    pwin=0

    def pwin():
        global ehealth
        if ehealth<=0:
            ehealthl.configure(text="Health: 0"+"/"+str(ebasehp))
            print("Player has won :D")
            global pwin
            pwin=1
            winner.configure(text="Player has won :D")

    def ewin():
        global health
        if health<=0:
            healthl.configure(text="Health: 0"+"/"+str(basehp))
            print("Enemy has won :(")
            global pwin
            pwin=1
            winner.configure(text="Enemy has won :(")

    def echance():
        global pwin
        global tdmg
        
        if pwin!=1:
            global health
            missche=random.randint(0,13)
            echance=random.randint(0,13)
            if echance>=5:
                if missche>=11:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed!")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(10,20)*emodifier))
                    health-=dmgdealt
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
                    enemymove.configure(text="Enemy used: Punch(Damage dealt: "+(str(dmgdealt))+")")
                    
            elif echance>=10:
                if missche>=10:
                    print("Enemy attack missed!")
                    enemymove.configure(text="Enemy attack missed!")
                else:
                    global ehealth
                    dmgdealt=int(round(random.randint(14,26)*emodifier))
                    health-=dmgdealt
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(health)+"/"+str(basehp))
                    enemymove.configure(text="Enemy used: Kick(Damage dealt: "+(str(dmgdealt))+")")
            
            elif echance<=4:
                global tdmg
                chance=1
                while chance<7:
                    dmgdealt=random.randint(2,7)*emodifier
                    tdmg+=int(round(dmgdealt))
                    health-=dmgdealt
                    chance=int(round(random.randint(0,11)))
                    print("Player health is now: "+str(health))
                    healthl.configure(text="Health: "+str(int(round(health)))+"/"+str(basehp))
                enemymove.configure(text="Enemy used: Grapple(Damage dealt: "+(str(tdmg))+")")           
            tdmg=0
    def punchp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=11:
                print("Player attack missed!")
            else:
                global dmgdealtp
                dmgdealtp=int(round(random.randint(9,21)*pmodifier))
                ehealth-=dmgdealtp
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()


    def kickp():
        global pwin
        if pwin!=1:
            global ehealth
            missch=random.randint(0,13)
            if missch>=10:
                print("Player attack missed!")
            else:
                global dmgdealtp
                dmgdealtp==int(round(random.randint(14,26)*kmodifier))
                ehealth-=dmgdealtp
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
                playerddealt.configure(text="Damage dealt to enemy: "+str(dmgdealtp))
            pwin()
            echance()
            ewin()

    def grapplep():
        if pwin!=1:
            global ehealth
            global tdmgp
            chance=1
            while chance<7:
                dmgdealtp=random.randint(2,7)*gmodifier
                tdmgp+=dmgdealtp
                ehealth-=dmgdealtp
                chance=int(round(random.randint(0,11)))
                print("Enemy health is now: "+str(ehealth))
                ehealthl.configure(text="Health: "+str(int(round(ehealth)))+"/"+str(ebasehp))
            playerddealt.configure(text="Damage dealt to enemy: "+str(tdmgp))
            tdmgp=0                
            pwin()
            echance()
            ewin()
    def restart():
        print("\nNew game loaded\n")
        window.destroy()
        menug()
		
    player=tkinter.Label(window, text="Player (￣_,￣ )", font=("Kristen ITC", 24, "bold"))
    healthl=tkinter.Label(window, text=("Health💓: "+str(health)+"/"+str(basehp)), font=("Kristen ITC", 18))
    enemy=tkinter.Label(window, text="Enemy💀", font=("Kristen ITC", 24, "bold"))
    ehealthl=tkinter.Label(window, text=("Health💓: "+str(ehealth)+"/"+str(ebasehp)), font=("Kristen ITC", 18))
    punch=tkinter.Button(window, text="Punch",command=punchp)
    kick=tkinter.Button(window, text="Kick", command =kickp)
    grapple=tkinter.Button(window, text="Grapple", command=grapplep)
    restart=tkinter.Button(window, text="Restart", command=restart)
    texit=tkinter.Button(window, text="Exit", command=exit)
    enemymove=tkinter.Label(window,text="", font=("Kristen ITC", 14), bg="Black",fg="white")
    playerddealt=tkinter.Label(window,text="", font=("Kristen ITC", 14), bg="Black", fg="white")
    winner=tkinter.Label(window, text="", font=("Kristen ITC", 14, "bold"), bg="Black", fg="white")

    texit.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    player.pack(pady=10, padx=20, fill=tkinter.X)
    healthl.pack()
    punch.pack(pady=3)
    kick.pack(pady=3)
    grapple.pack(pady=3)
    playerddealt.pack()
    enemy.pack(pady=10, padx=20, fill=tkinter.X)
    ehealthl.pack()
    enemymove.pack()
    restart.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    winner.pack(side=tkinter.BOTTOM)
    window.mainloop()


menug()

