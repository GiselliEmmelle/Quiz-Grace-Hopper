import streamlit as st

st.set_page_config(page_title="INSERIR TÍTULO AQUI")

# --- Inicialização do estado de sessão ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "nome" not in st.session_state:
    st.session_state.nome = ""
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "escolha" not in st.session_state:
    st.session_state.escolha = None

# --- Banco de perguntas ---
perguntas = [
    {
        "pergunta": "A importância de Grace Hopper está relacionada principalmente ao fato de ela ter:",
        "opcoes": ["Desenvolvido componentes físicos dos computadores modernos.",
                   "Trabalhado exclusivamente com hardware.",
                   "Criado sistemas de navegação militar.",
                   "Tornado a programação mais próxima da linguagem humana."],
        "resposta": "D"
    },
    {
        "pergunta": "O desenvolvimento de compiladores por Grace Hopper contribuiu para:",
        "opcoes": ["A eliminação das linguagens de programação.",
                   "A substituição dos computadores por máquinas analógicas.",
                   "A tradução de linguagens compreensíveis para código de máquina.",
                   "A criação de dispositivos físicos mais rápidos."],
        "resposta": "C"
    },
    # Você pode continuar adicionando todas as perguntas restantes aqui...
]

# --- Funções ---
def iniciar_quiz():
    if st.session_state.nome.strip() != "":
        st.session_state.pagina = "quiz"
        st.session_state.indice = 0
        st.session_state.total = 0
        st.session_state.respondido = False
        st.session_state.feedback = ""
        st.session_state.escolha = None
        st.experimental_rerun()
    else:
        st.warning("Por favor, digite seu nome para iniciar o quiz.")

def responder():
    escolha = st.session_state.escolha
    correta = perguntas[st.session_state.indice]["resposta"]
    if escolha == correta:
        st.session_state.feedback = "✅ Resposta correta!"
        st.session_state.total += 10
    else:
        st.session_state.feedback = f"❌ Resposta errada! A alternativa correta era letra {correta}."
    st.session_state.respondido = True

def proxima():
    st.session_state.indice += 1
    st.session_state.feedback = ""
    st.session_state.respondido = False
    st.session_state.escolha = None
    if st.session_state.indice >= len(perguntas):
        st.session_state.pagina = "resultado"
    st.experimental_rerun()

# --- Tela Inicial ---
if st.session_state.pagina == "inicio":
    st.title("INSERIR TÍTULO AQUI")
    st.session_state.nome = st.text_input("Como você quer ser chamado?")
    st.button("Iniciar Quiz", on_click=iniciar_quiz)

# --- Tela de Quiz ---
elif st.session_state.pagina == "quiz":
    pergunta_atual = perguntas[st.session_state.indice]
    st.subheader(f"QUESTÃO {st.session_state.indice + 1}")
    st.write(pergunta_atual["pergunta"])

    # Exibir opções
    st.radio(
        "Escolha uma opção:",
        ["A", "B", "C", "D"],
        key="escolha",
        format_func=lambda x: f"{x}) {pergunta_atual['opcoes'][['A','B','C','D'].index(x)]}",
        disabled=st.session_state.respondido
    )

    if not st.session_state.respondido:
        st.button("Responder", on_click=responder)
    else:
        st.info(st.session_state.feedback)
        st.button("Próxima", on_click=proxima)

# --- Tela de Resultado ---
elif st.session_state.pagina == "resultado":
    st.title(f"Parabéns, {st.session_state.nome}!")
    st.subheader(f"Seu total de pontos é: {st.session_state.total}")

    if st.session_state.total >= 80:
        st.success("Parabéns! Você demonstrou um excelente conhecimento sobre Grace Hopper e sua importância para a história da computação.")
    elif st.session_state.total >= 50:
        st.info("Você foi muito bem no quiz! Mostrou que já conhece grande parte da trajetória de Grace Hopper e suas contribuições.")
    elif st.session_state.total >= 20:
        st.warning("Você está no caminho certo! Já conhece alguns fatos importantes sobre Grace Hopper, mas ainda pode aprender mais.")
    else:
        st.error("Não se preocupe! Esse quiz é uma ótima oportunidade para conhecer melhor quem foi Grace Hopper. Estude mais e tente novamente!")
