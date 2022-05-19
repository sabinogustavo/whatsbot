import pywhatkit
import pandas as pd 

clientes = pd.read_csv("base/clientes_migracao.csv", sep=";", encoding="ISO-8859-1")


for cliente in range(len(clientes)):
        message = f"Olá, tudo bem?"
        message1 = f"Você é responsável pelas linhas móveis da empresa {clientes.loc[cliente, 'CLIENTE']}?"
        message2 = f"Caso sim me contate, pois tenho uma proposta de renovação antecipada do seu plano com redução de até 20% e melhoria no pacote de dados."
        message3 = f"Se não for responsável, poderia me indicar como encontrá-lo?"
        message4 = f"Obrigada"
        mensagens = (message, message1, message2, message3)
        i = 1
        for mensagem in mensagens:
            pywhatkit.sendwhatmsg_instantly(phone_no=f"+55{int(clientes.loc[cliente, 'NR_TELEFONE'])}", message = mensagem, wait_time = 40, tab_close = True )
        
            i+=1
     


