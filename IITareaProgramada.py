from Tkinter import *  
from pyswip import * #Se importa de la libreria pyswip 
from tkMessageBox import *


global p
p=Prolog()


class main:
     
    #constructor de la clase
    def __init__(self,master):

        #Imagenes de Fondo
        self.start_background=PhotoImage(file="Imagenes/Background_start.gif")
        self.addkid_background=PhotoImage(file="Imagenes/Background_addkid.gif")
        self.addgiftbackg= PhotoImage(file="Imagenes/Background_addgift.gif")
        self.consultbackg= PhotoImage(file="Imagenes/Background_consult.gif")
        self.background=PhotoImage(file='Imagenes/whitebkg.gif') 

        #Imagenes de Botones
        self.img_start=PhotoImage(file="Imagenes/b_start.gif")
        self.img_addkid=PhotoImage(file="Imagenes/b_addkid.gif")
        self.img_consult=PhotoImage(file="Imagenes/b_consult.gif")   
        self.img_addgift= PhotoImage(file="Imagenes/b_addgift.gif")
        self.img_add=PhotoImage(file="Imagenes/b_add.gif")
        self.img_doconsult=PhotoImage(file="Imagenes/b_doconsult.gif")
        self.img_bnyml=PhotoImage(file="Imagenes/b_bnyml.gif")
        self.img_cash=PhotoImage(file="Imagenes/b_cash.gif")
        self.img_rgpop=PhotoImage(file="Imagenes/b_rgpop.gif")

        
        p.assertz('(fun(X):-car(X),red(X))')
        p.assertz('car(ferrari)')
        p.assertz('red(ferrari)')

        print list(p.query('member(X,[2,1,3])'))


        print list(p.query('fun(X)'))
        
        

        #Se llama a la ventana principal 
        self.main_window() 
        
    # ventana principal
    def main_window(self):
        root.geometry("1000x655") #tamano de la ventana
        self.lbbackground=Label(root, image=self.background).place(x=0,y=0) 
        self.lb1=Label(root,image=self.start_background,bg='white').place(x=0,y=67) 
        self.but1=Button(root,image=self.img_start,command=self.main_window).place(x=0,y=0)
        self.but1=Button(root,image=self.img_addkid,bg='white',command=self.window_addkid).place(x=256,y=0)
        self.but2=Button(root,image=self.img_addgift,bg='white',command=self.window_addgift).place(x=512,y=0)
        self.but3=Button(root,image=self.img_consult,bg='white',command=self.window_consult).place(x=768,y=0)
        if not self: root.quit()  


#===========================================
    # Funcion para obtener datos del entry e ingresar animales a la BC
    def ing_nino(self):
        self.nombre = (self.entry_nino_nbr.get()).replace(" ","_")
        self.edad = self.entry_edad.get()
        self.pais = (self.entry_pais.get()).replace(" ","_")
        self.buenas_acc = (self.entry_buenas_acc.get()).replace(" ","")
        self.malas_acc = (self.entry_malas_acc.get()).replace(" ","")
        self.wishlist = (self.entry_wishlist.get()).replace(" ","")
        self.presupuesto= self.entry_presupuesto.get()
        
        self.nombre = self.nombre.lower()
        self.edad = self.edad.lower()
        self.pais = self.pais.lower()
        self.buenas_acc = self.buenas_acc.lower()
        self.malas_acc= self.malas_acc.lower()
        self.wishlist = self.wishlist.lower()
        
        if ((self.nombre!= "") and (self.edad!="") and (self.pais!="") and (self.buenas_acc !="") and (self.malas_acc!="") and (self.wishlist!="") and (self.presupuesto!="")):       #El entry de raza no debe ser vacio
            showinfo("Nuevo nino", "Se ha anadido un nuevo nino a la base de conocimientos")
            self.entry_nino_nbr.delete(0, END)   #Se limpian todos los entry cuando ya guarda el contacto
            self.entry_edad.delete(0, END)
            self.entry_pais.delete(0,END)
            self.entry_buenas_acc.delete(0, END)
            self.entry_malas_acc.delete(0, END)
            self.entry_wishlist.delete(0, END)
            self.entry_presupuesto.delete(0,END)
            return self.save_cont_n(self.nombre, self.edad, self.pais, self.buenas_acc, self.malas_acc,self.wishlist,self.presupuesto) #Guarda el contenido q se ingresa 

        else:
            showwarning("Error", "ERROR: Por favor ingrese todos los datos.")

    def ing_regalo(self):
        self.juguete = (self.entry_juguete.get()).replace(" ","_")
        self.marca = (self.entry_marca.get()).replace(" ","_")
        self.precio = self.entry_precio.get()
        self.edadlim = self.entry_edadlim.get()

        self.juguete = self.juguete.lower()
        self.marca = self.marca.lower()
        self.precio = self.precio.lower()
        self.edadlim = self.edadlim.lower()
        
        if ((self.juguete!= "") and (self.marca!="") and (self.precio!="") and (self.edadlim !="")):       #El entry de raza no debe ser vacio
            showinfo("Nuevo Juguete!", "Se ha anadido el juguete a la base de conocimientos")
            self.entry_juguete.delete(0, END)   #Se limpian todos los entry cuando ya guarda el contacto
            self.entry_marca.delete(0, END)
            self.entry_precio.delete(0,END)
            self.entry_edadlim.delete(0, END)
            
            return self.save_cont_j(self.juguete, self.marca, self.precio, self.edadlim) 

        else:
            showwarning("Error", "ERROR: Por favor ingrese todos los datos.")

#====================================================================================


    # Funcion que inserta los animales a la base de conocimiento en Prolog y ademas crea un txt como respaldo de los animales ingresados 
    def save_cont_j(self,juguete, marca, precio, edadlim):     
        assertz = Functor("assertz", 1)
        regalo = Functor("regalo", 4)
        call(assertz(regalo(self.juguete,self.marca,self.precio,self.edadlim)))
        print list(p.query('regalo(A,B,C,D)'))
        
        try:        
            infousuario=("juguete("+self.juguete,self.marca,self.precio,self.edadlim+").")
            info=open("Base_Conocimiento.pl","r")              
            info=open("Base_Conocimiento.pl","a") #Abre la informacion guardada del txt
            info.write(",".join(infousuario)+"\n")
            info.close()
           

        except IOError:     #Creacion del archivo si no esta creado
            info=open("Base_Conocimiento.pl","w")
            info.write(",".join(infousuario)) # Separa la informacion por comas
            self.save_cont_j(self.juguete, self.marca, self.precio, self.edadlim)
            info.close()

#====================================================================================

    # Funcion que inserta los animales a la base de conocimiento en Prolog y ademas crea un txt como respaldo de los animales ingresados 
    def save_cont_n(self,nombre, edad, pais, buenas_acc, malas_acc, wishlist, presupuesto):     
        assertz = Functor("assertz", 1)
        nino = Functor("nino", 3)
        call(assertz(nino(self.nombre,self.edad,self.pais,self.buenas_acc,self.malas_acc,self.wishlist,self.presupuesto)))
        print list(p.query('nino(A,B,C,D,E,F,G)'))
        try:        
            infousuario=("nino("+self.nombre,self.edad,self.pais,self.buenas_acc,self.malas_acc,self.wishlist,self.presupuesto+").")
            info=open("Base_Conocimiento.pl","r")              
            info=open("Base_Conocimiento.pl","a") #Abre la informacion guardada del txt
            info.write(",".join(infousuario)+"\n")
            info.close()

        except IOError:     #Creacion del archivo si no esta creado
            info=open("Base_Conocimiento.pl","w")
            info.write(",".join(infousuario)) # Separa la informacion por comas
            self.save_cont_n(self.nombre, self.edad, self.pais, self.buenas_acc,self.malas_acc,self.wishlist,self.presupuesto)
            info.close()



#==================================================================================

    def consult_bnyml(self):

        X=Variable()
        Bn=Variable()
        Ml=Variable()
        _=Variable()
        q=Query(nino(X,_,_,Bn,Ml,_,_))

        w_consult = Toplevel()
        w_consult.resizable(width=NO,height=NO)
        w_consult.title("Consulta")
        w_consult.geometry('570x600')
        self.scrl = Scrollbar(ventconsulta)
        self.T = Text(ventconsulta)
        self.T.focus_set()
        self.scrl.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.scrl.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.s.set)
        self.T.insert(END, "Ninos Buenos\n")
        
        while q.nextSolution():
            bn=str(Bn.value).split(",")
            ml=str(Ml.value).split(",")
            if len(bn)>len(ml):
                self.T.insert(END, "\n"+str(X.value))

        self.T.insert(END, "Ninos Malos\n")
        
        while q.nextSolution():
            bn=str(Bn.value).split(",")
            ml=str(Ml.value).split(",")
            if len(bn)<len(ml):
                self.T.insert(END, "\n"+str(X.value))

        
        q.closeQuery()
        w_consult.mainloop()


#==================================================================================


    # Ventana para ingresar regalos
    def window_addgift(self):
       
        root.geometry("1000x655") 
        self.lbbackground=Label(root, image=self.background).place(x=0,y=67) 
        self.lb1=Label(root,image=self.addgiftbackg,bg='white').place(x=0,y=67) 
        
        self.lb_juguete_nmbr = Label (root, text= "Nombre", bg = "orange",fg = 'black', borderwidth = 0, font = ('Century Gothic',15))
        self.lb_juguete_nmbr.place(x=350,y=220)
        self.entry_juguete = Entry (root, width=22, bg = "white",fg = 'black',font=("consolas", 15))
        self.entry_juguete.place(x=480,y=220)
        
        self.lb_marca = Label(root, text= "Marca", bg = "orange",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_marca.place(x=350,y=260)
        self.entry_marca = Entry (root, width=22, bg = "white",fg = 'black',font=("consolas", 15))
        self.entry_marca.place(x=480,y=260)
        
        self.lb_precio = Label(root, text= "Precio", bg = "orange",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_precio.place(x=350,y=300)
        self.entry_precio = Entry (root, width=22, bg = "white",fg = 'black',font=('consolas',15))
        self.entry_precio.place(x=480,y=300)
        
        self.lb_edadlim = Label(root, text= "Edad", bg = "orange",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_edadlim.place(x=350,y=340)
        self.entry_edadlim = Entry (root, width=22, bg = "white",fg = 'black',font=('Consolas',15))
        self.entry_edadlim.place(x=480,y=340)
        
        
        self.b_ing_j = Button(root, image= self.img_add,cursor = "hand2", command = self.ing_regalo).place(x=100,y=560)



    # Ventana de ingreso
    def window_addkid(self):
       
        root.geometry("1000x655") #Tamano estandar de la raiz
        self.lbbackground=Label(root, image=self.background).place(x=0,y=67) #Fondo blanco para tapar
        self.lb1=Label(root,image=self.addkid_background,bg='white').place(x=0,y=67) #Posicion del logo
        
        self.lb_nino_nbr = Label (root, text= "Nombre", bg = "#FF6633",fg = 'black', borderwidth = 0, font = ('Century Gothic',15))
        self.lb_nino_nbr.place(x=350,y=220)
        self.entry_nino_nbr = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas",15))
        self.entry_nino_nbr.place(x=555,y=220)
        
        self.label_edad = Label(root, text= "Edad", bg = "#FF6633",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.label_edad.place(x=350,y=260)
        self.entry_edad = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_edad.place(x=555,y=260)
        
        self.lb_pais = Label(root, text= "Pais", bg = "#FF6633",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_pais.place(x=350,y=300)
        self.entry_pais = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_pais.place(x=555,y=300)
        
        self.lb_buenas_acc = Label(root, text= "Buenas Acciones", bg = "#FF6633",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_buenas_acc.place(x=350,y=340)
        self.entry_buenas_acc = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_buenas_acc.place(x=555,y=340)
        
        self.lb_malas_acc = Label(root, text= "Malas Acciones", bg = "#FF6633",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_malas_acc.place(x=350,y=380)
        self.entry_malas_acc = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_malas_acc.place(x=555,y=380)
        
        self.lb_wishlist = Label(root, text= "Deseos", bg = "#FF6633",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_wishlist.place(x=350,y=420)
        self.entry_wishlist = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_wishlist.place(x=555,y=420)

        
        self.lb_presupuesto = Label(root, text= "Presupuesto", bg = "#FF6633",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_presupuesto.place(x=350,y=460)
        self.entry_presupuesto = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_presupuesto.place(x=555,y=460)
        
        self.b_ing_n = Button(root, image= self.img_add, cursor = "hand2", command = self.ing_nino)
        self.b_ing_n.place(x=100,y=560)


    # Ventana de consultas
    def window_consult(self):
        root.geometry("1000x655") #Tamano estandar de la raiz
        
        self.lbbackground=Label(root, image=self.background).place(x=0,y=67) #Fondo blanco para tapar
        self.lb1=Label(root,image=self.consultbackg,bg='white').place(x=0,y=67) #Posicion del logo

        self.b_bnyml=Button(root,image=self.img_bnyml,bg='white',cursor = "hand2",command = self.consult_bnyml).place(x=40,y=300)

        self.b_cash=Button(root,image=self.img_cash,bg='white').place(x=40,y=390)

        self.b_rgpop=Button(root,image=self.img_rgpop,bg='white').place(x=40,y=480)
        
        self.lb_n_accbn = Label(root, text= "Niños-Acción Buena", bg = "#FF4747",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_n_accbn.place(x=40,y=120)
        self.entry_n_accbn = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_n_accbn.place(x=250,y=120)
        
        self.lb_n_accml = Label(root, text= "Niños-Acción Mala", bg = "#FF4747",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_n_accml.place(x=530,y=120)
        self.entry_n_accml = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_n_accml.place(x=740,y=120)

        
        self.lb_nreg = Label(root, text= "Niño-Regalos", bg = "#FF4747",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_nreg.place(x=40,y=170)
        self.entry_nreg = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_nreg.place(x=250,y=170)
        
        self.lb_nreg_posb = Label(root, text= "Niño-Regalos Posibles", bg = "#FF4747",fg = 'black', borderwidth = 0,  font = ('Century Gothic',15))
        self.lb_nreg_posb.place(x=530,y=170)
        self.entry_nreg_posb = Entry (root, width=22, bg = "white",fg = 'black',font=("Consolas", 15))
        self.entry_nreg_posb.place(x=740,y=170)

        
        self.boton_consultar = Button(root, image= self.img_doconsult ).place(x=40,y=210)


root=Tk()
root.resizable(width=NO,height=NO)
app=main(root) #Asigna un espacio de memoria para ejecutar la clase
root.title('TALLER DE SANTA') #Nombre de la raiz
root.geometry('1000x655') #Tamano estandar de la raiz
root.mainloop() #Ejecuta la ventana
