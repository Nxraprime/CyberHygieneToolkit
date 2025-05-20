
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Functions
def enable_firewall():
    subprocess.call("netsh advfirewall set allprofiles state on", shell=True)
    messagebox.showinfo("Success", "Firewall Enabled")

def defender_scan():
    subprocess.call("start windowsdefender://", shell=True)

def clear_junk():
    subprocess.call("powershell.exe -ExecutionPolicy Bypass -File modules/clear_temp.ps1", shell=True)
    messagebox.showinfo("Done", "Junk files cleared")

def check_disk():
    subprocess.call("powershell.exe -ExecutionPolicy Bypass -File modules/check_disk.ps1", shell=True)

def show_sys_info():
    subprocess.call("powershell.exe -ExecutionPolicy Bypass -File modules/system_info.ps1", shell=True)

# Main Window
root = tk.Tk()
root.title("Cyber Hygiene Toolkit - LUNIX WEB")
root.geometry("400x350")
root.configure(bg='#f5f5f5')

tk.Label(root, text="LUNIX WEB", font=("Helvetica", 18, "bold"), bg='#f5f5f5').pack(pady=(10, 0))
tk.Label(root, text="Your Vision, Our Code", font=("Helvetica", 12), bg='#f5f5f5').pack(pady=(0, 20))

tk.Button(root, text="Enable Firewall", command=enable_firewall, width=30, height=2).pack(pady=5)
tk.Button(root, text="Run Defender Scan", command=defender_scan, width=30, height=2).pack(pady=5)
tk.Button(root, text="Clear Junk Files", command=clear_junk, width=30, height=2).pack(pady=5)
tk.Button(root, text="Check Disk Usage", command=check_disk, width=30, height=2).pack(pady=5)
tk.Button(root, text="Show System Info", command=show_sys_info, width=30, height=2).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, width=30, height=2, bg="red", fg="white").pack(pady=(20, 10))

root.mainloop()
