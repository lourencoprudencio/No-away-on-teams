import pyautogui  # Controla o cursor do rato / Controls the mouse cursor
import time  # Adiciona pausas no script / Adds pauses to the script
import threading  # Permite verificar a opção de saída sem interromper o loop principal / Allows exit check without interrupting the main loop
from datetime import datetime, timedelta  # Importa datetime para exibir a hora exata / Imports datetime to display the exact time

# Variável global para controlar a execução do script / Global variable to control script execution
executando = True

# Função para o menu de escolha de tempo de ativação do script / Function to choose the script execution interval
def escolher_tempo():
    print("\nEscolhe de quanto em quanto tempo o script é executado / Choose how often the script is executed:")  # Choose how often the script runs
    print("1 - 1 minuto / 1 minute")
    print("2 - 2 minutos / 2 minutes")
    print("3 - 3 minutos / 3 minutes")
    print("4 - 4 minutos / 4 minutes")
    print("5 - 5 minutos / 5 minutes")
    print("6 - Personalizado / Custom")
    print("7 - Fechar o script / Close the script")  # Option to stop the script

    tempos = {
        1: 60,   # 1 minuto / 1 minute
        2: 120,  # 2 minutos / 2 minutes
        3: 180,  # 3 minutos / 3 minutes
        4: 240,  # 4 minutos / 4 minutes
        5: 300,  # 5 minutos / 5 minutes
    }

    try:
        opcao = int(input("Indica de quanto em quanto tempo o script é executado / Indicates how often the script is executed: "))  # Specify how often the script runs

        if opcao in tempos:
            return tempos[opcao]  # Retorna o tempo correspondente / Returns the corresponding time
        
        elif opcao == 6:
            tempo_personalizado = int(input("Indica o tempo em segundos / Indicates the time in seconds: "))  # Specify time in seconds
            if tempo_personalizado > 0:
                return tempo_personalizado  

        elif opcao == 7:
            print("🛑 Script encerrado pelo user. / Script stopped by user.")
            exit()  

    except ValueError:
        pass  

    print("O valor é inválido! Iniciado com o valor padrão de 4 minutos. / Invalid value! Starting with the default 4-minute setting.")
    return 240  

# Função para verificar se o user quer encerrar o script enquanto ele está a correr
# Function to check if the user wants to stop the script while it's running
def verificar_saida():
    global executando
    while executando:
        opcao_sair = input("\n❓ Escreve '7' para fechar o script a qualquer momento: ").strip()  # Type '7' to stop the script anytime
        if opcao_sair == "7":
            print("🛑 Script encerrado pelo user. / Script stopped by user.")
            executando = False  # Altera o estado da variável global para encerrar o loop principal / Changes global variable state to stop main loop

# Chama a função para definir o intervalo de tempo / Calls the function to set the execution interval
intervalo = escolher_tempo()

print("🟢 Script iniciado! O Microsoft Teams não vai ficar ausente. / Script started! Microsoft Teams won't show you as away.")
print("🔴 Para parar, fecha esta janela ou digita '7' para encerrar. / To stop, close this window or type '7' to exit.")

# Inicia a thread que permite ao user encerrar o script enquanto ele está a ser executado
# Starts the thread that allows the user to stop the script while running
thread_verificacao = threading.Thread(target=verificar_saida, daemon=True)
thread_verificacao.start()

# Loop principal que mantém o script ativo / Main loop that keeps the script running
while executando:
    x, y = pyautogui.position()  # Recebe a posição atual do cursor / Gets the current cursor position
    pyautogui.moveTo(x + 1, y)  # Mexe o cursor 1 pixel para a direita / Moves the cursor 1 pixel to the right
    time.sleep(0.5)
    pyautogui.moveTo(x, y)  # Mexe de volta o cursor à posição original / Moves the cursor back to the original position

    # Recebe a hora atual e formata HH:MM:SS / Gets the current time and formats as HH:MM:SS
    hora_atual = datetime.now().strftime("%H:%M:%S")
    proximo_movimento = (datetime.now() + timedelta(seconds=intervalo)).strftime("%H:%M:%S")  # Calcula o próximo movimento / Calculates next movement time
    
    # Mensagem com o horário da execução e o próximo movimento / Message with execution time and next movement
    print(f"🖱 Mouse movimentado com sucesso - {hora_atual} / Mouse moved successfully - {hora_atual} / Próximo Movimento do mouse - {proximo_movimento} / Next mouse move - {proximo_movimento}")

    time.sleep(intervalo)  # Aguarda o tempo definido antes da próxima execução / Waits for the defined interval before the next execution

print("✅ O script foi finalizado com sucesso. / The script was successfully terminated.")