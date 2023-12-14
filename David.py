import streamlit as st

st.title("Sabe mesmo sobre Futebol?")

if 'pontuacao' not in st.session_state:
    st.session_state.pontuacao = 0

nome = st.text_input("Digite seu nome: ")
if nome:
    st.header(f"Seja bem vindo {nome}!!")
    st.header("Esse quiz sobre futebol busca testar seu conhecimento sobre o esporte com muito entretenimento e clubismo.")

    
    perg1 = st.subheader("1. Quem é o artilheiro da seleção brasileira?")
    res1 = st.button('a) Pelée')
    res2 = st.button("b) Ronaldo")
    res3 = st.button("c) Neymarr")
    res4 = st.button("d) Zico")
    if res3:
        st.success("Acertou!")
        st.session_state.pontuacao += 1


    perg2 = st.subheader("2. Qual país sediou a Copa do Mundo de 2022?")
    res1_2 = st.button("a) Alemanha")
    res2_2 = st.button("b) Rússia")
    res3_2 = st.button("c) França")
    res4_2 = st.button("d) Qatar")
    if res4_2:
        st.success("Acertou!")
        st.session_state.pontuacao += 1


    perg3 = st.subheader("3. Em que ano o Brasil sediou a última Copa do Mundo antes de 2014?")
    res1_3 = st.button("a) 2002")
    res2_3 = st.button("b) 1998")
    res3_3 = st.button("c) 1994")
    res4_3 = st.button("d) 1950")
    if res4_3:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    perg4 = st.subheader("4. Quem é o único jogador a ter vencido a Bola de Ouro da FIFA por mais de cinco vezes?")
    res1_4 = st.button("a) Cristiano Ronaldo")
    res2_4 = st.button("b) Lionel Messi")
    res3_4 = st.button("c) Neymar")
    res4_4 = st.button("d) Andrés Iniesta")
    if res2_4:
        st.success("Acertou!")
        st.session_state.pontuacao += 1


    perg5 = st.subheader("5. Quais foram os anos que o Brasil ganhou as suas copas?")
    res1_5 = st.button("a) 1974, 1982, 1988, 2002")
    res2_5 = st.button("b) 1958, 1962, 1970, 1994, 2002")
    res3_5 = st.button("c) 1958, 1962, 1970, 1998, 2002")
    res4_5 = st.button("d) 1958, 1962, 1970, 1998, 2006")
    if res2_5:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    perg6 = st.subheader("6. Quem é o maior artilheiro por seleções?")
    res1_6 = st.button("a) Pelé")
    res2_6 = st.button("b) Neymaru")
    res3_6 = st.button("c) Cristiano Ronaldo")
    res4_6 = st.button("d) Zidane")
    if res3_6:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    perg7 = st.subheader("7. Maior campeão do campeonato brasileiro?")
    res1_7 = st.button("a) Palmeiras")
    res2_7 = st.button("b) Santos")
    res3_7 = st.button("c) Flamengo")
    res4_7 = st.button("d) Corinthians")
    if res1_7:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    perg8 = st.subheader("8. Quem é o último campeão brasileiro em mundial de clubes?")
    res1_8 = st.button("a) Corinthians")
    res2_8 = st.button("b) Liverpool")
    res3_8 = st.button("c) Vasco")
    res4_8 = st.button("d) Grêmio")
    if res1_8:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    perg9 = st.subheader("9. Quem é o brasileiro mais jovem a ter atuado pela seleção brasileira em uma partida oficial?")
    res1_9 = st.button("a) Neynar")
    res2_9 = st.button("b) Ronaldinho Gaúcho")
    res3_9 = st.button("c) Pellé")
    res4_9 = st.button("d) Kaká")
    if res3_9:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    perg10 = st.subheader("10. O único goleiro a ganhar Bola de Ouro?")
    res1_10 = st.button("a) Alisson")
    res2_10 = st.button("b) Gianluigi Donnarumma")
    res3_10 = st.button("c) Suárez")
    res4_10 = st.button("d) Yashin")
    if res4_10:
        st.success("Acertou!")
        st.session_state.pontuacao += 1

    st.title(f'Essa foi sua Pontuação {st.session_state.pontuacao}')
