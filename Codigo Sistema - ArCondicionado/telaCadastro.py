from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from dateutil.relativedelta import relativedelta
import datetime as dt
import random as rd
import os
import datetime
import subprocess
import sqlite3 as sql3
from babel.numbers import * 
import bd_cadastroZero as bd
from tkinter.simpledialog import askstring
#--------------------------------------------------------------
img_path = os.path.join(os.getcwd(), 'imagens')
cadastro_path = os.path.join(os.getcwd(), 'CadrastoZero.db')
#--------------------------------------------------------------
# Criando Janela
janela = Tk()
janela.title('Zero Grau')
janela.geometry('870x580')
janela.resizable(width= False, height= False)

# Criando Frames
frameCima= Frame(janela, width=1310, height=50, bg='#FFFFFF')
frameCima.grid(row= 0, column=0)

frameMeio= Frame(janela, width=1310, height=250, bg='white', pady= 20)
frameMeio.grid(row= 1, column=0, pady=2, padx=0)

frameBaixo= Frame(janela, width=700, height=280, bg='white', pady= 20)
frameBaixo.place(x=0 , y=300)
#-------------------------------------------------------
s= ttk.Style()
#('clam', 'alt', 'default', 'classic')
s.theme_use('clam')
# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', font=('Calibri', 14,'bold'), background="white")
s.configure('Treeview', font=('Calibri', 13,'bold'))
#--------------------------------------------------

def expirados():
    
    global expirados2
    try:

        con = sql3.connect(cadastro_path)

        with con:
            # Criando um cursor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando Lista Vazia para Armazenar os Dados
            expirados= []

            # Criando outra sentença SQL para selecionar registros
            sql_select = 'select * from usuarios' 

            # Seleciona todos os registros 
            cursor.execute(sql_select)

            # recupera os registros
            selectDados = cursor.fetchall()

            # Mostra
            for linha in selectDados:

                prox_limpeza = linha[5]
                data_armazenada = datetime.datetime.strptime(prox_limpeza, '%d-%m-%Y').date()
                data_atual = datetime.date.today()
                                          
                if data_atual >= data_armazenada:
                   expirados.append(linha)

                   
        return expirados

    except Exception as err:
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err) 

def logoff():

    janela.destroy()
    messagebox.showinfo('Sucesso','Fazendo Logoff')
    subprocess.run("Zero Grau.exe")

def gerar_relatorio():

        pergunta = messagebox.askyesno('Aviso', 'Você deseja gerar um relatorio?')

        if pergunta == True:

            bd.gerar_relatorio()

def matricula():
    
    limpar_campos()

    matricula = e_matricula.get()
    bt_consultar.configure(state= 'disabled')
    bt_sair.configure(state= 'disabled')    
    bt_expirados.configure(state= 'disable')
    bt_consultarnome.configure(state= 'disabled')
    bt_atualizar.configure(state= 'disabled')
    bt_relatorio.configure(state='disabled')
    bt_financeiro.configure(state= 'disable')
    bt_excluir.configure(state= 'disabled')
    e_consultarnome.configure(state= 'disabled')
    bt_adicionar.configure(state= 'normal')
    bt_cancel_cad.configure(state= 'normal')
    #sorteia um numero de 0 ate 10,000
    matricula = e_matricula.get()
    mat = rd.randrange(10000)
        
    e_matricula.insert(0,mat)

    i = len(matricula)
            
    if(i == 0):
        bt_matricula.configure(state= 'disabled') 

def limpar_campos():
    
    e_matricula.delete(0,'end')
    e_nome.delete(0,'end')
    e_whatsapp.delete(0,'end')
    e_endereco.delete(0,'end')
    e_consultarnome.delete(0,'end')
    e_calendario.delete(0,'end')
    e_calendario2.delete(0,'end')
    
def bt_normal():
    bt_sair.configure(state= 'normal')
    bt_limpar.configure(state= 'normal')
    bt_expirados.configure(state= 'normal')
    bt_matricula.configure(state= 'normal')
    bt_financeiro.configure(state= 'normal')
    bt_consultar.configure(state= 'normal')
    bt_consultarnome.configure(state= 'normal')
    bt_atualizar.configure(state= 'normal')
    bt_excluir.configure(state= 'normal')
    bt_relatorio.configure(state='normal')
    e_consultarnome.configure(state= 'normal')

def cancelar_cadastro():
    
    messagebox.showerror('Cancelado','Cadastro Cancelado!')
    limpar_campos()
    bt_normal()
    botão_desativado()
    return

def area_financeira():
    try:
        senha = askstring('Admin', 'Senha', show='*')
        
        if senha == 'zero': 
            janela.destroy()
            import telaFinanceira
            #messagebox.showinfo('Sucesso','Sucesso')

        else:
            messagebox.showerror('Erro','Login ou Senha Invalidos')
            return
    except Exception as err:
        messagebox.showerror('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)      

def login():   

    matricula = e_matricula.get()
    nome = e_nome.get()
    whatsapp = e_whatsapp.get()
    endereco = e_endereco.get()
    data_limpeza = e_calendario.get()
    prox_limpeza = e_calendario2.get() 
    
    data = dt.datetime.now()
    data_cad = data.strftime("%d/%m/%Y")  
            
#--------------------------------------------------   
    # Criando Lista
    lista_inserir= [matricula, nome, whatsapp, endereco,  data_limpeza, prox_limpeza, data_cad]
    lista_matricula = [matricula]
    
    for i in lista_matricula:
        if i=='':
            messagebox.showerror('Erro','Para Cadastrar é necessario a MATRICULA !')
            bt_normal() 
            botão_desativado()
            return
        
    for i in lista_inserir:

        if i=='':
            messagebox.showerror('Erro','Favor Inserir os dados!')
            #limpar_campos()
            #bt_normal()
            #botão_desativado()
            return

    bd.inserirDados(lista_inserir)
    limpar_campos()
    bt_normal()
    botão_desativado()
    consultarGeral()

def consultar_expirados():
    
    global tree 
    
    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço','Data Limpeza', 'Prox Limpeza','Data Cadastro']

    # Função Select do Banco de Dados
    
    lista = expirados()

    if lista == []:
        messagebox.showerror('Erro','Não existe nenhuma data Expirada!')
    
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=15)

    hd=["center","center","center","center","center","center","center","center"]
    h=[100,100,100,110,130,130,180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista:
        tree.insert('', 'end', values=item)

def consultarGeral():
    
    global tree 
    
    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço','Data Limpeza', 'Prox Limpeza','Data Cadastro']

    # Função Select do Banco de Dados
    
    lista_itens = bd.selectAll()

    if lista_itens == []:
        messagebox.showerror('Erro','No momento não tem ninguém a ser Consultado!')

    #print(lista_itens)
    
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=15)

    hd=["center","center","center","center","center","center","center","center"]
    h=[100,100,100,110,130,130,180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

def mostrarTabela():

    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço','data Limpeza', 'Prox Limpeza',"Data Cadastro"]

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=15)

    hd=["center","center","center","center","center","center","center","center"]
    h=[100,100,100,110,130,130,180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1
        
def consultarMat():      
    nome = e_consultarnome.get() 
    
    if nome =='':
        messagebox.showerror('Erro','Favor Preencher os Campos')
        return
        
    nome = str(e_consultarnome.get())
   
    # Chamar a Função Limpar os Campos
    limpar_campos()
    bt_normal() 
    
    # Chamar a Função Mostrar Tabela
    consultar_nome(nome)
    
def consultar_nome(nome):
    
    global tree 
    
    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço','data Limpeza', 'Prox Limpeza',"Data Cadastro"]

    # Função Select do Banco de Dados
    
    lista_itens = bd.selectnome(nome)
    
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=15)

    hd=["center","center","center","center","center","center","center","center"]
    h=[100,100,100,110,130,130,180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)
        
def carregar_dados(lista):
    bt_matricula.configure(state= 'disabled')
    e_matricula.insert(0,lista[0])
    e_nome.insert(0,lista[1])
    e_whatsapp.insert(0,lista[2])
    e_endereco.insert(0,lista[3])
    e_calendario.insert(0,lista[4])
    e_calendario2.insert(0,lista[5])

def atualizar():
    try:
        limpar_campos()
        bt_consultarnome.configure(state= 'disable')
        bt_adicionar.configure(state= 'disable')
        bt_financeiro.configure(state= 'disable')
        bt_atualizar.configure(state= 'disable')
        bt_sair.configure(state= 'disable')
        bt_limpar.configure(state= 'disable')
        bt_expirados.configure(state= 'disable')
        bt_consultar.configure(state= 'disable')
        bt_relatorio.configure(state='disable')
        bt_excluir.configure(state= 'disable')
        e_consultarnome.configure(state= 'disable')
        foco= tree.focus()
        focoItem= tree.item(foco)
        focoLista= focoItem['values']

        carregar_dados(focoLista)     
            
        def cancelar_atualizacao():
            messagebox.showerror('Erro','Atualização Cancelada.')
            bt_confirmarAtt.destroy()
            bt_cancelarAtt.destroy()          
            limpar_campos()
            bt_normal()
            botão_desativado()
            return

        def confirmar_atualizacao(): 

            matricula = e_matricula.get()
            nome = e_nome.get()
            whatsapp = e_whatsapp.get()
            endereco = e_endereco.get()
            prox_limpeza = e_calendario2.get()
            data_limpeza = e_calendario.get()
                
            lista_atualizar= [nome,whatsapp,endereco,data_limpeza,prox_limpeza,matricula]
            lista_atualizar2 = [nome,whatsapp,endereco,matricula,data_limpeza]

            for i in lista_atualizar2:
                    if i=='':
                        messagebox.showerror('Erro','Favor Preencher os Campos')
                        return
                    
            bd.updateDados(lista_atualizar)

            limpar_campos()
            bt_normal()

            consultar_nome(matricula)
        
            bt_confirmarAtt.destroy()
            bt_cancelarAtt.destroy()

            limpar_campos()
            bt_normal()

        bt_confirmarAtt= Button(frameMeio, width=176,image = img03, text='Confirmar Atualização',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= confirmar_atualizacao)
        bt_confirmarAtt.place(x=20, y=200)

        bt_cancelarAtt= Button(frameMeio, width=176,image = img03, text='Cancelar Atualização',compound= LEFT, anchor= CENTER, fg='black', bg='white',command = cancelar_atualizacao)
        bt_cancelarAtt.place(x=199, y=200)
        
    except Exception as err:
            messagebox.showerror('Erro','Favor Selecionar Um Aluno')
            bt_consultarnome.configure(state= 'normal')
            bt_financeiro.configure(state='normal')
            bt_adicionar.configure(state= 'normal')
            bt_sair.configure(state= 'normal')
            bt_limpar.configure(state= 'normal')
            bt_expirados.configure(state= 'normal')
            bt_atualizar.configure(state= 'normal')
            bt_consultar.configure(state= 'normal')
            bt_excluir.configure(state= 'normal')
            e_consultarnome.configure(state= 'normal')
            bt_relatorio.configure(state='normal')
            bt_matricula.configure(state='normal')
            botão_desativado()
            return  
        
def deletar():
    try:
        foco = tree.focus()
        focoItem= tree.item(foco)
        focoLista= focoItem['values']

        pergunta = messagebox.askyesno('Aviso', 'Você Deseja Apagar este Usuario?')

        if pergunta == True:

            matricula = int(focoLista[0])     

            bd.deleteDados(matricula)
            consultarGeral()
            limpar_campos()
            bt_normal()  

        else:
            return
    except:
        messagebox.showerror('Erro','Para excluir um usuario é necessario seleciona-lo!')
        return
    
def botão_desativado():
    bt_adicionar.configure(state= 'disabled')
    bt_cancel_cad.configure(state= 'disabled')

#-------------------------------------------------------

# Criando Logo
img00 = Image.open(os.path.join(img_path,'Logo_ZeroGrau2.png'))
img00 = img00.resize((250, 250))
img00 = ImageTk.PhotoImage(img00)

lb_logo = Label(frameCima, padx=10, width=1045,image = img00,compound=LEFT, anchor=NW,bg='white')
lb_logo.place(x=305, y=-80)

img01 = Image.open(os.path.join(img_path,'Logo_ZeroGrau.png'))
img01 = img01.resize((220, 220))
img01 = ImageTk.PhotoImage(img01)

lb_logo = Label(frameMeio, padx=10, width=1045,image = img01,compound=LEFT, anchor=NW,bg='white')
lb_logo.place(x=650, y=-20)

janela.iconbitmap(os.path.join(img_path,'floconeve2.ico'))
#--------------------------------------------------------

lb_matricula =Label(frameMeio, font=('bold'), text='Matrícula',bg='#FFFFFF', fg='black')
lb_matricula.place(x=10, y=10)
e_matricula= Entry(frameMeio, width=10)
e_matricula.place(x=90, y=11)

img02 = Image.open(os.path.join(img_path,'floconeve.png'))
img02 = img02.resize((20, 20))
img02 = ImageTk.PhotoImage(img02)

bt_matricula= Button(frameMeio, width=130,image = img02, text='Gerar Matrícula',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= matricula)
bt_matricula.place(x=160, y=8)

lb_nome =Label(frameMeio, font=('bold'), text='Nome',bg='#FFFFFF', fg='black')
lb_nome.place(x=10, y=50)
e_nome= Entry(frameMeio, width=40)
e_nome.place(x=90, y=51)

lb_whatsapp =Label(frameMeio, font=('bold'), text='Whatsapp',bg='#FFFFFF', fg='black')
lb_whatsapp.place(x=10, y=90)
e_whatsapp= Entry(frameMeio, width=40)
e_whatsapp.place(x=101, y=91)

lb_endereco =Label(frameMeio, font=('bold'), text='Endereço',bg='#FFFFFF', fg='black')
lb_endereco.place(x=10, y=130)
e_endereco= Entry(frameMeio, width=40)
e_endereco.place(x=101, y=131)

img03 = Image.open(os.path.join(img_path,'floconeve.png'))
img03 = img03.resize((20, 20))
img03 = ImageTk.PhotoImage(img03)

bt_adicionar= Button(frameMeio, width=100,image = img03, text='Cadastrar',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= login)
bt_adicionar.place(x=396, y=8)

bt_cancel_cad= Button(frameMeio, width=125,image = img03, text='Cancelar Cadastro',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= cancelar_cadastro)
bt_cancel_cad.place(x=520, y=8)

bt_relatorio= Button(frameCima, width=125,image = img03, text='Gerar Relatorio',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=gerar_relatorio)
bt_relatorio.place(x=10, y=10)
                
bt_consultar= Button(frameMeio, width=100,image = img03, text='Consultar',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= consultarGeral)
bt_consultar.place(x=396, y=50)

bt_atualizar= Button(frameMeio, width=95,image = img03, text='Atualizar',compound= LEFT, anchor= CENTER, fg='black', bg='white',command = atualizar)
bt_atualizar.place(x=20, y=200)

bt_expirados= Button(frameMeio, width=125,image = img03, text='Consultar Expirados',compound= LEFT, anchor= CENTER, fg='black', bg='white',command =  consultar_expirados)
bt_expirados.place(x=520, y=50)

bt_excluir= Button(frameMeio, width=95,image = img03, text='Excluir',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= deletar)
bt_excluir.place(x=130, y=200)

bt_limpar= Button(frameMeio, width=125,image = img03, text='Limpar Campos',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= limpar_campos)
bt_limpar.place(x=240, y=200)

bt_sair= Button(frameCima, width=95,image = img03, text='Sair',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=logoff)
bt_sair.place(x=590, y=10)

bt_financeiro= Button(frameCima, width=120,image = img03, text='Área Financeira',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=area_financeira)
bt_financeiro.place(x=700, y=10)
                
bt_consultarnome= Button(frameMeio, width=130,image = img03, text='Consultar Nome',compound= LEFT, anchor= CENTER, fg='black', bg='white',command =  consultarMat)
bt_consultarnome.place(x=537, y=200)
e_consultarnome= Entry(frameMeio, width=20)
e_consultarnome.place(x=690, y=201)

lb_calendario =Label(frameMeio, font=('bold'), text='Data Limpeza', bg='#FFFFFF', fg='black')
lb_calendario.place(x=5, y=170)
e_calendario= DateEntry(frameMeio, width=15, date_pattern='dd-mm-y')
e_calendario.place(x=120, y=171)

lb_calendario2 =Label(frameMeio, font=('bold'), text='Próxima Limpeza', bg='#FFFFFF', fg='black')
lb_calendario2.place(x=250, y=170)
e_calendario2= DateEntry(frameMeio, width=15, date_pattern='dd-mm-y')
e_calendario2.place(x=390, y=171)

limpar_campos()
bt_normal()
mostrarTabela()
botão_desativado()
janela.mainloop()