import streamlit as st

st.set_page_config(page_title="Quiz Grace Hopper", layout="centered")

# -------------------------------
# PERGUNTAS
# -------------------------------
quiz = [
    {
        "pergunta": "A importância de Grace Hopper está relacionada principalmente ao fato de ela ter:",
        "opcoes": [
            "A) Desenvolvido componentes físicos dos computadores modernos.",
            "B) Trabalhado exclusivamente com hardware.",
            "C) Criado sistemas de navegação militar.",
            "D) Tornado a programação mais próxima da linguagem humana."
        ],
        "resposta": "D"
    },
    {
        "pergunta": "O desenvolvimento de compiladores por Grace Hopper contribuiu para:",
        "opcoes": [
            "A) A eliminação das linguagens de programação.",
            "B) A substituição dos computadores por máquinas analógicas.",
            "C) A tradução de linguagens compreensíveis para código de máquina.",
            "D) A criação de dispositivos físicos mais rápidos."
        ],
        "resposta": "C"
    },
    {
        "pergunta": "Ao influenciar linguagens como o COBOL, Grace Hopper promoveu:",
        "opcoes": [
            "A) O uso exclusivo da programação militar.",
            "B) A popularização de linguagens mais acessíveis.",
            "C) A redução do uso de computadores.",
            "D) A limitação da programação a especialistas."
        ],
        "resposta": "B"
    },
    # Adicione as demais perguntas aqui...
]

# -------------------------------
# ESTADO
# -------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if "indice" not in st.session_state:
    st.session_state.indice = 0

if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

if "nome" not in st.session_state:
    st.session_state.nome = ""

if "respondido" not in st.session_state:
    st.session_state.respondido = False

# -------------------------------
# TELA INICIAL
# -------------------------------
if st.session_state.pagina == "inicio":
    st.title("INSERIR TÍTULO AQUI")

    nome = st.text_input("Como você quer ser chamado?")

    if st.button("Iniciar Quiz"):
        if nome.strip():
            st.session_state.nome = nome
            st.session_state.pagina = "quiz"
            st.rerun()
        else:
            st.warning("Digite seu nome!")

# -------------------------------
# QUIZ
# -------------------------------
elif st.session_state.pagina == "quiz":
    q = quiz[st.session_state.indice]

    st.subheader(f"Questão {st.session_state.indice + 1}")
    st.write(q["pergunta"])

    resposta = st.radio("Escolha uma opção:", q["opcoes"])

    # -------------------------
    # BOTÃO RESPONDER
    # -------------------------
    if not st.session_state.respondido:
        if st.button("Responder"):
            letra = resposta[0]

            if letra == q["resposta"]:
                st.success("✅ Você acertou!")
            else:
                st.error(f"❌ Você errou! A resposta correta é {q['resposta']})")

            # Atualiza pontuação
            if letra == q["resposta"]:
                st.session_state.pontuacao += 10

            st.session_state.respondido = True

    # -------------------------
    # BOTÃO PRÓXIMA (aparece abaixo do feedback)
    # -------------------------
    if st.session_state.respondido:
        if st.button("Próxima"):
            st.session_state.indice += 1
            st.session_state.respondido = False

            if st.session_state.indice >= len(quiz):
                st.session_state.pagina = "resultado"

            st.rerun()

# -------------------------------
# RESULTADO
# -------------------------------
elif st.session_state.pagina == "resultado":
    total = st.session_state.pontuacao

    st.title(f"Parabéns, {st.session_state.nome}!")
    st.write(f"Pontuação: {total}")

    if total >= 80:
        st.success("Excelente conhecimento sobre Grace Hopper!")
    elif total >= 50:
        st.info("Muito bom! Continue estudando!")
    elif total >= 20:
        st.warning("Você está no caminho certo!")
    else:
        st.error("Continue estudando e tente novamente!")

    if st.button("Reiniciar"):
        st.session_state.pagina = "inicio"
        st.session_state.indice = 0
        st.session_state.pontuacao = 0
        st.session_state.respondido = False
        st.rerun()
