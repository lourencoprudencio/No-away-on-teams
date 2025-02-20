import time  # Pausas no script / Script pauses
import ctypes  # Manipula funções do SO / Handles OS functions
import threading  # Permite verificar a opção de saída sem interromper o loop principal / Allows exit option check without interrupting main loop
from datetime import datetime  # Exibe a hora exata da execução / Displays exact execution time

# Variável global para controlar a execução do script / Global variable to control script execution
executando = True

# Função para o menu de escolha de tempo de ativação do script / Function for selecting script execution interval
def escolher_tempo():
    print("\nEscolhe de quanto em quanto tempo o script é executado:")  # Select how often the script runs
    print("1 - 1 minuto / 1 minute")
    print("2 - 2 minutos / 2 minutes")
    print("3 - 3 minutos / 3 minutes")
    print("4 - 4 minutos / 4 minutes")
    print("5 - 5 minutos / 5 minutes")
    print("6 - Personalizado / Custom")
    print("7 - Fechar o script / Close the script")

    tempos = {
        1: 60,   # 1 minuto / 1 minute
        2: 120,  # 2 minutos / 2 minutes
        3: 180,  # 3 minutos / 3 minutes
        4: 240,  # 4 minutos / 4 minutes
        5: 300,  # 5 minutos / 5 minutes
    }

    try:
        opcao = int(input("Indica de quanto em quanto tempo o script é executado: "))  # Specify script execution interval

        if opcao in tempos:
            return tempos[opcao]  # Retorna o tempo correspondente / Returns the corresponding time
        
        elif opcao == 6:
            tempo_personalizado = int(input("Indica o tempo em segundos: "))  # Specify time in seconds
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
            executando = False  # Encerra o loop principal / Ends the main loop

# Função para simular uma tecla pressionada (Scroll Lock) / Function to simulate a key press (Scroll Lock)
def manter_ativo():
    while executando:
        ctypes.windll.user32.keybd_event(0x91, 0, 0, 0)  # Pressiona Scroll Lock / Press Scroll Lock
        time.sleep(0.1)
        ctypes.windll.user32.keybd_event(0x91, 0, 2, 0)  # Solta Scroll Lock / Release Scroll Lock
        
        # Obtém a hora atual e formata em HH:MM:SS / Get current time and format as HH:MM:SS
        hora_atual = datetime.now().strftime("%H:%M:%S")
        print(f"🕒 Tecla pressionada - {hora_atual}")  # Key pressed message with exact time

        time.sleep(intervalo)  # Espera o tempo definido antes de repetir / Waits the defined time before repeating

# Chama a função para definir o intervalo de tempo / Calls the function to set the time interval
intervalo = escolher_tempo()

print("🟢 Script iniciado! O Microsoft Teams não vai ficar ausente. / Script started! Microsoft Teams won't show you as away.")
print("🔴 Para parar, fecha esta janela ou digita '7' para encerrar. / To stop, close this window or type '7' to exit.")

# Inicia a thread que permite ao user encerrar o script enquanto ele está em execução
# Starts the thread that allows the user to stop the script while running
thread_verificacao = threading.Thread(target=verificar_saida, daemon=True)
thread_verificacao.start()

# Inicia a thread para simular teclas no background / Starts the thread to simulate key presses in the background
thread_teclado = threading.Thread(target=manter_ativo, daemon=True)
thread_teclado.start()

# Mantém o script ativo enquanto "executando" for True / Keeps the script running while "executando" is True
while executando:
    time.sleep(1)  # Mantém o loop ativo até o usuário encerrar / Keeps the loop running until user stops it

print("✅ O script foi finalizado com sucesso. / The script was successfully terminated.")
