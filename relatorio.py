import streamlit as st

def furadeira_bancada_simulador(b1, b2, s2, s4, s3, s1, s7, e_stop):
    acionametos = st.columns(4)
    
    # Lógica do Ladder
    if b1 and b2 and s1 and not s2 and s4 and not e_stop and not s7:
        
        acionametos[0].success('L1 Acessa')
        acionametos[1].error('L2 Apagada')

        if not s3:
            acionametos[2].warning('M1 Acionado')
            acionametos[3].error('M2 não Acionado')
        else:
            acionametos[3].warning('M2 Acionado')
            acionametos[2].error('M1 não Acionado')
    else:
        acionametos[0].error('L1 Apagada')
        acionametos[1].success('L2 Acessa')
        acionametos[2].error('M1 não acionado')
        acionametos[3].error('M2 não acionado')

def main():
    st.title("Automação de Furadeira de Bancada")
    
    st.header('Introdução')
    
    with st.expander('Apresentação'):
        st.write('''
                 # Automação de Furadeira de Bancada
***Trabalho Desenvolvido para a disciplina de Sistemas de Integração e Automação Industrial.***
* Prof M.Sc. João Marcos Soares Anjos
* Aluno: Mateus Souza Silva
* Data: 24 de Janeiro de 2024

O Trabalho foi desenvolvido no ambiente LogixPro, utilizando a simulação básica de I/O para o desenvolvimento da lógica de funcionamento da Furadeira de Bancada e posteriormente o código Ladder correspondente. 
Como a implementação no LogixPro possa ser limitada no quesito funcionamento e didaticidade. Por conta desses empecilhos, foi desenvolvido uma explicação "dinâmica" utilizando a linguagem de programação python e uma biblioteca de desenvolvimento de aplicações web para uma melhor visualização do lógica da solução proposta para o trabalho. 
                 ''')
    
    st.header('Desenvolvimento')
    
    with st.expander('Código em Ladder'):
        st.write('Código desenvolvido no LogixPro')
        st.image(r'imgs/ladder.png')
    
    with st.expander('Simulação'):
        st.write('''
                 ## Como simular
Para que possa simular a automação, deve seguir os seguintes passos:
* Para que a furadeira desça e execute sua função de furar a peça, ambas as mãos do operador devem estar acionando as botoeiras B1 e B2.
* O sensor de peça tem de ser acionado, indicando que existe uma peça a ser furada.
* *A área de segurança protegida por uma cortina de luz, sensor S2, não pode ser invadida.
* O sensor de início de curso S4 deve estar acionado, indicando que a furadeira se encontra na posição inicial do processo.
* A botoeira de emergência e o sensor S7 de sobrecarga do motor não podem estar acionados.

Nessas condições, a lâmpada L1 deve acender e o contator de acionamento de descida do motor deve ser acionado. Quando o sensor S3 é acionado, o contator que propicia a descida da furadeira deve ser desligado e o contator que propicia a subida do conjunto deve ser acionado. O motor da furadeira tem de ser desligado quando o sensor S4 for acionado novamente. A qualquer momento em que uma das botoeiras do operador deixar de ser acionada, S7 apresentar sobrecarga, S1 detectar a ausência de peça ou a cortina de luz for invadida, o processo de descida ou subida com o motor da furadeira acionado deve ser interrompido. Esse processo somente pode ser reiniciado com as condições iniciais de operação garantidas (subindo quando interrompido na subida e descendo quando interrompido na descida).
                 ''')
        
        st.divider()
        
        fatores = st.columns(3)
        
        # Adicionando checkbox para simular as entradas e sensores
        
        with fatores[0]:
            st.write('Furadeira')
            b1 = st.checkbox("B1 - Mão Esquerda")
            b2 = st.checkbox("B2 - Mão Direita")
            
        with fatores[1]:
            st.write('Sensores')
            s1 = st.checkbox("S1 - Presência de Peça")
            s2 = st.checkbox("S2 - Cortina de Luz Invadida")
            s3 = st.checkbox("S3 - Sensor de Fim de Curso")
            s4 = st.checkbox("S4 - Sensor de Início de Curso")
            
        with fatores[2]:
            st.error('Emergência')
            e_stop = st.checkbox("Botão de Emergência (E-STOP)")
            s7 = st.checkbox("S7 - Sobrecarga do Motor")
        
        st.divider()
        
        furadeira_bancada_simulador(b1, b2, s2, s4, s3, s1, s7, e_stop)
        
    st.header('Conclusão')
    
    with st.expander('Resolução'):
        st.write('''
                 A utilização do simulador LogixPro permitiu validar o código Ladder desenvolvido e o seu funcionamento, proporcionando uma visualização clara do comportamento do sistema em diferentes cenários. A criação de uma representação dinâmica em Python, utilizando a biblioteca Streamlit, teve como objetivo a compreensão do funcionamento do programa Ladder de forma mais visual, tornando-o mais acessível e didático.
                 
Durante a simulação, observamos que a lógica implementada respondeu de maneira consistente às condições de entrada e sensores, acionando corretamente as saídas esperadas, como indicado pelas lâmpadas e contatos simulados. A interface gráfica proporcionou uma experiência interativa, facilitando a compreensão do sistema e fornecendo uma representação visual clara das condições de operação.

Em resumo, a implementação do projeto buscou demonstrar a eficácia da linguagem Ladder na automação de sistemas industriais, enquanto a representação dinâmica proporciona uma abordagem didática para um maior aprendizado e comunicação efetiva dos conceitos de automação.
                 ''')

if __name__ == "__main__":
    main()
