import tkinter as tk, math, datetime as dt
win = tk.Tk()
win.title('Hodziny')

velkost = 800
s1 = velkost/2
s2 = velkost/2
kratka_ruc = 75    
dlha_ruc = 150
hrubka_h = 5
hrubka_m = 3
hrubka_s = 1

canvas = tk.Canvas(win, width=velkost, height=velkost, bg='white')
canvas.pack()

rucicka_min =  canvas.create_line(s1, s2, s1,  s2 - dlha_ruc, width = hrubka_m, fill= 'black')
rucicka_sekunda = canvas.create_line(s1, s2, s1, s2 - dlha_ruc, width = hrubka_s, fill= 'brown')
rucicka_hodina = canvas.create_line(s1, s2, s1, s2 - kratka_ruc, width = hrubka_h, fill= 'black')

canvas.create_oval(250,250,550,550,  outline = "black")
canvas.create_oval(215,215,585,585, width = 5, outline = "brown")
for i in range(1, 13):
   canvas.create_text(s1+170*math.cos(math.radians(i*30-90)),s2+170*math.sin(math.radians(i*30-90)) , font='Arial 15 bold', text=i, fill = "brown")

def hodziny():
    cas = dt.datetime.now()
    uhol_min = math.radians(cas.minute * 6 - 90)   
    uhol_sek = math.radians(cas.second * 6 - 90)   
    uhol_hod = math.radians(cas.hour * 30 + cas.minute * 0.5 - 90)   
    canvas.coords(rucicka_min, s1, s2, s1 + dlha_ruc * math.cos(uhol_min), s2 + dlha_ruc * math.sin(uhol_min))
    canvas.coords(rucicka_sekunda, s1, s2, s1 + dlha_ruc * math.cos(uhol_sek), s2 + dlha_ruc * math.sin(uhol_sek))
    canvas.coords(rucicka_hodina, s1, s2, s1 + kratka_ruc * math.cos(uhol_hod), s2 + kratka_ruc * math.sin(uhol_hod))
    canvas.after(1000, hodziny)

hodziny()
win.mainloop()
