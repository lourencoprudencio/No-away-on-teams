import pyautogui  # Controla o cursor do rato
import time  # Adiciona pausas no script
import threading  # Permite verificar a opção de saída sem interromper o loop principal
from datetime import datetime  # Importa datetime para exibir a hora exata

# Variável global para controlar a execução do script
executando = True

# Função para o menu de escolha de tempo de ativação do script
def escolher_tempo():
    print("\nEscolhe de quanto em quanto tempo o script é executado:")
    print("1 - 1 minuto")
    print("2 - 2 minutos")
    print("3 - 3 minutos")
    print("4 - 4 minutos")
    print("5 - 5 minutos")
    print("6 - Personalizado")
    print("7 - Fechar o script")  # Opção para encerrar o script

    tempos = {
        1: 60,   # 1 minuto
        2: 120,  # 2 minutos
        3: 180,  # 3 minutos
        4: 240,  # 4 minutos
        5: 300,  # 5 minutos
    }

    try:
        opcao = int(input("Indica de quanto em quanto tempo o script é executado: "))

        if opcao in tempos:
            return tempos[opcao]  # Retorna o tempo correspondente
        
        elif opcao == 6:
            tempo_personalizado = int(input("Indica o tempo em segundos: "))  
            if tempo_personalizado > 0:
                return tempo_personalizado  

        elif opcao == 7:
            print("🛑 Script encerrado pelo user.")
            exit()  

    except ValueError:
        pass  

    print("O valor é inválido! Iniciado com o valor padrão de 4 minutos.")
    return 240  

# Função para verificar se o user quer encerrar o script enquanto ele está a correr
def verificar_saida():
    global executando
    while executando:
        opcao_sair = input("\n❓ Escreve '7' para fechar o script a qualquer momento: ").strip()
        if opcao_sair == "7":
            print("🛑 Script encerrado pelo user.")
            executando = False  # Altera o estado da variável global para encerrar o loop principal

# Chama a função para definir o intervalo de tempo
intervalo = escolher_tempo()

print("🟢 Script iniciado! O Microsoft Teams não vai ficar ausente.")
print("🔴 Para parar, fecha esta janela ou digita '7' para encerrar.")

# Inicia a thread que permite ao user encerrar o script enquanto ele está a ser executado
thread_verificacao = threading.Thread(target=verificar_saida, daemon=True)
thread_verificacao.start()

# Loop principal que mantém o script ativo
while executando:
    x, y = pyautogui.position()  # Recebe a posição atual do cursor
    pyautogui.moveTo(x + 1, y)  # Mexe o cursor 1 pixel para a direita
    time.sleep(0.5)
    pyautogui.moveTo(x, y)  # Mexe de volta o cursor à posição original

    # Eecebe a hora atual e formata HH:MM:SS
    hora_atual = datetime.now().strftime("%H:%M:%S")
    
    # Mensagem com o horário da execução
    print(f"🖱 Mouse movimentado com sucesso - {hora_atual}")

    time.sleep(intervalo)  # Aguarda o tempo definido antes da próxima execução

print("✅ O script foi finalizado com sucesso.")  