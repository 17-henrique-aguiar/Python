import streamlit as st
import db as db # importa as funções do banco

# .\.venv\Scripts\activate - Ativar o venv pelo terminal

# Configuração inicial
st.set_page_config(page_title="Loja Virtual", page_icon="", layout="wide")
db.criar_tabela()

# Lista de produtos
produtos = [
    {"nome": "Celular", "preco": 1500, "imagem": "imagem/imagem1.jpg"},
    {"nome": "Notebook", "preco": 3500, "imagem": "imagem/notebook.jpg"},
    {"nome": "Fone de Ouvido", "preco": 200, "imagem": "imagem/fone.jpg"},
    {"nome": "Smartwatch", "preco": 500, "imagem": "imagem/tablet.jpg"},
]

st.title("Loja Virtual")
st.write("Escolha seu produto:")

cols = st.columns(4)

# Exibe os cards
for idx, produto in enumerate(produtos):
    with cols[idx % 4]:
        st.image(produto["imagem"], use_container_width=True)
        st.subheader(produto["nome"])
        st.write(f" $ {produto['preco']:.2f}")
        if st.button(f"Comprar {produto['nome']}", key=produto["nome"]):
            db.adicionar_item(produto["nome"], produto["preco"])
            st.success(f"{produto['nome']} adicionado ao carrinho!")

# Exibe o carrinho
st.markdown("## Carrinho")
itens = db.listar_carrinho()

if itens:
    total = 0
    for item in itens:
        item_id, nome, preco = item
        st.write(f"- {nome} — $ {preco:.2f}")
        total += preco
        if st.button(f"Remover {nome}", key=f"remover_{item_id}"):
            db.remover_item(item_id)
            st.rerun()

    st.markdown(f"### Total: {total:.2f}")
else:
    st.write("Carrinho vazio.")
