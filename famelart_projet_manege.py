import tkinter as tk
from tkinter import messagebox

def autorisation():
  age=int(entry_age.get())
  taille=float(entry_taille.get())

  if age < 14:
      label_resultat.config(text="Il faut minimum 14 ans")
  else:
      if (taille >= 1.1 and taille < 1.3):
          label_resultat.config(text="Autorisation pour Force 1")
      elif taille >= 1.3:
          label_resultat.config(text="Autorisation pour Force 2")
      else :
          label_resultat.config(text="La taille n'est pas suffisante")

def affiche_message():
  age = entry_age.get()
  messagebox.showinfo("Age ", age)

fenetre = tk.Tk()
fenetre.title("TP Manège Parc d'attraction - BTS CIEL")
fenetre.geometry("450x300")

label = tk.Label(fenetre, text="Manège du parc - Force 1/Force 2", bg="mintcream", fg="navy", font =(18))
label.pack(side="top", fill="x")


label = tk.Label (fenetre, text="Entrez votre âge et votre taille pour savoir à quelle force vous pouvez faire le manège.", fg="black", font =(16), wraplength =450)
label.pack(pady=10)

label_age = tk.Label(fenetre, text="Entrez votre âge:", font =(16))
label_age.pack(pady=5)
entry_age = tk.Entry(fenetre)
entry_age.pack(pady=5)

label_taille = tk.Label(fenetre, text="Entrez votre taille (en mètre, exemple : 1.73):", font=(16))
label_taille.pack(pady=5)
entry_taille = tk.Entry(fenetre)
entry_taille.pack(pady=5)

label_resultat = tk.Label(fenetre, text="", font=(16), fg="blue")
label_resultat.pack(pady=10)
button_resultat = tk.Button(fenetre, text="Envoyer", font=(16), command=autorisation)
button_resultat.pack(pady=5)

fenetre.mainloop()