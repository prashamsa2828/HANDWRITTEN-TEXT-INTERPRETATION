import easyocr

from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from translate import Translator




reader = easyocr.Reader(['en','en'], gpu = False)
import PIL
from PIL import ImageDraw

                         
im = PIL.Image.open(r'C:\Users\prashamsa28\OneDrive\Desktop\htr\text5.jfif')
im
                         
bounds = reader.readtext(r'C:\Users\prashamsa28\OneDrive\Desktop\htr\text5.jfif')
bounds
def draw_boxes(image, bounds, color='yellow',width = 8):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3], fill= color, width = width)
    return image
draw_boxes(im, bounds)

im.save(r"C:\Users\prashamsa28\OneDrive\Desktop\htr\text5.jfif")

len(bounds)
la=[]
for i in bounds:
    la.append(i[1])
f = open(r'C:\Users\prashamsa28\OneDrive\Desktop\htr\text5.jfif.txt', mode= 'a', encoding="utf-8")
win = Tk()

win.geometry("750x350")


def open_win():
   new= Toplevel(win)
   new.geometry("250x200")
   new.title("New Window")
   #Create a Label in New window
   translator= Translator(to_lang="Hindi")
   
   translation = translator.translate(str(la))
   Label(new, text=translation, font=('Helvetica 17 bold')).pack(pady=30)
   
#Label(win, text= "LANGUAGE", font= ('Helvetica 17 bold')).pack(pady=30)   


#Create a label
ttk.Button(win, text="TRANSLATE", command=open_win).pack()
link=Label(win,text=la,font=('Helvetica 14 bold'),fg='blue',cursor='hand2')

#Create a button to open a New Window



link.pack()
link.bind("<Button-1>",lambda e:la ) 


img = ImageTk.PhotoImage(Image.open("BACK.png"))
panel = Label(win, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

 
win.mainloop()        
for i in bounds:
    print(i[1])
    f.write(i[1])

   
