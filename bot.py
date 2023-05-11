import time
from datetime import datetime, timedelta
import win32serviceutil

tempo_atual = time.strftime('%H:%M', time.localtime()) # obtem a hora atual da maquina
data_inicio = datetime.strptime(tempo_atual, "%H:%M") # transforma a string em data

hora_atual = data_inicio.strftime('%H:%M:00') #variavel hora atual para comparar com a do arquivo de log

dir = r'C:\C5Client\C5Servico\C5LiberaCargaExpedService\Logs\ExecLog.consinco' #diretorio arqv de log
    
with open(dir) as file:
    content = file.readlines()
    hr_atual_no_arqv = content[0][11:19] #obtem valor que está como "hora atual" no arquivo

    file.close()

if hora_atual != hr_atual_no_arqv :

    intervalo = '00:02'
    horas, minutos = map(int, intervalo.split(':'))

    # transforma a string em timedelta
    intervalo = timedelta(hours=horas, minutes=minutos)

    # soma a data à duração
    new_time = data_inicio + intervalo

    # formata o resultado
    hora = new_time.strftime('%H:%M')

    arquivo = open(r'C:\C5Client\C5Servico\C5LiberaCargaExpedService\C5LiberaCargaExpedService.config.consinco', 'w')

    arquivo.write('1|'+ hora +'|||||')
    arquivo.close()

    # reinicia o serviço 
    try:
        servico = "C5LiberaCargaExpedService"
        win32serviceutil.RestartService(servico)
        print('Serviço reiniciado com sucesso')
    except Exception as e:
        print(f'Não foi possível reiniciar o serviço {servico}: {e}')          
else:
    pass


