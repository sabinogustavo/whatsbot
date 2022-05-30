import pywhatkit
import pandas as pd 

base = f"base/{input('Insira o nome do arquivo a ser utilizado: ')}.csv"
clientes = pd.read_csv(base, sep=";", encoding="ISO-8859-1")


for cliente in range(len(clientes)):
        mensagens = (
            f"Olá, tudo bem?",
            f"Você é responsável pelas linhas móveis da empresa {clientes.loc[cliente, 'CLIENTE']}?",
            f"Caso sim me contate, pois tenho uma proposta de renovação antecipada do seu plano com redução de até 20% e melhoria no pacote de dados.",
            f"Se não for responsável, poderia me indicar como encontrá-lo?",
            f"Obrigada"
        )
        i = 1
        for mensagem in mensagens:
            pywhatkit.sendwhatmsg_instantly(phone_no=f"+55{int(clientes.loc[cliente, 'NR_TELEFONE'])}", message = mensagem, wait_time = 40, tab_close = True )
            i+=1
     


