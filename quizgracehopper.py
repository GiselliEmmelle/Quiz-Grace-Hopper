import streamlit as st

# --- Tela Inicial ---
st.title("INSERIR TÍTULO AQUI")

if 'pagina' not in st.session_state:
    st.session_state.pagina = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'nome' not in st.session_state:
    st.session_state.nome = ""

# Lista de perguntas, opções e respostas corretas
quiz = [
    {
        "pergunta": "A importância de Grace Hopper está relacionada principalmente ao fato de ela ter:",
        "opcoes": ["A) Desenvolvido componentes físicos dos computadores modernos.",
                   "B) Trabalhado exclusivamente com hardware.",
                   "C) Criado sistemas de navegação militar.",
                   "D) Tornado a programação mais próxima da linguagem humana."],
        "resposta": "D"
    },
    {
        "pergunta": "O desenvolvimento de compiladores por Grace Hopper contribuiu para:",
        "opcoes": ["A) A eliminação das linguagens de programação.",
                   "B) A substituição dos computadores por máquinas analógicas.",
                   "C) A tradução de linguagens compreensíveis para código de máquina.",
                   "D) A criação de dispositivos físicos mais rápidos."],
        "resposta": "C"
    },
    {
        "pergunta": "Ao influenciar linguagens como o COBOL, Grace Hopper promoveu:",
        "opcoes": ["A) O uso exclusivo da programação militar.",
                   "B) A popularização de linguagens mais acessíveis.",
                   "C) A redução do uso de computadores.",
                   "D) A limitação da programação a especialistas."],
        "resposta": "B"
    },
    {
        "pergunta": "Antes das contribuições de Grace Hopper, a programação era caracterizada por:",
        "opcoes": ["A) Linguagem simples e intuitiva.",
                   "B) Forte acessibilidade ao público geral.",
                   "C) Uso predominante de interfaces gráficas.",
                   "D) Alto nível de complexidade técnica."],
        "resposta": "D"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": ["A) A aproximação entre humanos e máquinas.",
                   "B) A substituição da lógica de programação.",
                   "C) O fim das linguagens de programação.",
                   "D) A automação total sem necessidade de código."],
        "resposta": "A"
    },
    {
        "pergunta": "A transformação promovida por Grace Hopper permitiu:",
        "opcoes": ["A) Apenas na área militar.",
                   "B) Apenas na construção de hardware.",
                   "C) Na evolução da tecnologia e dos computadores.",
                   "D) Exclusivamente na educação básica."],
        "resposta": "C"
    },
    {
        "pergunta": "A criação de compiladores pode ser entendida como um avanço porque:",
        "opcoes": ["A) Eliminou a necessidade de computadores.",
                   "B) Facilitou a comunicação entre humanos e máquinas.",
                   "C) Tornou a programação mais complexa.",
                   "D) Substituiu os programadores."],
        "resposta": "B"
    },
    {
        "pergunta": "O papel de Grace Hopper na história da computação evidencia:",
        "opcoes": ["A) A democratização do acesso à programação.",
                   "B) A dificuldade crescente da programação.",
                   "C) A centralização do conhecimento tecnológico.",
                   "D) A limitação da informática ao meio militar."],
        "resposta": "A"
    },
    {
        "pergunta": "A expressão 'linguagens mais acessíveis' indica que:",
        "opcoes": ["A) Apenas especialistas podiam utilizá-las.",
                   "B) Eram voltadas exclusivamente para máquinas.",
                   "C) Eram mais fáceis de compreender por humanos.",
                   "D) Não utilizavam código."],
        "resposta": "C"
    },
    {
        "pergunta": "Pode-se concluir que as contribuições de Grace Hopper:",
        "opcoes": ["A) Ajudaram a moldar a computação moderna.",
                   "B) Foram irrelevantes para a informática atual.",
                   "C) Reduziram o avanço tecnológico.",
                   "D) Tiveram impacto apenas temporário."],
        "resposta": "A"
    },
]

def mostrar_pergunta(index):
    st.subheader(f"QUESTÃO {index + 1}")
    st.write(quiz[index]["pergunta"])
    escolha = st.radio("Escolha uma alternativa:", quiz[index]["opcoes"])
    if st.button("Próxima"):
        # Verifica se a resposta está correta
        if escolha[0].upper() == quiz[index]["resposta"]:
            st.session_state.total += 10
        st.session_state.pagina += 1
        st.experimental_rerun()

# --- Lógica de navegação ---
if st.session_state.pagina == 0:
    nome = st.text_input("Como você quer ser chamado?")
    if st.button("Iniciar Quiz") and nome:
        st.session_state.nome = nome
        st.session_state.pagina = 1
        st.experimental_rerun()
elif 1 <= st.session_state.pagina <= len(quiz):
    mostrar_pergunta(st.session_state.pagina - 1)
else:
    # Tela final
    st.subheader(f"Parabéns, {st.session_state.nome}! Você concluiu o quiz!")
    st.write(f"Seu total de pontos é: {st.session_state.total}")

    if st.session_state.total >= 80:
        st.success("Parabéns! Você demonstrou um excelente conhecimento sobre Grace Hopper e sua importância para a história da computação. Suas respostas mostram que você realmente entende o impacto dela no desenvolvimento da tecnologia. Continue explorando a história da informática!")
    elif st.session_state.total >= 50:
        st.info("Você foi muito bem no quiz! Mostrou que já conhece grande parte da trajetória de Grace Hopper e suas contribuições para a programação. Com um pouco mais de estudo, você chega ao nível máximo! Parabéns pela conquista!")
    elif st.session_state.total >= 20:
        st.warning("Você está no caminho certo! Já conhece alguns fatos importantes sobre Grace Hopper, mas ainda pode aprender mais sobre a história dela e sua influência na computação moderna. Continue praticando!")
    else:
        st.error("Não se preocupe! Esse quiz é uma ótima oportunidade para conhecer melhor quem foi Grace Hopper e como ela ajudou a transformar a programação e os computadores. Estude mais e tente novamente para ver a sua evolução!")
