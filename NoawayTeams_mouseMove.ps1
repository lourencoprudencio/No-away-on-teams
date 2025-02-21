Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class MouseMover {
    [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
    public static extern bool SetCursorPos(int x, int y);
}
"@ -Language CSharp

while ($true) {
    [MouseMover]::SetCursorPos(500, 500)
    Start-Sleep -Seconds 30
    [MouseMover]::SetCursorPos(505, 505)
    Start-Sleep -Seconds 30
}
