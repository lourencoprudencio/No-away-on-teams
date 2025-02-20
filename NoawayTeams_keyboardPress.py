import time  # Pausas no script
import ctypes  # Manipula funções do SO
import threading  # Permite verificar a opção de saída sem interromper o loop principal
from datetime import datetime  # Exibe a hora exata da execução

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
    print("7 - Fechar o script")

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
            executando = False  # Encerra o loop principal

# Função para simular uma tecla pressionada (Scroll Lock)
def manter_ativo():
    while executando:
        ctypes.windll.user32.keybd_event(0x91, 0, 0, 0)  # Pressiona Scroll Lock
        time.sleep(0.1)
        ctypes.windll.user32.keybd_event(0x91, 0, 2, 0)  # Solta Scroll Lock
        
        # Obtém a hora atual e formata em HH:MM:SS
        hora_atual = datetime.now().strftime("%H:%M:%S")
        print(f"🕒 Tecla pressionada - {hora_atual}")  # Mensagem com a hora exata

        time.sleep(intervalo)  # Espera o tempo definido antes de repetir

# Chama a função para definir o intervalo de tempo
intervalo = escolher_tempo()

print("🟢 Script iniciado! O Microsoft Teams não vai ficar ausente.")
print("🔴 Para parar, fecha esta janela ou digita '7' para encerrar.")

# Inicia a thread que permite ao user encerrar o script enquanto ele está em execução
thread_verificacao = threading.Thread(target=verificar_saida, daemon=True)
thread_verificacao.start()

# Inicia a thread para simular teclas no background
thread_teclado = threading.Thread(target=manter_ativo, daemon=True)
thread_teclado.start()

# Mantém o script ativo enquanto "executando" for True
while executando:
    time.sleep(1)  # Mantém o loop ativo até o usuário encerrar

print("✅ O script foi finalizado com sucesso.") 
