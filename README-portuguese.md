# Aplicativo Interativo
[README em inglês](./README.md)
## Descrição
Esse repositório contém a solução para um desafio inicial de um curso de Arduino.

Imagine que você está desenvolvendo um aplicativo de monitoramento para uma horta inteligente, equipada com sensores de umidade, temperatura e luminosidade. Sua tarefa é projetar um menu interativo para essa aplicação. Como você estruturaria e implementaria um menu que permita ao usuário visualizar as leituras atuais dos sensores, ajustar configurações de alerta para cada sensor (por exemplo, definir um limite mínimo de umidade). Descreva a lógica do menu, as opções disponíveis para o usuário e como você lidaria com a entrada do usuário para navegar entre as diferentes funcionalidades do aplicativo.

Na minha solução eu implementei Python com Streamlit para desenvolver uma pagina web que usuários possam interagir para configurar valores minimos e máximos para os sensores.

Você pode checar o resultado da minha solução em: [Render Deployed](https://arduino-final-test.onrender.com/)


## Tecnologias usadas
1. Python
2. Render
3. Streamlit

> [!NOTE]
> Já que o Render é grátis, talvez nos próximos meses a página não esteja disponível, tente acessar e aguardar alguns minutos para o Render iniciar o servidor web.

## Como Replicar e Executar a Aplicação
1. Clone o repositório
2. Crie um ambiente virtual com `py -m venv venv`
3. Ative o ambiente virtual (este passo pode variar dependendo do seu sistema operacional):
```.\venv\Scripts\activate```
4. Instale as dependências do projeto com `pip install -r requirements.txt`
5. Execute o servidor da aplicação usando o comando `streamlit run main.py`
6. Acesse o link fornecido pelo streamlit
