import psutil
import GPUtil
import time
import tkinter as tk
from tkinter import ttk
import threading

class PC_Monitor_Luxo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aether Monitor • Elite System")
        self.root.geometry("560x480")
        self.root.configure(bg="#0a0a12")
        self.root.resizable(False, False)

        # Fundo chique (gradiente + estilo rico)
        self.create_background()

        self.create_widgets()
        self.update_data()

    def create_background(self):
        # Canvas para fundo bonito
        self.canvas = tk.Canvas(self.root, width=560, height=480, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Gradiente escuro luxuoso
        for i in range(480):
            color = f"#{10:02x}{max(10, 20-i//8):02x}{max(18, 40-i//6):02x}"
            self.canvas.create_line(0, i, 560, i, fill=color)

        # Efeito de brilho sutil
        self.canvas.create_rectangle(0, 0, 560, 120, fill="#1a1a2e", stipple="gray50")

    def create_widgets(self):
        # Título luxuoso
        title = tk.Label(self.root, text="AETHER MONITOR", 
                        font=("Helvetica", 26, "bold"), 
                        fg="#00ffcc", bg="#1a1a2e")
        title.place(x=140, y=25)

        subtitle = tk.Label(self.root, text="SYSTEM STATUS • ELITE", 
                          font=("Helvetica", 9), fg="#666699", bg="#1a1a2e")
        subtitle.place(x=210, y=55)

        # Frame central transparente
        frame = tk.Frame(self.root, bg="#111118", bd=2, relief="solid", highlightbackground="#00ffcc", highlightthickness=1)
        frame.place(x=40, y=100, width=480, height=320)

        self.labels = {}
        infos = [
            ("CPU", "Processor"),
            ("RAM", "Memory"),
            ("GPU", "Graphics"),
            ("Bateria", "Power"),
            ("Temperatura", "Thermal"),
            ("Status", "System")
        ]

        for i, (key, label_text) in enumerate(infos):
            # Nome do sensor
            tk.Label(frame, text=label_text, font=("Helvetica", 11), 
                    fg="#8888aa", bg="#111118").place(x=30, y=25 + i*45)
            
            # Valor
            self.labels[key] = tk.Label(frame, text="•••", 
                                      font=("Helvetica", 16, "bold"),
                                      fg="#00ffcc", bg="#111118")
            self.labels[key].place(x=220, y=22 + i*45)

    def update_data(self):
        def refresh():
            while True:
                try:
                    # CPU
                    cpu = psutil.cpu_percent()
                    self.labels["CPU"].config(text=f"{cpu}%")

                    # RAM
                    ram = psutil.virtual_memory().percent
                    self.labels["RAM"].config(text=f"{ram:.1f}%")

                    # GPU
                    try:
                        gpus = GPUtil.getGPUs()
                        if gpus:
                            gpu = gpus[0]
                            self.labels["GPU"].config(text=f"{gpu.load*100:.1f}% • {gpu.memoryUtil*100:.1f}% VRAM")
                            self.labels["Temperatura"].config(text=f"{gpu.temperature}°C GPU")
                        else:
                            self.labels["GPU"].config(text="N/A")
                    except:
                        self.labels["GPU"].config(text="N/A")

                    # Bateria
                    bat = psutil.sensors_battery()
                    if bat:
                        tempo = "Carregando" if bat.secsleft == -1 else f"{bat.secsleft//60} min"
                        self.labels["Bateria"].config(text=f"{bat.percent:.0f}% • {tempo}")
                    else:
                        self.labels["Bateria"].config(text="Desktop")

                    # Status geral
                    self.labels["Status"].config(text="OPERATIONAL • STABLE")

                except:
                    pass
                
                time.sleep(1.2)

        threading.Thread(target=refresh, daemon=True).start()

# ==================== RODAR ====================
if __name__ == "__main__":
    app = PC_Monitor_Luxo()
    app.root.mainloop()