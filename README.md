# 🟢 NoAwayTeams – Impede que o Microsoft Teams te marque como "Ausente"

## 🌟 Versão em Português

Este repositório contém **três scripts** que impedem que o Microsoft Teams te marque como **Ausente/Inativo**, garantindo que o teu status permaneça como **"Disponível"** enquanto o script está em execução.

## 🔧 Como Funciona?

Cada script simula atividade no computador, evitando que o Teams ou outras aplicações considerem a tua sessão inativa.

- **NoawayTeams\_mouseMove.py** → Move ligeiramente o cursor do rato a cada X minutos.
- **NoawayTeams\_keyboardPress.py** → Simula o pressionamento da tecla "Scroll Lock" a cada X minutos.
- **NoawayTeams\_PowerShell.ps1** → Move o cursor do rato ligeiramente a cada 30 segundos através de um script em PowerShell.

## 🌟 Scripts Disponíveis

### 1️⃣ `NoawayTeams_mouseMove.py`

🖱 **Movimenta ligeiramente o rato** para simular atividade.

✔️ Mantém a sessão ativa sem pressionar teclas.\
✔️ Funciona mesmo se estiveres a assistir a vídeos ou apresentações.\
❌ Pode interferir em jogos ou em aplicações sensíveis ao movimento do rato.

### 2️⃣ `NoawayTeams_keyboardPress.py`

💪 **Simula o pressionamento da tecla "Scroll Lock"**.

✔️ Não mexe no rato, sendo ideal para quem usa múltiplos monitores.\
✔️ Tecla "Scroll Lock" não afeta a maioria dos softwares.

### 3️⃣ `NoawayTeams_PowerShell.ps1`

🔠 **Executa um comando PowerShell que move ligeiramente o cursor do rato a cada 30 segundos.**

✔️ Solução rápida e leve, sem necessidade de instalar dependências.\
✔️ Pode ser executado em segundo plano no Windows.\
✔️ Cada vez que o script é executado, retorna "True" na consola.

## 🛠 Como Usar?

### 1️⃣ **Instala as dependências (para scripts Python)**

Certifica-te de que tens o Python instalado e instala as dependências:

```sh
pip install pyautogui
```

### 2️⃣ **Executa o script**

Escolhe o script e executa-o no terminal:

```sh
python NoawayTeams_mouseMove.py
```

ou

```sh
python NoawayTeams_keyboardPress.py
```

Para o PowerShell, primeiro executa este comando:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Depois, podes correr o script de uma das seguintes formas:
- **Clicar com o botão direito do rato** sobre o ficheiro `.ps1` e selecionar **Run with PowerShell**
- **Abrir um terminal PowerShell** e copiar o conteúdo do `.ps1` para execução manual
- **Executar diretamente o script** no PowerShell com o comando:

```powershell
powershell -ExecutionPolicy Bypass -File .\NoawayTeams_PowerShell.ps1
```

### 3️⃣ **Escolhe um intervalo de tempo (para scripts Python)**

O menu interativo permitirá escolher de quanto em quanto tempo o script será executado:

```
Escolhe de quanto em quanto tempo o script é executado:
1 - 1 minuto
2 - 2 minutos
3 - 3 minutos
4 - 4 minutos
5 - 5 minutos
6 - Personalizado
7 - Fechar o script
```

Para parar o script, **fecha a janela do terminal** ou escreve **"7"** no terminal.

## 📌 Dicas

✅ **Se baixares a tampa do portátil**, os scripts continuam a funcionar.\
✅ **Funciona em trabalho remoto** sem necessidade de interação manual.\
✅ **Executa em segundo plano** sem atrapalhar o teu fluxo de trabalho.

---

## 🚀 Contribuições

Não hesite em contribuir abrindo um **Pull Request** ou sugerir melhorias na seção **Issues**. 😊

## 📝 Licença

Este projeto está disponível sob a licença **MIT**. O user é livre de o utilizar e modificar conforme necessário.

### 🔥 Agora podes manter o teu estado “Disponível” no Teams sem preocupações! 🚀

---

# 🇬🇧 🟢 NoAwayTeams – Prevents Microsoft Teams from Marking You as "Away"

## 🔧 How It Works?

This repository contains **three scripts** that prevent Microsoft Teams from marking you as **Away/Inactive**, ensuring your status remains **"Available"** while the script is running.

- **NoawayTeams\_mouseMove.py** → Moves the mouse cursor slightly every X minutes.
- **NoawayTeams\_keyboardPress.py** → Simulates a "Scroll Lock" key press every X minutes.
- **NoawayTeams\_PowerShell.ps1** → Moves the mouse cursor slightly every 30 seconds using a PowerShell script.

## 🌟 Available Scripts

### 1️⃣ `NoawayTeams_mouseMove.py`

🖱 **Slightly moves the mouse** to simulate activity.

✔️ Keeps your session active without pressing keys.\
✔️ Works even if you're watching videos or presentations.\
❌ May interfere with games or applications that rely on mouse movement.

### 2️⃣ `NoawayTeams_keyboardPress.py`

💪 **Simulates pressing the "Scroll Lock" key**.

✔️ Does not move the mouse, ideal for multi-monitor setups.\
✔️ "Scroll Lock" key does not affect most software.

### 3️⃣ `NoawayTeams_PowerShell.ps1`

🔠 **Runs a PowerShell command that moves the mouse cursor slightly every 30 seconds.**

✔️ Fast and lightweight solution, no dependencies required.\
✔️ Can run in the background on Windows.\
✔️ Each time the script is executed, it returns "True" in the console.

## 🛠 How to Use?

For Python scripts, install dependencies:

```sh
pip install pyautogui
```

Run the script:

```sh
python NoawayTeams_mouseMove.py
```

or

```sh
python NoawayTeams_keyboardPress.py
```

For PowerShell, first run:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then execute the script by:
- **Right-clicking** the `.ps1` file and selecting **Run with PowerShell**
- **Opening PowerShell**, copying the `.ps1` contents, and running manually
- **Running the script directly** in PowerShell with:

```powershell
powershell -ExecutionPolicy Bypass -File .\NoawayTeams_PowerShell.ps1
```
