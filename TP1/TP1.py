import random
import math
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

class Jeu:
    def __init__(self):

        self.__liste_personnage = {
                                    "Zilong" : {"nom" : "Zilong",
                                                "classe" : "Combattant",
                                                "compétence" : ["Spear Flip", "Spear Strike", "Supreme Warrior", "Dragon Flurry"],
                                                "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Zilong.jpg"},

                                    "Freya" : {"nom" : "Freya",
                                               "classe" : "Combattant",
                                               "compétence" : ["Leap of Faith", "Spirit Combo", "Valkyrie Descent", "Power of Einherjar"],
                                               "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Freya.jpg"},
                                    
                                    "Franco" : {"nom" : "Franco",
                                                "classe" : "Tank",
                                                "compétence" : ["Iron Hook", "Fury Shock", "Bloody Hunt", "Wasteland Force"],
                                                "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Franco.png"},
                                    
                                    "Tigreal" : {"nom" : "Tigreal",
                                                 "classe" : "Tank",
                                                 "compétence" : ["Attack Wave", "Sacred Hammer", "Implosion", "Fearless"],
                                                 "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Tigreal.jpg"},
                                    
                                    "Xavier" : {"nom" : "Xavier",
                                                "classe" : "Mage",
                                                "compétence" : ["Infinite Extension", "Mystic Field", "Dawning Light", "Transcendence"],
                                                "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Xavier.png"},
                                    
                                    "Chang'e" : {"nom" : "Chang'e",
                                                 "classe" : "Mage",
                                                 "compétence" : ["Starmoon Shockwave", "Crescent Moon", "Meteor Shower", "Trouble Maker"],
                                                 "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Chang'e.png"},
                                    
                                    "Miya" : {"nom" : "Miya",
                                              "classe" : "Tireur",
                                              "compétence" : ["Moon Arrow", "Arrow of Eclipse", "Hidden Moonlight", "Moon Blessing"],
                                              "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Miya.png"},
                                    
                                    "Layla" : {"nom" : "Layla",
                                               "classe" : "Tireur",
                                               "compétence" : ["Malefic Bomb", "Void Projectile", "Destruction Rush", "Malefic Gun"],
                                               "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Layla.jpg"},
                                    
                                    "Angela" : {"nom" : "Angela",
                                                "classe" : "Support",
                                                "compétence" : ["Love Waves", "Puppet-on-a-String", "Heartguard", "Smart Heart"],
                                                "image" : r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Angela.png"}        
                                    }
        
        # créer une instance de la classe Factory
        factory = Factory()
        
        # parcourir les clés du dictionnaire et créer une instance de chaque personnage
        instance = {}
        for nom_personnage in self.__liste_personnage:
            personnage = factory.creer_personnage(self.__liste_personnage[nom_personnage]["nom"], self.__liste_personnage[nom_personnage]["classe"], self.__liste_personnage[nom_personnage]["compétence"])
            instance[nom_personnage] = personnage
            
        def printerL(event):
            if ListePersonnageL.curselection() != ():
                textL.delete('1.0', tk.END)
                textL.insert(tk.END, instance[ListePersonnageL.get(ListePersonnageL.curselection())].allInfo() + '\n')
                textL.tag_configure('center', justify='center') # alignement au centre
                textL.tag_add('center', '1.0', 'end')
                
                # Récupère le nom du personnage sélectionné
                nom_personnage = ListePersonnageL.get(ListePersonnageL.curselection())
                # Récupère le chemin de l'image du personnage
                chemin_image = self.__liste_personnage[nom_personnage]["image"]
                # Charge l'image avec Pillow et crée un objet ImageTk
                image = Image.open(chemin_image)
                image_tk = ImageTk.PhotoImage(image)
                # Met à jour le widget Label avec l'image
                persoL_label.configure(image=image_tk)
                persoL_label.image = image_tk  # Garde une référence à l'objet ImageTk pour éviter la suppression automatique
                               
        def printerR(event):
            if ListePersonnageR.curselection() != ():
                textR.delete('1.0', tk.END)
                textR.insert(tk.END, instance[ListePersonnageR.get(ListePersonnageR.curselection())].allInfo() + '\n')
                textR.tag_configure('center', justify='center') # alignement au centre
                textR.tag_add('center', '1.0', 'end')                
        
                # Récupère le nom du personnage sélectionné
                nom_personnage = ListePersonnageR.get(ListePersonnageR.curselection())
                # Récupère le chemin de l'image du personnage
                chemin_image = self.__liste_personnage[nom_personnage]["image"]
                # Charge l'image avec Pillow et crée un objet ImageTk
                image = Image.open(chemin_image)
                image_tk = ImageTk.PhotoImage(image)
                # Met à jour le widget Label avec l'image
                persoR_label.configure(image=image_tk)
                persoR_label.image = image_tk  # Garde une référence à l'objet ImageTk pour éviter la suppression automatique
                
        def fight():
            perso1 = ListePersonnageL.get("active")
            perso2 = ListePersonnageR.get("active")
            try:
                if perso1 and perso2:
                    actualiser(perso1, perso2)
                    textMid.insert(tk.END, instance[perso1].attaquer(instance[perso2]) + '\n')
                    textMid.tag_configure('center', justify='center') # alignement au centre
                    textMid.tag_add('center', '1.0', 'end')
                else:
                    print("Please select one character from each listbox.")
            except AttributeError:
                messagebox.showerror("Error", "This character can't fight.")            
        
        def heal():
            perso1 = ListePersonnageL.get("active")
            perso2 = ListePersonnageR.get("active")
            try:
                if perso1 and perso2:
                    actualiser(perso1, perso2)
                    textMid.insert(tk.END, instance[perso1].soigner(instance[perso2]) + '\n')
                    textMid.tag_configure('center', justify='center') # alignement au centre
                    textMid.tag_add('center', '1.0', 'end')
                else:
                    print("Please select one character from each listbox.")                   
            except AttributeError:
                messagebox.showerror("Error", "This character can't heal.")
                            
        def actualiser(perso1, perso2):
            textL.delete('1.0', tk.END)
            textR.delete('1.0', tk.END)
            textMid.delete('1.0', tk.END)
            textL.insert(tk.END, instance[perso1].allInfo() + '\n')
            textL.tag_configure('center', justify='center') # alignement au centre
            textL.tag_add('center', '1.0', 'end')
            textR.insert(tk.END, instance[perso2].allInfo() + '\n')
            textR.tag_configure('center', justify='center') # alignement au centre
            textR.tag_add('center', '1.0', 'end')
        
        fen = tk.Tk() # Création de la fenêtre
        fen.title("TP1") # Titre de la fenêtre
        fen.geometry("860x700") # Taille de la fenêtre
        fen.iconbitmap(r"C:\Users\victo\OneDrive\Bureau\POO\TP1\Mobile.ico") # Icone de la fenêtre

        img = Image.open(r"C:\Users\victo\OneDrive\Bureau\POO\TP1\img\Lightborn.jpg") # Image de fond
        bg = ImageTk.PhotoImage(img)
        bg_label = tk.Label(fen, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        Titre = tk.Label(fen, text="MobileLegend", bg="#fef27d", fg="#8796ac", font=("Calibri", "32"), relief=tk.GROOVE) # Création du titre
        Titre.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        boutonCombat = tk.Button(fen, text="Combat", bg="black", fg="white", font=("Calibri", "20"), relief=tk.GROOVE, width=7, height=1, command=fight) # Création du bouton Combat
        boutonCombat.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        boutonSoigne = tk.Button(fen, text="Soigne", bg="black", fg="white", font=("Calibri", "20"), relief=tk.GROOVE, width=7, height=1, command=heal) # Création du bouton Soigne
        boutonSoigne.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        ListePersonnageL = tk.Listbox(fen, bg="black", fg="white", font=("Calibri", "20"), relief=tk.GROOVE, width=10) # Création de la liste des personnages
        
        i = 0
        for nom_personnage in instance:
            i += 1
            ListePersonnageL.insert(i, instance[nom_personnage].nom)
                        
        ListePersonnageL.config(height=ListePersonnageL.size()) # Ajuster la taille de la liste en fonction du nombre d'éléments
        ListePersonnageL.bind('<<ListboxSelect>>', printerL) # Lorsqu'un élément est sélectionné, afficher son nom dans la console
        ListePersonnageL.grid(row=1, column=0, padx=10, pady=10, sticky="nsew") # Placement de la liste

        ListePersonnageR = tk.Listbox(fen, bg="black", fg="white", font=("Calibri", "20"), relief=tk.GROOVE, width=10) # Création de la liste des personnages
        
        i = 0
        for nom_personnage in instance:
            i += 1
            ListePersonnageR.insert(i, instance[nom_personnage].nom)
            
        ListePersonnageR.config(height=ListePersonnageR.size()) # Ajuster la taille de la liste en fonction du nombre d'éléments
        ListePersonnageR.bind('<<ListboxSelect>>', printerR) # Lorsqu'un élément est sélectionné, afficher son nom dans la zone de texte
        ListePersonnageR.grid(row=1, column=4, padx=10, pady=10, sticky="nsew") # Placement de la liste

        textL = tk.Text(fen, bg="black", fg="white", font=("Calibri", "20"), relief=tk.GROOVE, width=10, height=5) # Création de la zone de texte
        textR = tk.Text(fen, bg="black", fg="white", font=("Calibri", "20"), relief=tk.GROOVE, width=10, height=5) # Création de la zone de texte
        textMid = tk.Text(fen, bg="black", fg="white", font=("Calibri", "19"), relief=tk.GROOVE, width=10, height=5) # Création de la zone de texte

        textL.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        textR.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")
        textMid.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        
        ###########################################################################   
        persoR_label = tk.Label(fen, bd=0, highlightthickness=0)
        persoL_label = tk.Label(fen, bd=0, highlightthickness=0)
        persoR_label.grid(row=2, column=3)
        persoL_label.grid(row=2, column=1)
        ListePersonnageR.bind("<<ListboxSelect>>", printerR)      
        ListePersonnageL.bind("<<ListboxSelect>>", printerL)      
        ###########################################################################

        fen.mainloop() # Boucle principale de la fenêtre
        
    @property
    def liste_personnage(self):
        return self.__liste_personnage
    
class Factory:
    def __init__(self):
        pass
    
    def creer_personnage(self, nom, classe, compétence):
        if classe == "Combattant":
            return Combattant(nom, compétence)
        elif classe == "Tank":
            return Tank(nom, compétence)
        elif classe == "Mage":
            return Mage(nom, compétence)
        elif classe == "Tireur":
            return Tireur(nom, compétence)
        elif classe == "Support":
            return Support(nom, compétence)
        else:
            return NotImplementedError

class NoHPErreur(Exception):
    pass

class Personnage:
    def __init__(self, nom, compétence):
        if type(self) == Personnage :
            raise NotImplementedError()
        else :
            self.nom = nom
            self.pv = random.randint(5000, 8000)
            self.position = random.randint(1, 10)
            self.compétence = compétence
            
    def allInfo(self):
        return f"{self.nom} ({self.__class__.__name__}) - PV : {self.pv}"

# Interface Attaquant
class Attaquant(Personnage):
    def __init__(self, nom, compétence):
        if type(self) == Attaquant :
            raise NotImplementedError()
        else :
            super().__init__(nom, compétence)
            self.atq = random.randint(1000, 2000)
    
    def attaquer(self, personnage):
        raise NotImplementedError()
    
    def allInfo(self):
        return f"{self.nom} \n{self.__class__.__name__} \nPV : {self.pv} \nATQ : {self.atq}"
        #return f"{self.nom} ({self.__class__.__name__}) - PV : {self.pv} - ATQ : {self.atq}"
    
# Interface Soignant 
class Soignant(Personnage):
    def __init__(self, nom, compétence):
        if type(self) == Soignant :
            raise NotImplementedError()
        else :
            super().__init__(nom, compétence)
            self.soin = random.randint(1000, 3000)
        
    def soigner(self, personnage):
        raise NotImplementedError()
    
    def allInfo(self):
        return f"{self.nom} \n{self.__class__.__name__} \nPV : {self.pv} \nSOIN : {self.soin}"        
        #return f"{self.nom} ({self.__class__.__name__}) - PV : {self.pv} - SOIN : {self.soin}"

# Les Guerriers peuvent attaquer d'autres personnages       
class Guerrier(Attaquant):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)

    def attaquer(self, personnage):
        self.attaque = self.compétence[random.randint(0, len(self.compétence)-1)]
        
        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot attack"
        
        elif personnage == self :
            return "You cannot attack yourself"
        
        elif personnage.pv <= 0 :
            return f"{personnage.nom} ({personnage.__class__.__name__}) \nis already dead"
        
        elif (abs(self.position - personnage.position) > 5) :
            return "The enemy is out of \nrange"
         
        elif type(personnage) == Tank :
            personnage.pv -= math.ceil(self.atq/3)
            return f"{self.nom} ({self.__class__.__name__}) uses {self.attaque} and deals {math.ceil(self.atq/3)} \ndamage to {personnage.nom}"
        
        else :
            personnage.pv -= self.atq
            return f"{self.nom} ({self.__class__.__name__}) uses {self.attaque} and deals {self.atq} \ndamage to {personnage.nom}"
    
# Les Combattants subissent des degats lorsqu'ils attaquent
class Combattant(Guerrier):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)
            
    def attaquer(self, personnage):
        self.attaque = self.compétence[random.randint(0, len(self.compétence)-1)]
        
        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot attack"
        
        elif personnage == self :
            return "You cannot attack yourself"

        elif personnage.pv <= 0 :
            return f"{personnage.nom} ({personnage.__class__.__name__}) \nis already dead"
        
        elif (abs(self.position - personnage.position) > 5) :
            return "The enemy is out of \nrange"
        
        elif type(personnage) == Tank :
            self.pv -= 500
            personnage.pv -= math.ceil(self.atq/3)
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {math.ceil(self.atq/3)} \ndamage to {personnage.nom}"

        else :
            self.pv -= 1000
            personnage.pv -= self.atq*2
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {self.atq*2} \ndamage to {personnage.nom}"

# Les Tanks subissent moins de degats lorsqu'ils sont attaques
class Tank(Guerrier):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)
            
    def attaquer(self, personnage):
        self.attaque = self.compétence[random.randint(0, len(self.compétence)-1)]
        
        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot attack"
        
        elif personnage == self :
            return "You cannot attack \nyourself"
        
        elif personnage.pv <= 0 :
            return f"{personnage.nom} ({personnage.__class__.__name__}) \nis already dead"      
          
        elif (abs(self.position - personnage.position) > 5) :
            return "The enemy is out of \nrange"
                
        elif type(personnage) == Tank :
            personnage.pv -= math.ceil(self.atq/3)
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {math.ceil(self.atq/3)} \ndamage to {personnage.nom}"
        
        else :
            personnage.pv -= math.ceil(self.atq/2)
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {math.ceil(self.atq/2)} \ndamage to {personnage.nom}"

# Les Tireurs ont une plus grande portee et se soigne lorsqu'ils attaquent
class Tireur(Guerrier):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)
            
    def attaquer(self, personnage):
        self.attaque = self.compétence[random.randint(0, len(self.compétence)-1)]

        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot attack"
        
        elif personnage == self :
            return "You cannot attack \nyourself"
        
        elif personnage.pv <= 0 :
            return f"{personnage.nom} ({personnage.__class__.__name__}) \nis already dead"       
         
        elif (abs(self.position - personnage.position) < 2) :
            return "The enemy is out of \nrange"
                
        elif type(personnage) == Tank :
            self.pv += 500
            personnage.pv -= math.ceil(self.atq/3)
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {math.ceil(self.atq/3)} \ndamage to {personnage.nom}"
        
        else :
            self.pv += 1000
            personnage.pv -= self.atq
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {self.atq} \ndamage to {personnage.nom}"
        
# Les Mages ont une plus grande portee et sont les contres des Tanks
class Mage(Guerrier):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)
            
    def attaquer(self, personnage):
        self.attaque = self.compétence[random.randint(0, len(self.compétence)-1)]

        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot attack"
        
        elif personnage == self :
            return "You cannot attack \nyourself"
        
        elif personnage.pv <= 0 :
            return f"{personnage.nom} ({personnage.__class__.__name__}) \nis already dead"
        
        elif ((abs(self.position - personnage.position) < 2) or (abs(self.position - personnage.position) > 8)) :
            return "The enemy is out of \nrange"
               
        else :
            personnage.pv -= self.atq
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {self.atq} \ndamage to {personnage.nom}"        

# Les Soigneurs peuvent soigner d'autres personnages     
class Soigneur(Soignant):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)
        
    def soigner(self, personnage):
        self.sort = self.compétence[random.randint(0, len(self.compétence)-1)]

        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot heal"
        else :
            personnage.pv += self.soin
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.sort} \nand heals {self.soin} HP to {personnage.nom}"
    
# Le Paladin est un attaquant et un soignant   
class Paladin(Attaquant, Soignant):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)
        self.sort_attaque = self.compétence[random.randint(0, len(self.compétence)-1)]
        self.sort_soin = self.compétence[random.randint(0, len(self.compétence)-1)]

    def allInfo(self):
        return f"{self.nom} \n{self.__class__.__name__} \nPV : {self.pv} \nATQ : {self.atq} \nSOIN : {self.soin}"     
        #return f"{self.nom} ({self.__class__.__name__}) - PV : {self.pv} - ATQ : {self.atq} - SOIN : {self.soin}"
    
# Les Supports sont des soigneurs qui peuvent attaquer
class Support(Paladin):
    def __init__(self, nom, compétence):
        super().__init__(nom, compétence)

    def attaquer(self, personnage):
        self.attaque = self.compétence[random.randint(0, len(self.compétence)-1)]

        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot attack"
        
        elif personnage == self :
            return "You cannot attack \nyourself"
        
        elif personnage.pv <= 0 :
            return f"{personnage.nom} ({personnage.__class__.__name__}) \nis already dead"       
         
        elif (abs(self.position - personnage.position) > 4) :
            return "The enemy is out of \nrange"
                
        elif type(personnage) == Tank :
            personnage.pv -= math.ceil(self.atq/3)
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {math.ceil(self.atq/3)} \ndamage to {personnage.nom}"
        
        else :
            personnage.pv -= math.ceil(self.atq/2)
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.attaque} \nand deals {math.ceil(self.atq/2)} \ndamage to {personnage.nom}"
    
    def soigner(self, personnage):
        self.sort = self.compétence[random.randint(0, len(self.compétence)-1)]

        if self.pv <= 0 :
            return f"{self.nom} ({self.__class__.__name__}) \nis dead and \ncannot heal"
        else :
            personnage.pv += self.soin
            return f"{self.nom} ({self.__class__.__name__}) \nuses {self.sort} \nand heals {self.soin} HP to {personnage.nom}"

MobileLegend = Jeu()