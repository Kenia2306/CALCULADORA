
from tkinter import*

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x400")

frame = Frame(ventana)
frame.config(height="300px",width="600px")
frame.pack(fill="both",expand=1)

titulo = Label(frame,text="CALCULADORA ")
titulo.pack(side=TOP)

n1 = StringVar()
n2= StringVar()
r= StringVar()

def suma():
   r.set(float(n1.get())+float(n2.get()))
   

def resta():
   r.set(float(n1.get())-float(n2.get()))
   

def multiplicacion():
       r.set(float(n1.get())*float(n2.get()))
   
   
def division():
       r.set(float(n1.get())/float(n2.get()))
   
def borrar():
     n1.set(" ")
     n2.set(" ")
     r.set(" ")
   
   
lbl_numeroA = Label(ventana, text="Numero A").place(relx=0.2,rely=0.2)
entrada_numeroA2 = Entry(ventana,textvariable=n1).place(relx=0.4,rely=0.2)

lbl_numeroB = Label(ventana, text="Numero B").place(relx=0.2,rely=0.3)
entrada_numeroB2 = Entry(ventana,textvariable=n2).place(relx=0.4,rely=0.3)


lbl_RESULTADO = Label(ventana, text="Resultado").place(relx=0.2,rely=0.4)
entrada_RESULTADO2 = Entry(ventana,textvariable=r).place(relx=0.4,rely=0.4)

rbt_suma = Button(ventana, text="SUMA",command=suma).place(relx=0.2,rely=0.5)
rbt_mult = Button(ventana, text="MULT",command=multiplicacion).place(relx=0.4,rely=0.5)
rbt_borrar = Button(ventana, text=" C ",command=borrar,width=5, height=4).place(relx=0.6,rely=0.5)
rbt_div = Button(ventana, text="DIVISION", command=division).place(relx=0.2,rely=0.6)
rbt_rest = Button(ventana, text="RESTA",command=resta).place(relx=0.4,rely=0.6)

ventana.mainloop()




