import streamlit as st

# --- Título do App ---
st.set_page_config(page_title="INSERIR TÍTULO AQUI")

# Inicialização do estado de sessão
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "nome" not in st.session_state:
    st.session_state.nome = ""

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
    {
        "pergunta": "Ao influenciar linguagens como o COBOL, Grace Hopper promoveu:",
        "opcoes": ["O uso exclusivo da programação militar.",
                   "A popularização de linguagens mais acessíveis.",
                   "A redução do uso de computadores.",
                   "A limitação da programação a especialistas."],
        "resposta": "B"
    },
    {
        "pergunta": "Antes das contribuições de Grace Hopper, a programação era caracterizada por:",
        "opcoes": ["Linguagem simples e intuitiva.",
                   "Forte acessibilidade ao público geral.",
                   "Uso predominante de interfaces gráficas.",
                   "Alto nível de complexidade técnica."],
        "resposta": "D"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": ["A aproximação entre humanos e máquinas.",
                   "A substituição da lógica de programação.",
                   "O fim das linguagens de programação.",
                   "A automação total sem necessidade de código."],
        "resposta": "A"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": ["Apenas na área militar.",
                   "Apenas na construção de hardware.",
                   "Na evolução da tecnologia e dos computadores.",
                   "Exclusivamente na educação básica."],
        "resposta": "C"
    },
    {
        "pergunta": "A criação de compiladores pode ser entendida como um avanço porque:",
        "opcoes": ["Eliminou a necessidade de computadores.",
                   "Facilitou a comunicação entre humanos e máquinas.",
                   "Tornou a programação mais complexa.",
                   "Substituiu os programadores."],
        "resposta": "B"
    },
    {
        "pergunta": "O papel de Grace Hopper na história da computação evidencia:",
        "opcoes": ["A democratização do acesso à programação.",
                   "A dificuldade crescente da programação.",
                   "A centralização do conhecimento tecnológico.",
                   "A limitação da informática ao meio militar."],
        "resposta": "A"
    },
    {
        "pergunta": "A expressão 'linguagens mais acessíveis' indica que:",
        "opcoes": ["Apenas especialistas podiam utilizá-las.",
                   "Eram voltadas exclusivamente para máquinas.",
                   "Eram mais fáceis de compreender por humanos.",
                   "Não utilizavam código."],
        "resposta": "C"
    },
    {
        "pergunta": "Pode-se concluir que as contribuições de Grace Hopper:",
        "opcoes": ["Ajudaram a moldar a computação moderna.",
                   "Foram irrelevantes para a informática atual.",
                   "Reduziram o avanço tecnológico.",
                   "Tiveram impacto apenas temporário."],
        "resposta": "A"
    }
]

# --- Função para avançar ---
def proxima():
    escolha = st.session_state.escolha.upper() if st.session_state.escolha else ""
    if escolha == perguntas[st.session_state.indice]["resposta"]:
        st.session_state.total += 10
    st.session_state.indice += 1
    st.session_state.escolha = None

# --- Tela inicial ---
if st.session_state.pagina == "inicio":
    st.title("INSERIR TÍTULO AQUI")
    st.session_state.nome = st.text_input("Como você quer ser chamado?")
    if st.button("Iniciar Quiz"):
        if st.session_state.nome.strip() != "":
            st.session_state.pagina = "quiz"
        else:
            st.warning("Por favor, digite seu nome para iniciar o quiz.")

# --- Tela de perguntas ---
elif st.session_state.pagina == "quiz":
    if st.session_state.indice < len(perguntas):
        pergunta_atual = perguntas[st.session_state.indice]
        st.subheader(f"QUESTÃO {st.session_state.indice + 1}")
        st.write(pergunta_atual["pergunta"])
        st.radio("Escolha uma opção:", ["A", "B", "C", "D"], key="escolha", format_func=lambda x: f"{x}) {pergunta_atual['opcoes'][['A','B','C','D'].index(x)]}")
        if st.button("Próxima"):
            if st.session_state.escolha is None:
                st.warning("Selecione uma opção antes de continuar!")
            else:
                proxima()
                st.experimental_rerun()
    else:
        st.session_state.pagina = "resultado"
        st.experimental_rerun()

# --- Tela de resultado ---
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
