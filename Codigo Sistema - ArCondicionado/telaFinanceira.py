from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from dateutil.relativedelta import relativedelta
from datetime import datetime
import datetime as dt
import random as rd
import os
import subprocess
from babel.numbers import * 
import bd_cadastroFinanceiro as bd

#--------------------------------------------------------------
img_path = os.path.join(os.getcwd(), 'imagens')
#--------------------------------------------------------------
# Criando Janela
janela = Tk()
janela.title('Zero Grau')
janela.geometry('1300x620')
janela.resizable(width= False, height= False)

# Criando Frames
frameCima= Frame(janela, width=1310, height=50, bg='#FFFFFF')
frameCima.grid(row= 0, column=0)

frameMeio= Frame(janela, width=1310, height=650, bg='white', pady= 20)

frameMeio.grid(row= 1, column=0, pady=2, padx=0)

frameBaixo= Frame(janela, width=190, height=950, bg='white', pady= 20)
frameBaixo.place(x=0,y=320)

#-------------------------------------------------------
s= ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading', font=('Calibri', 13,'bold'), background="white")
s.configure('Treeview', font=('Calibri', 13,'bold'))
s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
#--------------------------------------------------
def logoff():

    janela.destroy()
    messagebox.showinfo('Sucesso','Fazendo Logoff')
    subprocess.run("Zero Grau.exe")

def gerar_relatorio():

        pergunta = messagebox.askyesno('Aviso', 'Você deseja gerar um relatorio?')

        if pergunta == True:
            bd.gerar_relatorio() 

def matricula():

    mostrarTabela()
    limpar_campos()
    matricula = e_matricula.get()

    bt_consultar.configure(state= 'disabled')
    bt_sair.configure(state= 'disable')
    e_consultarnome.configure(state='disabled')
    bt_consultarnome.configure(state= 'disabled')
    bt_consultarmat.configure(state= 'disabled')
    bt_atualizar.configure(state= 'disabled')
    bt_relatorio.configure(state='disabled')
    bt_excluir.configure(state= 'disabled')
    e_consultarmat.configure(state= 'disabled')
    bt_adicionar.configure(state= 'normal')
    bt_cancel_cad.configure(state= 'normal')

    #sorteia um numero de 0 ate 10,000
    matricula = e_matricula.get()
    mat = rd.randrange(10000)
        
    e_matricula.insert(0,mat)

    i = len(matricula)
            
    if(i == 0):
        bt_matricula.configure(state= 'disabled') 

def login():  
    calculo()   
    matricula = e_matricula.get()
    nome = e_nome.get()
    whatsapp = e_whatsapp.get()
    endereco = e_endereco.get()
    descricao_servico = e_desc_servico.get()
    preco_final = e_preco_final.get()
    servico = combo_serv.get()
    pagamento = combo_pag.get()
    marca_ar = combo_Ar.get()
    materiais_usados = e_mat_usados.get()
    data = dt.datetime.now()
    data_cad = data.strftime("%d/%m/%Y")
    lucro = e_lucro.get()
    gasto = e_gasto.get()  
#--------------------------------------------------   
    # Criando Lista
    lista_inserir= [matricula, nome, whatsapp, endereco, servico, descricao_servico,materiais_usados,pagamento,lucro,gasto,preco_final,marca_ar, data_cad]
    lista_inserir2= [matricula, nome, whatsapp, endereco, servico, descricao_servico,materiais_usados,pagamento,gasto,preco_final,marca_ar, data_cad]
    lista_matricula = [matricula]
    
    for i in lista_matricula:
        if i=='':
            messagebox.showerror('Erro','Para Cadastrar é necessario a MATRICULA !')
            bt_normal()
            botão_desativado()
            return
        
    for i in lista_inserir2:

        if i=='':
            messagebox.showinfo('Erro','Favor Inserir os dados!')
            #bt_normal()
            #limpar_campos()
            #botão_desativado()
            return
            
    bd.inserirDados(lista_inserir)
    bt_normal() 
    limpar_campos()
    botão_desativado()
    consultarGeral()

def calculo(): 
    try:
        preco_final = e_preco_final.get()
        gasto = e_gasto.get()

        lucro1 = int(preco_final) - int(gasto)

        e_lucro.insert(0,lucro1)

        messagebox.showinfo('Sucesso','Cadastro Realizado com Sucesso')
        messagebox.showinfo('Lucro','Tivemos um lucro de {} Reais com este usuario!'.format(lucro1))
        
    except ValueError:
        #messagebox.showerror('Erro','Digite um numero valido nos campos gasto e Preço final!')
        #bt_normal()
        #limpar_campos()
        return
    
def cancelar_cadastro():
    
    messagebox.showerror('Cancelado','Cadastro Cancelado!')
    bt_normal()
    limpar_campos()
    botão_desativado()

def atualizar():
    try:
        limpar_campos()
        bt_consultarmat.configure(state= 'disable')
        bt_consultarnome.configure(state='disable')
        bt_adicionar.configure(state= 'disable')
        bt_atualizar.configure(state= 'disable')
        bt_consultar.configure(state= 'disable')
        bt_relatorio.configure(state='disable')
        bt_sair.configure(state= 'disable')
        bt_excluir.configure(state= 'disable')
        e_consultarmat.configure(state= 'disable')
        e_consultarnome.configure(state='disable')
        foco= tree.focus()
        focoItem= tree.item(foco)
        focoLista= focoItem['values']

        carregar_dados(focoLista)     
            
        def cancelar_atualizacao():
            messagebox.showerror('Erro','Atualização Cancelada.')
            bt_confirmarAtt.destroy()
            bt_cancelarAtt.destroy() 
            bt_normal()          
            limpar_campos()
            botão_desativado()

        def confirmar_atualizacao(): 

            matricula = e_matricula.get()
            nome = e_nome.get()
            whatsapp = e_whatsapp.get()
            endereco = e_endereco.get()
            descricao_servico = e_desc_servico.get()
            preco_final = e_preco_final.get()
            servico = combo_serv.get()
            pagamento = combo_pag.get()
            marca_ar = combo_Ar.get()
            materiais_usados = e_mat_usados.get()

            lucro = e_lucro.get()
            gasto = e_gasto.get() 
                           
            lista_atualizar= [nome, whatsapp, endereco, servico, descricao_servico, materiais_usados, pagamento, lucro,gasto, preco_final, marca_ar, matricula]
            lista_atualizar2= [nome, whatsapp, endereco, servico, descricao_servico, materiais_usados, pagamento, marca_ar, matricula]

            for i in lista_atualizar2:
                    if i=='':
                        messagebox.showerror('Erro','Favor Preencher os Campos')
                        return
                    
            bd.updateDados(lista_atualizar)
            
            consultar_matricula(matricula)
            bt_confirmarAtt.destroy()
            bt_cancelarAtt.destroy()
            bt_normal()
            limpar_campos()

        bt_confirmarAtt= Button(frameMeio, width=176,image = img03, text='Confirmar Atualização',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= confirmar_atualizacao)
        bt_confirmarAtt.place(x=10, y=220)

        bt_cancelarAtt= Button(frameMeio, width=176,image = img03, text='Cancelar Atualização',compound= LEFT, anchor= CENTER, fg='black', bg='white',command = cancelar_atualizacao)
        bt_cancelarAtt.place(x=194, y=220)

    except Exception as err:
            messagebox.showerror('Erro','Favor Selecionar Um Usuario')
            bt_consultarmat.configure(state= 'normal')
            bt_consultarnome.configure(state='normal')
            bt_adicionar.configure(state= 'normal')
            bt_atualizar.configure(state= 'normal')
            bt_consultar.configure(state= 'normal')
            bt_excluir.configure(state= 'normal')
            bt_sair.configure(state= 'normal')
            e_consultarmat.configure(state= 'normal')
            e_consultarnome.configure(state='normal')
            bt_relatorio.configure(state='normal')
            bt_matricula.configure(state='normal')
            botão_desativado()

def carregar_dados(selectDados):
    bt_matricula.configure(state= 'disabled')
    e_matricula.insert(0,selectDados[0])
    e_nome.insert(0,selectDados[1])
    e_whatsapp.insert(0,selectDados[2])
    e_endereco.insert(0,selectDados[3])
    e_mat_usados.insert(0,selectDados[6])
    e_desc_servico.insert(0,selectDados[5])
    e_lucro.insert(0,selectDados[8])
    e_gasto.insert(0,selectDados[9])
    e_preco_final.insert(0,selectDados[10])
    combo_Ar.insert(0,selectDados[9])
    combo_pag.insert(0,selectDados[7])
    combo_serv.insert(0,selectDados[4])
    
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

        else:
            return
    except:
        messagebox.showerror('Erro','Para excluir um usuario é necessario seleciona-lo!')

def limpar_campos():
    
    e_matricula.delete(0,'end')
    e_consultarnome.delete(0,'end')
    e_nome.delete(0,'end')
    e_whatsapp.delete(0,'end')
    e_endereco.delete(0,'end')
    combo_serv.delete(0,'end')
    e_preco_final.delete(0,'end')
    e_mat_usados.delete(0,'end')
    combo_pag.delete(0,'end')
    combo_Ar.delete(0,'end')
    e_desc_servico.delete(0,'end')
    e_consultarmat.delete(0,'end')
    e_lucro.delete(0,'end')
    e_gasto.delete(0,'end')
   
def bt_normal():

    bt_matricula.configure(state= 'normal')
    bt_sair.configure(state= 'normal')
    bt_consultarnome.configure(state='normal')
    bt_consultar.configure(state= 'normal')
    bt_consultarmat.configure(state= 'normal')
    bt_atualizar.configure(state= 'normal')
    bt_excluir.configure(state= 'normal')
    bt_relatorio.configure(state='normal')
    e_consultarmat.configure(state= 'normal')
    e_consultarnome.configure(state='normal')

def consultarGeral():
    
    global tree 
    
    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço', 'Serviço','Descrição Do Serviço','Materiais Usados','Forma de pagamento', 'Lucro']

    # Função Select do Banco de Dados
    
    lista_itens = bd.selectAll()

    if lista_itens == []:
         messagebox.showerror('Erro','No momento não tem ninguém a ser Consultado!')
    #print(lista_itens)
    
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings",height=11)

    # vertical scrollbar
    
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=1500)

    hd=["center","center","center","center","center","center","center","center","center"]
    h=[100,100,150,140,140,200,150,170,130]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item) 

def consultarMat():      
    matricula1 = e_consultarmat.get() 
    
    if matricula1 =='':
            messagebox.showerror('Erro','Favor Preencher os Campos')
            return
        
    matricula1 = int(e_consultarmat.get())
   
    # Chamar a Função Limpar os Campos
    limpar_campos() 
    
    # Chamar a Função Mostrar Tabela
    consultar_matricula(matricula1) 
    
def consultar_matricula(matricula1):
    
    global tree 
    
    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço', 'Serviço','Descrição Do Serviço','Materiais Usados','Forma de pagamento', 'Lucro']

    # Função Select do Banco de Dados
    
    lista_itens = bd.selectMatricula(matricula1)
    
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings",height=11)

    # vertical scrollbar
    
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=1500)

    hd=["center","center","center","center","center","center","center","center","center"]
    h=[100,100,150,140,140,200,150,170,130]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

def consultarNome():      
    nome = e_consultarnome.get() 
    
    if nome =='':
            messagebox.showerror('Erro','Favor Preencher os Campos')
            return
        
    nome = str(e_consultarnome.get())
   
    # Chamar a Função Limpar os Campos
    limpar_campos() 
    
    # Chamar a Função Mostrar Tabela
    consultar_nome(nome) 
    
def consultar_nome(nome):
    
    global tree 
    
    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço', 'Serviço','Descrição Do Serviço','Materiais Usados','Forma de pagamento', 'Lucro']

    # Função Select do Banco de Dados
    
    lista_itens = bd.selectNome(nome)
    
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings",height=11)

    # vertical scrollbar
    
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=1500)

    hd=["center","center","center","center","center","center","center","center","center"]
    h=[100,100,150,140,140,200,150,170,130]
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

    tabela_head = ['Matricula', 'Nome', 'Whatsapp', 'Endereço', 'Serviço','Descrição Do Serviço','Materiais Usados','Forma de pagamento', 'Lucro']

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings",height=11)

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=1500)
    
    tree.tag_configure('odd', background='#E8E8E8')
    tree.tag_configure('even', background='#DFDFDF') 

    hd=["center","center","center","center","center","center","center","center","center"]
    h=[100,100,150,140,140,200,150,170,130]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

def botão_desativado():
    bt_adicionar.configure(state= 'disabled')
    bt_cancel_cad.configure(state= 'disabled')
#-------------------------------------------------------
# Criando Logo
img00 = Image.open(os.path.join(img_path,'Logo_ZeroGrau2.png'))
img00 = img00.resize((250, 250))
img00 = ImageTk.PhotoImage(img00)

lb_logoCabeçalho = Label(frameCima, padx=10, width=1045,image = img00,compound=LEFT, anchor=NW,bg='white')
lb_logoCabeçalho.place(x=500, y=-80)

img01 = Image.open(os.path.join(img_path,'Logo_ZeroGrau.png'))
img01 = img01.resize((170, 170))
img01 = ImageTk.PhotoImage(img01)

lb_logo = Label(frameMeio, padx=10, width=1045,image = img01,compound=LEFT, anchor=NW,bg='white')
lb_logo.place(x=1050, y=-10)

janela.iconbitmap(os.path.join(img_path,'floconeve2.ico'))
#--------------------------------------------------------

lb_matricula =Label(frameMeio, font=('bold'), text='Matrícula',bg='#FFFFFF', fg='black')
lb_matricula.place(x=10, y=10)
e_matricula= Entry(frameMeio, width=10)
e_matricula.place(x=90, y=11)

img02 = Image.open(os.path.join(img_path,'floconeve.png'))
img02 = img02.resize((20, 20))
img02 = ImageTk.PhotoImage(img02)

bt_matricula= Button(frameMeio, width=130,image = img02, text='Gerar Matrícula',compound= LEFT, anchor= CENTER, fg='black', bg='white',command= matricula)
bt_matricula.place(x=190, y=8)

lb_nome =Label(frameMeio, font=('bold'), text='Nome',bg='#FFFFFF', fg='black')
lb_nome.place(x=10, y=60)
e_nome= Entry(frameMeio, width=40)
e_nome.place(x=90, y=61)

lb_whatsapp =Label(frameMeio, font=('bold'), text='Whatsapp',bg='#FFFFFF', fg='black')
lb_whatsapp.place(x=345, y=60)
e_whatsapp= Entry(frameMeio, width=20)
e_whatsapp.place(x=435, y=61)

lb_endereco =Label(frameMeio, font=('bold'), text='Endereço',bg='#FFFFFF', fg='black')
lb_endereco.place(x=576, y=61)
e_endereco= Entry(frameMeio, width=40)
e_endereco.place(x=665, y=61)

lb_desc_servico =Label(frameMeio, font=('bold'), text='Descrição Do Serviço',bg='#FFFFFF', fg='black')
lb_desc_servico.place(x=10, y=110)
e_desc_servico= Entry(frameMeio, width=40)
e_desc_servico.place(x=187, y=111)

lb_mat_usados =Label(frameMeio, font=('bold'), text='Materiais Usados',bg='#FFFFFF', fg='black')
lb_mat_usados.place(x=10, y=160)
e_mat_usados= Entry(frameMeio, width=40)
e_mat_usados.place(x=157, y=161)

lb_preco_final =Label(frameMeio, font=('bold'), text='Preço Final',bg='#FFFFFF', fg='black')
lb_preco_final.place(x=740, y=160)
lb_reais =Label(frameMeio, font=('bold'), text='Reais',bg='#FFFFFF', fg='black')
lb_reais.place(x=900, y=160)
e_preco_final= Entry(frameMeio, width=10)
e_preco_final.place(x=830, y=161)

lista_servico= bd.selectServico()

lb_servico =Label(frameMeio, font=('bold'),height=1, text='Serviço',bg='#FFFFFF', fg='black')
lb_servico.place(x=450, y=110)
combo_serv= ttk.Combobox(frameMeio,width=18)
combo_serv['values']= (lista_servico)
combo_serv.current(0) # Default
combo_serv.place(x=520, y=111)

lista_pagamento = bd.selectPagamento()

lb_pagamento =Label(frameMeio, font=('bold'),height=1, text='Forma De Pagamento',bg='#FFFFFF', fg='black')
lb_pagamento.place(x=450, y=160)
combo_pag= ttk.Combobox(frameMeio,width=13)
combo_pag['values']= (lista_pagamento)
combo_pag.current(0) # Default
combo_pag.place(x=620, y=161)

lb_gasto =Label(frameMeio, font=('bold'), text='Gasto',bg='#FFFFFF', fg='black')
lb_gasto.place(x=450, y=200)
e_gasto= Entry(frameMeio, width=10)
e_gasto.place(x=505, y=201)

lb_lucro =Label(frameMeio, font=('bold'), text='Lucro',bg='#FFFFFF', fg='black')
lb_lucro.place(x=620, y=200)
e_lucro= Entry(frameMeio, width=15)
e_lucro.place(x=680, y=201)

lista_arcondicionado = bd.selectAr()

lb_marcaAr =Label(frameMeio, font=('bold'),height=1, text='Marca do Ar Condicionado',bg='#FFFFFF', fg='black')
lb_marcaAr.place(x=680, y=110)
combo_Ar= ttk.Combobox(frameMeio,width=13)
combo_Ar['values']= (lista_arcondicionado)
combo_Ar.current(0) # Default
combo_Ar.place(x=880, y=111)

img03 = Image.open(os.path.join(img_path,'floconeve.png'))
img03 = img03.resize((20, 20))
img03 = ImageTk.PhotoImage(img03)

bt_adicionar= Button(frameMeio, width=120,image = img03, text='Cadastrar',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=login)
bt_adicionar.place(x=450, y=8)

bt_cancel_cad= Button(frameMeio, width=125,image = img03, text='Cancelar Cadastro',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=cancelar_cadastro)
bt_cancel_cad.place(x=600, y=8)

bt_relatorio= Button(frameMeio, width=125,image = img03, text='Gerar Relatorio',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=gerar_relatorio)
bt_relatorio.place(x=760, y=8)
                
bt_consultar= Button(frameMeio, width=95,image = img03, text='Consultar',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=consultarGeral)
bt_consultar.place(x=10, y=220)

bt_atualizar= Button(frameMeio, width=95,image = img03, text='Atualizar',compound= LEFT, anchor= CENTER, fg='black', bg='white',command= atualizar)
bt_atualizar.place(x=130, y=220)

bt_excluir= Button(frameMeio, width=95,image = img03, text='Excluir',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=deletar)
bt_excluir.place(x=250, y=220)

bt_limpar= Button(frameMeio, width=125,image = img03, text='Limpar Campos',compound= LEFT, anchor= CENTER, fg='black', bg='white', command= limpar_campos)
bt_limpar.place(x=910, y=8)

bt_sair= Button(frameCima, width=95,image = img03, text='Sair',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=logoff)
bt_sair.place(x=1150, y=10)

bt_consultarmat= Button(frameMeio, width=130,image = img03, text='Consultar Matricula',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=consultarMat)
bt_consultarmat.place(x=990, y=210)
e_consultarmat= Entry(frameMeio, width=20)
e_consultarmat.place(x=1150, y=211)

bt_consultarnome= Button(frameMeio, width=130,image = img03, text='Consultar Nome',compound= LEFT, anchor= CENTER, fg='black', bg='white',command=consultarNome)
bt_consultarnome.place(x=990, y=170)
e_consultarnome= Entry(frameMeio, width=20)
e_consultarnome.place(x=1150, y=171)

limpar_campos()
botão_desativado()
mostrarTabela()
janela.mainloop()