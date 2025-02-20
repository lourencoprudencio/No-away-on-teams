# 🟢 NoAwayTeams – Impede que o Microsoft Teams te marque como "Ausente"

## 🇵🇹 Versão em Português

Este repositório contém **dois scripts Python** que impedem que o Microsoft Teams te marque como **Ausente/Inativo**, garantindo que o teu status permaneça como **"Disponível"** enquanto o script está em execução.

## 🔧 Como Funciona?

Cada script simula atividade no computador, evitando que o Teams ou outras aplicações considerem a tua sessão inativa.

- **NoawayTeams\_mouseMove.py** → Move ligeiramente o cursor do rato a cada X minutos.
- **NoawayTeams\_keyboardPress.py** → Simula o pressionamento da tecla "Scroll Lock" a cada X minutos.

## 📜 Scripts Disponíveis

### 1️⃣ `NoawayTeams_mouseMove.py`

🖱 **Movimenta ligeiramente o rato** para simular atividade.

✔️ Mantém a sessão ativa sem pressionar teclas. ✔️ Funciona mesmo se estiveres a assistir a vídeos ou apresentações. ❌ Pode interferir em jogos ou em aplicações sensíveis ao movimento do rato.

### 2️⃣ `NoawayTeams_keyboardPress.py`

⌨️ **Simula o pressionamento da tecla "Scroll Lock"**.

✔️ Não mexe no rato, sendo ideal para quem usa múltiplos monitores. ✔️ Tecla "Scroll Lock" não afeta a maioria dos softwares.

## 🛠 Como Usar?

### 1️⃣ **Instala as dependências**

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

### 3️⃣ **Escolhe um intervalo de tempo**

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

✅ **Se baixares a tampa do portátil**, os scripts continuam a funcionar. ✅ **Funciona em trabalho remoto** sem necessidade de interação manual. ✅ **Executa em segundo plano** sem atrapalhar o teu fluxo de trabalho.

---

## 🚀 Contribuições

Não hesite em contribuir abrindo um **Pull Request** ou sugerir melhorias na secção **Issues**. 😊

## 📜 Licença

Este projeto está disponível sob a licença **MIT**. O user é livre de o utilizar e modificar conforme necessário.

### 🔥 Agora podes manter o teu estado “Disponível” no Teams sem preocupações! 🚀

---

# 🇬🇧 NoAwayTeams – Prevents Microsoft Teams from Marking You as "Away"

## 🔧 How It Works?

This repository contains **two Python scripts** that prevent Microsoft Teams from marking you as **Away/Inactive**, ensuring your status remains **"Available"** while the script is running.

- **NoawayTeams\_mouseMove.py** → Moves the mouse cursor slightly every X minutes.
- **NoawayTeams\_keyboardPress.py** → Simulates a "Scroll Lock" key press every X minutes.

## 📜 Available Scripts

### 1️⃣ `NoawayTeams_mouseMove.py`

🖱 **Slightly moves the mouse** to simulate activity.

✔️ Keeps your session active without pressing keys. ✔️ Works even if you're watching videos or presentations. ❌ May interfere with games or applications that rely on mouse movement.

### 2️⃣ `NoawayTeams_keyboardPress.py`

⌨️ **Simulates pressing the "Scroll Lock" key**.

✔️ Does not move the mouse, ideal for multi-monitor setups. ✔️ "Scroll Lock" key does not affect most software.

## 🛠 How to Use?

### 1️⃣ **Install dependencies**

Make sure you have Python installed and install the necessary dependencies:

```sh
pip install pyautogui
```

### 2️⃣ **Run the script**

Choose a script and run it in the terminal:

```sh
python NoawayTeams_mouseMove.py
```

or

```sh
python NoawayTeams_keyboardPress.py
```

### 3️⃣ **Choose a time interval**

An interactive menu will allow you to choose how often the script executes:

```
Choose how often the script executes:
1 - 1 minute
2 - 2 minutes
3 - 3 minutes
4 - 4 minutes
5 - 5 minutes
6 - Custom
7 - Exit script
```

To stop the script, **close the terminal window** or type **"7"**.

## 📌 Tips

✅ **If you close the laptop lid**, the scripts continue running. ✅ **Works for remote work** without manual interaction. ✅ **Runs in the background** without disrupting your workflow.

---

## 🚀 Contributions

Feel free to contribute by opening a **Pull Request** or suggesting improvements in the **Issues** section. 😊

## 📜 License

This project is available under the **MIT License**. You are free to use and modify it as needed.

### 🔥 Now you can keep your "Available" status on Teams without worries! 🚀

