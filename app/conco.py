import pywhatkit
import pandas as pd 


clientes = pd.read_csv("base/base_robo_claro.csv", sep=";", encoding="UTF-8")


for cliente in range(len(clientes)):

        mensagem = f"Está disponível para empresa, {clientes.loc[cliente, 'Razão Social']}, uma excelente condição, para que possa ser um cliente de telefonia móvel da Vivo Empresas.\n 1. Tenho interesse em saber mais;\n 2.Não tenho interesse em melhorar a condição do meu plano e tão pouco reduzir o valor da minha conta de telefonia móvel." )
        
        pywhatkit.sendwhatmsg_instantly(phone_no=f"+55{int(clientes.loc[cliente, 'Telefone de Contato'])}", message = mensagem, wait_time = 40, tab_close = True )
        
     


