#!/usr/bin/env python
# coding: utf-8

# In[1]:
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk
import os
import sqlite3 as sql3
import pandas as pd
from hashlib import sha256

#----------------------------------------------------------------------------
# Banco de Dados 
# Path
cadastro_path = os.path.join(os.getcwd(), 'CadrastoZero.db')

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
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)

#------------------------------------------------------------------------     
# # Select Dados Login
def selectLogin(dados):
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
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)    

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
            sql_insert = 'insert into usuarios(matricula, nome, whatsapp, endereco,data_limpeza,prox_limpeza, data_cadastro)values (?, ?, ?, ?, ?, ?, ?)'

            # Inserindo os registros
            cursor.execute(sql_insert, dados)
            # Grava a transação
            con.commit()
            messagebox.showinfo('Sucesso','Cadastro Realizado com Sucesso')
                   
    except Exception as err:
        #messagebox.showerror('Erro','A matricula ja existe!, tente novamente')
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

    except Exception as err:
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)



def selectServico():
    try:
        con = sql3.connect(cadastro_path)
        with con:
            # Criando um cursor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando Lista Vazia para Armazenar os Dados
            var_dados= []

            # Criando outra sentença SQL para selecionar registros
            sql_select = 'select * from servico' 

            # Seleciona todos os registros 
            cursor.execute(sql_select)

            # recupera os registros
            selectDados = cursor.fetchall()

            # Mostra
            for linha in selectDados:  
                var_dados.append(linha)
        return var_dados 
     
    except Exception as err:
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)
#-----------------------------------
# Select Dados Cpf
def selectnome(dados):
    try:
        con = sql3.connect(cadastro_path)
        
        with con:
            # Criando um cursor 
            # (Um cursorsor permite percorrer todos os registros em um conjunto de dados)
            cursor = con.cursor()

            # Criando Lista Vazia para Armazenar os Dados
            var_dadosId= []

            # Criando outra sentença SQL para selecionar registros
            sql_select = 'select * from usuarios where nome=?'        
            
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
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)  
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
            sql_update = 'update usuarios SET  nome=? ,whatsapp=?, endereco=?, data_limpeza=?, prox_limpeza=? WHERE matricula=?'    

            # Atualizando os registros
            cursor.execute(sql_update, dados)
            messagebox.showinfo('Sucesso','Atualizado com Sucesso')

            # Fecha a conexão
            #con.close()
    except Exception as err:
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)
    
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
            
    except Exception as err:
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')
        #messagebox.showerror('Erro',err)

def gerar_relatorio():
    try:
        
        con = sql3.connect(cadastro_path)

        with con:
            
            rtCSV_path = os.path.join(os.getcwd(),'relatorios/Limpezas/rt_limpeza.csv')
            rtXLSX_path = os.path.join(os.getcwd(),'relatorios/Limpezas/rt_limpeza.xlsx')

            df = pd.read_sql('select * from usuarios',con, index_col='matricula')

            df.to_csv(rtCSV_path)
            df.to_excel(rtXLSX_path)

            messagebox.showinfo('Sucesso','Relatorio Gerado com Sucesso')

    except  Exception as err:
        messagebox.showinfo('Erro','Ops..Alguma Coisa deu errado!')       
        #messagebox.showerror('Erro',err)    


# In[4]:





# In[ ]:




