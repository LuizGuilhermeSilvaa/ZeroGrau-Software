#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk
#from tkinter import filedialog as fd
import os
# Importando o módulo de acesso ao SQLite
import sqlite3 as sql3
import datetime as dt

# Gmail
import smtplib
import email.message

# Senha
from hashlib import sha256

#-------- GMAIL ---------------------
      

#----------------------------------------------------------------------------
# Banco de Dados 
# Path
cadastro_path = os.path.join(os.getcwd(), 'CadrastoZero.db')

# # ---------------------------- TB CURSOS ---------------  


# # ---------------------------- TB LOGIN ---------------  
# # Inserindo Dados LOGIN
def inserirLogin(dados):
    try:
        con = sql3.connect(cadastro_path)
        
        with con:
            # Criando um cursorsor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando outra sentença SQL para inserir registros
            sql_insert = 'insert into login(login,senha,data_cadastro)values (?, ?, ?)'

            # Inserindo os registros
            cursor.execute(sql_insert, dados)
            # Grava a transação
            con.commit()
            messagebox.showinfo('Sucesso','Cadastro Realizado com Sucesso')
            
            
    except Exception as err:
        messagebox.showerror('Erro',err)

#------------------------------------------------------------------------     
# # Select Dados Login
def selectLogin(dados):
    #print(dados[0])
    try:
        con = sql3.connect(cadastro_path)    
        with con:
            # Criando um cursor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando Lista Vazia para Armazenar os Dados
            var_dadosId= []
            
            # Criando outra sentença SQL para selecionar registros
            sql_select = 'select * from login where login=? and senha=?'              
                                   
            # Seleciona todos os registros 
            cursor.execute(sql_select, dados)
            #cursor.execute(sql_select, selDados)

            # recupera os registros
            selectDados = cursor.fetchall()

            # Mostra
            for linha in selectDados:  
                var_dadosId.append(linha)            
        
        return var_dadosId 
    except Exception as err:
        messagebox.showerror('Erro',err)    

# ---------------------------- TB CADASTRO --------------- 
# Inserindo Dados CADASTRO
def inserirDados(dados):    
    try:
        con = sql3.connect(cadastro_path) 
        with con:
            # Criando um cursorsor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()
            
            # Criando outra sentença SQL para inserir registros
            sql_insert = 'insert into usuarios(matricula, nome, whatsapp, endereco, servico, data_cadastro)values (?, ?, ?, ?, ?, ?)'

            # Inserindo os registros
            cursor.execute(sql_insert, dados)
            # Grava a transação
            con.commit()
            messagebox.showinfo('Sucesso','Cadastro Realizado com Sucesso')
                   
    except Exception as err:
        messagebox.showerror('Erro',err)

#------------------------------------------------------------
# Select Dados Geral
def selectAll():
    try:
        con = sql3.connect(cadastro_path)
        with con:
            # Criando um cursor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando Lista Vazia para Armazenar os Dados
            var_dados= []

            # Criando outra sentença SQL para selecionar registros
            sql_select = 'select * from usuarios' 

            # Seleciona todos os registros 
            cursor.execute(sql_select)

            # recupera os registros
            selectDados = cursor.fetchall()

            # Mostra
            for linha in selectDados:  
                var_dados.append(linha)
        return var_dados 

        messagebox.showinfo('Sucesso','Consulta Realizado com Sucesso')    
    except Exception as err:
        messagebox.showerror('Erro',err)

#-----------------------------------
# Select Dados Cpf
def selectMatricula(dados):
    try:
        con = sql3.connect(cadastro_path)
        with con:
            # Criando um cursor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando Lista Vazia para Armazenar os Dados
            var_dadosId= []

            # Criando outra sentença SQL para selecionar registros
            sql_select = 'select * from usuarios where matricula=?'        
            
            # Dados converter
            selDados = [dados] 
                        
            # Seleciona todos os registros 
            #cursor.execute(sql_select, dados)
            cursor.execute(sql_select, selDados)

            # recupera os registros
            selectDados = cursor.fetchall()

            # Mostra
            for linha in selectDados:  
                var_dadosId.append(linha)            
        
        return var_dadosId  

    except Exception as err:
        messagebox.showerror('Erro',err)     

#-----------------------------------
# Atualizando Dados    
def updateDados(dados):
    try:
        con = sql3.connect(cadastro_path)
        with con:
            # Criando um cursorsor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()
 
            # Criando outra sentença SQL para inserir registros
            sql_update = 'update usuarios SET  whatsapp=?, endereco=? ,nome=? WHERE matricula=?'    

            # Atualizando os registros
            cursor.execute(sql_update, dados)
            messagebox.showinfo('Sucesso','Cadastro Atualizado com Sucesso')

            # Fecha a conexão
            #con.close()
    except Exception as err:
        messagebox.showerror('Erro',err)
    
#-----------------------------------------------
# Deletando Dados
def deleteDados(dados):
    try:
        con = sql3.connect(cadastro_path)
        with con:
            # Criando um cursorsor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando outra sentença SQL para inserir registros
            sql_delete = 'delete from usuarios WHERE matricula=?'

             # Dados converter 
            delDados = [dados] 
           
            # Deletar os registros
            cursor.execute(sql_delete, delDados) 
            messagebox.showinfo('Sucesso','Cadastro Excluido com Sucesso')
            
            # Fecha a conexão
            #con.close()
    except Exception as err:
        messagebox.showerror('Erro',err)     


# In[ ]:




