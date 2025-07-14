import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import matplotlib.pyplot as plt
from ping3 import ping


def run_ping():
    host = entry_host.get()
    try:
        count = int(entry_count.get())
        if count <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number (1 or more).")
        return

    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)

    rtts = []
    output_box.insert(tk.END, f"Pinging {host} {count} times...\n\n")

    for i in range(1, count + 1):
        delay = ping(host, timeout=2)
        if delay:
            rtt = round(delay * 1000, 2)
            msg = f"{i}. Reply from {host}: time={rtt}ms\n"
            rtts.append(rtt)
        else:
            msg = f"{i}. Request timed out.\n"
            rtts.append(0)
        output_box.insert(tk.END, msg)
        output_box.see(tk.END)

    output_box.insert(tk.END, "\nPing complete.\n")
    output_box.config(state='disabled')

    # Plot RTT graph
    plt.figure(figsize=(6, 4))
    plt.plot(range(1, count + 1), rtts, marker='o', color='#007acc', linewidth=2)
    plt.title(f"Ping Results to {host}")
    plt.xlabel("Ping Attempt")
    plt.ylabel("Latency (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# GUI Setup
root = tk.Tk()
root.title("🛰 Ping Visualizer")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#f0f2f5")

style = ttk.Style()
style.theme_use("clam")

# Frame: Input Section
frame_input = ttk.Frame(root, padding=10)
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Host/IP:", font=('Segoe UI', 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_host = ttk.Entry(frame_input, width=30, font=('Segoe UI', 10))
entry_host.grid(row=0, column=1, padx=5)
entry_host.insert(0, "google.com")

ttk.Label(frame_input, text="Ping Count:", font=('Segoe UI', 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_count = ttk.Entry(frame_input, width=10, font=('Segoe UI', 10))
entry_count.grid(row=1, column=1, sticky="w", padx=5)
entry_count.insert(0, "5")

btn_ping = ttk.Button(root, text="▶ Start Ping", command=run_ping)
btn_ping.pack(pady=10)

# Frame: Output Box
frame_output = ttk.LabelFrame(root, text="Results", padding=10)
frame_output.pack(fill="both", expand=True, padx=15, pady=5)

output_box = scrolledtext.ScrolledText(frame_output, height=15, font=("Consolas", 10), wrap=tk.WORD, state='disabled')
output_box.pack(fill="both", expand=True)

# Run the app
root.mainloop()