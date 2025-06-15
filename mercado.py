# streamlit run c:/Users/bacop/Documents/GitHub/market-checklist/_main.py [ARGUMENTS]

import streamlit as st
import json
import os

PRODUTOS = 'produtos.json'
CARRINHO ='carrinho.json'

# Funções
def carregar_produtos():
    if os.path.exists(PRODUTOS):
        with open(PRODUTOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return "Lista vazia" 

def carregar_carrinho():
    if os.path.exists(CARRINHO):
        with open(CARRINHO, 'r', encoding='utf-8') as f:
            return json.load(f)            
    else:
        return "Lista vazia"
    
def salvar_carrinho(lista):
    with open(CARRINHO, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

def adicionar_item(item_selec, qtd):
    # lista = carregar_carrinho()
    for item in lista:
        if item == {"item": item_selec, "quantidade": f"{qtd}"}: 
            st.error(f"⚠️ O item '{item_selec}' já está na lista. \n")
            return
    novo_item = {"item": item_selec, "quantidade": f"{qtd}"}
    lista.append(novo_item)
    salvar_carrinho(lista)
    print(f"✅ Item '{item_selec} ({qtd})' adicionado!\n") 

def atualizar_lista():
    # lista = carregar_carrinho()
    for item in lista:
            col1, col2 = st.columns([4, 1])
            col1.write(f"{item["item"]} ({item.get('quantidade')})")
            if col2.button("🗑️", key=item):
                remover_item(item)
                st.success(f"{item["item"]} ({item["quantidade"]}) foi excluído!") 
                st.button("Ok")

def remover_item(item):
    lista.remove(item)
    salvar_carrinho(lista)

PRODUTOS = 'produtos.json'
CARRINHO ='carrinho.json'
lista = carregar_carrinho()

st.set_page_config(page_title="Mercado", page_icon="🍳")
st.title("🍳 Mercado")
st.subheader("Lista de Compras")
# Gera uma lista só com os valores do atributo 'item'
p_json = carregar_produtos()
p_itens = [dicionario['item'] for dicionario in p_json if 'item' in dicionario]
# Input 
item_selec = st.selectbox("Produto:",options=p_itens)
# Input
qtd = st.slider("Quantidade: ", min_value=1, max_value=20, value=1)
# Button "Incluir"
if st.button("Incluir"):
    adicionar_item(item_selec, qtd)
    # atualizar_lista()
st.subheader("🛒 Lista de Compras")
# lista = carregar_carrinho()
atualizar_lista()
