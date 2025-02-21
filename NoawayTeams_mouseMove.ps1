# Adiciona uma definição de tipo C# dentro do PowerShell
# Adds a C# type definition inside PowerShell
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class MouseMover {
    // Importa a função SetCursorPos da biblioteca user32.dll para mover o cursor do rato
    // Imports the SetCursorPos function from user32.dll to move the mouse cursor
    [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
    public static extern bool SetCursorPos(int x, int y);
}
"@ -Language CSharp

# Inicia um loop infinito para manter o cursor em movimento
# Starts an infinite loop to keep the cursor moving
while ($true) {
    # Move o cursor do rato para a posição (500, 500)
    # Moves the mouse cursor to position (500, 500)
    [MouseMover]::SetCursorPos(500, 500)

    # Aguarda 30 segundos antes de mover novamente
    # Waits 30 seconds before moving again
    Start-Sleep -Seconds 30

    # Move o cursor do rato ligeiramente para (505, 505) para simular atividade
    # Moves the mouse cursor slightly to (505, 505) to simulate activity
    [MouseMover]::SetCursorPos(505, 505)

    # Aguarda mais 30 segundos antes do próximo ciclo
    # Waits another 30 seconds before the next cycle
    Start-Sleep -Seconds 30
}
