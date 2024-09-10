from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import os
# Criptografar Senha
from hashlib import sha256
import bd_cadastroZero as bd
import datetime as dt

img_path = os.path.join(os.getcwd(), 'imagens')
#-------------------------------------------------------------
#------------------- JANELA ---------------------------------------
# Criando Janela

cor_fundo = "white"
cor_letra = "black"

janela = Tk()
janela.title('Zero Grau')
janela.geometry('600x350')
janela.config(bg=cor_fundo)
janela.resizable(width= False, height= False)
#-------------------------------------------------------------
# Criando Frames
frameCima= Frame(janela, width=800, height=50, bg=cor_fundo)
frameCima.grid(row= 0, column=0)

frameMeio= Frame(janela, width=800, height=340, bg=cor_fundo, pady= 20)
frameMeio.grid(row= 1, column=0, pady=2, padx=0)
#-------------------------------------------------------------
img_path = os.path.join(os.getcwd(), 'imagens')
#-------------------------------------------------------------
def tela():

    login= e_login.get()
    senha= e_senha.get() 
    hash_senha= sha256(senha.encode()).digest()
    
    # Criando Lista
    lista_login= [login,hash_senha]
        
    for i in lista_login:
        if i=='':
            messagebox.showerror('Erro','Favor Preencher os Campos')
            return

    lista=[]  
    lista= bd.selectLogin(lista_login)
    i= len(lista)
    if(i > 0):
        messagebox.showinfo('Bem Vindo',login)
        janela.destroy()
        import telaCadastro
    else:
        messagebox.showerror('Erro','Login ou Senha Invalidos')
        limpar_campos()
        return  

def cadastrar():
    try:
        senha = askstring('Admin', 'Senha', show='*')
        
        if senha == 'Admin':

            limpar_campos()
            bt_login.configure(state= 'disabled')         
            bt_cadastrar.configure(state='normal')
            bt_cancel_cad.configure(state='normal')

        else:
            messagebox.showerror('Erro','Login ou Senha Invalidos')

    except Exception as err:
        messagebox.showerror('Erro', err)

def cancel_cad():

    limpar_campos()
    bt_cadastrar.configure(state='disabled')
    bt_cancel_cad.configure(state='disabled')
    bt_login.configure(state='normal')
    messagebox.showinfo('Cancelado','Cadastro Cancelado')
    return

def login(): 
      
    login= e_login.get()
    senha= e_senha.get()                
    data= dt.datetime.now()
    data_cad = data.strftime("%d/%m/%Y")        

    hash_senha= sha256(senha.encode()).digest()

    lista_inserir= [login, hash_senha, data_cad]

    for i in lista_inserir:
        if i=='':
            messagebox.showinfo('Bem Vindo','Favor Inserir: Login, Senha')
            return

    if len(login) and len(senha) > 2:
        if len(senha) and len(login) > 2:

            bd.inserirLogin(lista_inserir)
                
            limpar_campos() 
            bt_login.configure(state= 'normal') 
            bt_cadastrar.configure(state= 'disabled')
            bt_cancel_cad.configure(state='disabled')
                    
        else:
            messagebox.showerror('Erro','A Senha e o Login tem que ter no minimo 3 digitos')
            limpar_campos() 
    else:
            messagebox.showerror('Erro','A Senha e o Login tem que ter no minimo 3 digitos')
            limpar_campos()        
     
def limpar_campos():
    e_login.delete(0,'end')
    e_senha.delete(0,'end')       

def sair():
    messagebox.showinfo('Logout','Sair')
    janela.destroy()

#----------------------------------LOGO-------------------------------------------------------------------------------- 

img02 = Image.open(os.path.join(img_path,'floconeve.png'))
img02 = img02.resize((150, 150))
img02 = ImageTk.PhotoImage(img02)

lb_logo = Label(frameMeio, padx=10, width=1045,image = img02,compound=LEFT, anchor=NW,bg=cor_fundo)
lb_logo.place(x=380, y=60)

img00 = Image.open(os.path.join(img_path,'Logo_ZeroGrau2.png'))
img00 = img00.resize((250, 250))
img00 = ImageTk.PhotoImage(img00)

lb_logo = Label(frameCima, padx=10, width=1045,image = img00,compound=LEFT, anchor=NW,bg=cor_fundo)
lb_logo.place(x=200, y=-80)

janela.iconbitmap(os.path.join(img_path,'floconeve2.ico'))
#-------------------------------------------------------------
lb_login =Label(frameMeio, height=2, text='Login',font=("bold"),bg=cor_fundo, fg=cor_letra)
lb_login.place(x=10, y=30)
e_login= Entry(frameMeio, width=30)
e_login.place(x=72, y=41)

lb_senha =Label(frameMeio, height=2, text='Senha',font=("bold"),bg=cor_fundo, fg=cor_letra)
lb_senha.place(x=6, y=75)
e_senha= Entry(frameMeio, width=30,show='*')
e_senha.place(x=70, y=86)

img03 = Image.open(os.path.join(img_path,'floconeve.png'))
img03 = img03.resize((25, 25))
img03 = ImageTk.PhotoImage(img03) 

bt_login= Button(frameMeio,image=img03, width=95, text='Login',compound= LEFT, anchor= CENTER, fg=cor_letra, bg=cor_fundo,command=tela)
bt_login.place(x=10, y=130)

img04 = Image.open(os.path.join(img_path,'floconeve.png'))
img04 = img04.resize((25, 25))
img04 = ImageTk.PhotoImage(img04) 

img05 = img05 = Image.open(os.path.join(img_path,'floconeve.png'))
img05 = img05.resize((25, 25))
img05 = ImageTk.PhotoImage(img05)

bt_admin= Button(frameMeio,image=img05, width=125, text='Administrador',compound= LEFT, anchor= CENTER, fg=cor_letra, bg=cor_fundo,command= cadastrar)
bt_admin.place(x=350, y=-20)

img06 = Image.open(os.path.join(img_path,'floconeve.png'))
img06 = img06.resize((25, 25))
img06 = ImageTk.PhotoImage(img06)

bt_deletar= Button(frameMeio,image=img06, width=95, text='Sair',compound= LEFT, anchor= CENTER, fg=cor_letra, bg=cor_fundo,command=sair)
bt_deletar.place(x=490, y=-20)

bt_cadastrar= Button(frameMeio,image=img04, width=95, text='Cadastrar',compound= LEFT, anchor= CENTER, fg=cor_letra, bg=cor_fundo,command=login)
bt_cadastrar.place(x=140, y=130)
bt_cadastrar.configure(state='disabled')
    
bt_cancel_cad = Button(frameMeio,image=img04, width=125, text='Cancelar Cadastro',compound= LEFT, anchor= CENTER, fg=cor_letra, bg=cor_fundo,command=cancel_cad)
bt_cancel_cad.place(x=60, y=180)
bt_cancel_cad.configure(state='disabled')
janela.mainloop()
