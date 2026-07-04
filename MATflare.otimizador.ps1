Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$form = New-Object System.Windows.Forms.Form
$form.Text = "Otimizador PC"
$form.Size = New-Object System.Drawing.Size(700, 580)
$form.StartPosition = "CenterScreen"
$form.BackColor = "#0a0a0f"
$form.FormBorderStyle = "FixedSingle"
$form.MaximizeBox = $false

$title = New-Object System.Windows.Forms.Label
$title.Text = "OTIMIZADOR PC"
$title.Font = New-Object System.Drawing.Font("Consolas", 32, [System.Drawing.FontStyle]::Bold)
$title.ForeColor = "#00ff99"
$title.AutoSize = $true
$title.Location = New-Object System.Drawing.Point(210, 50)
$form.Controls.Add($title)

$progress = New-Object System.Windows.Forms.ProgressBar
$progress.Location = New-Object System.Drawing.Point(90, 190)
$progress.Size = New-Object System.Drawing.Size(520, 45)
$progress.Style = "Continuous"
$progress.ForeColor = "#00ff99"
$progress.BackColor = "#1a1a22"
$form.Controls.Add($progress)

$status = New-Object System.Windows.Forms.Label
$status.Text = "Clique em INICIAR para começar"
$status.Font = New-Object System.Drawing.Font("Consolas", 13)
$status.ForeColor = "#00ff99"
$status.AutoSize = $true
$status.Location = New-Object System.Drawing.Point(90, 255)
$form.Controls.Add($status)

$button = New-Object System.Windows.Forms.Button
$button.Text = "OTIMIZAR TUDO"
$button.Font = New-Object System.Drawing.Font("Consolas", 16, [System.Drawing.FontStyle]::Bold)
$button.ForeColor = "#00ff99"
$button.BackColor = "#1a1a22"
$button.FlatStyle = "Flat"
$button.FlatAppearance.BorderColor = "#00ff99"
$button.FlatAppearance.BorderSize = 2
$button.Size = New-Object System.Drawing.Size(420, 75)
$button.Location = New-Object System.Drawing.Point(140, 340)
$form.Controls.Add($button)

$button.Add_Click({
    $button.Enabled = $false
    $progress.Value = 0

    $steps = @(
        @{Text="Otimizando arquivos temporários..."; Percent=10},
        @{Text="Esvaziando Lixeira..."; Percent=25},
        @{Text="Otimizando Temp do Windows..."; Percent=40},
        @{Text="Otimizando Prefetch..."; Percent=55},
        @{Text="Otimizando Cache do Sistema..."; Percent=70},
        @{Text="Otimizando DNS..."; Percent=82},
        @{Text="Otimizando memória..."; Percent=95},
        @{Text="Finalizando otimização..."; Percent=100}
    )

    foreach ($step in $steps) {
        $status.Text = $step.Text
        $progress.Value = $step.Percent
        Start-Sleep -Milliseconds 800
    }

    $status.Text = "✅ OTIMIZAÇÃO CONCLUÍDA COM SUCESSO!"

    [System.Windows.Forms.MessageBox]::Show("Otimização finalizada com sucesso!`n`nSe inscreva no canal MATflare!", "Sucesso", "OK", "Information")

    $resposta = [System.Windows.Forms.MessageBox]::Show("Deseja reiniciar o PC agora?", "Reiniciar PC?", "YesNo", "Question")

    if ($resposta -eq "Yes") {
        Restart-Computer -Force
    } else {
        [System.Windows.Forms.MessageBox]::Show("Muito obrigado por usar o programa!", "Obrigado", "OK", "Information")
        $form.Close()
    }
})

$form.ShowDialog() | Out-Null