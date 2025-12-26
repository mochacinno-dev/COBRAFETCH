#########################
# Cobrafetch 0.9.1
# Resource Information Fetching Module
# Written by: Camila "Mocha" Rose
#########################

import cpuinfo
import subprocess
import os
import psutil
import platform

def cpu():
    cpu = cpuinfo.get_cpu_info()
    return cpu.get('brand_raw', 'Unknown CPU')

def gpu():
    system = platform.system()
    
    if system == "Windows":
        try:
            # Use WMIC to get GPU info on Windows
            result = subprocess.check_output(
                ['wmic', 'path', 'win32_VideoController', 'get', 'name'],
                stderr=subprocess.DEVNULL
            ).decode()
            gpus = [line.strip() for line in result.split('\n') if line.strip() and line.strip() != 'Name']
            return gpus[0] if gpus else 'Unknown GPU'
        except:
            pass
    else:
        try:
            result = subprocess.check_output(['lspci'], stderr=subprocess.DEVNULL).decode()
            for line in result.split('\n'):
                if 'VGA' in line or '3D' in line:
                    return line.split(': ')[1] if ': ' in line else 'Unknown GPU'
        except:
            pass
    
    return 'Unknown GPU'

def ram():
    mem = psutil.virtual_memory()
    total_gb = mem.total / (1024 ** 3)
    return f"{total_gb:.1f} GB"

def model():
    system = platform.system()
    
    if system == "Windows":
        try:
            # Use WMIC to get computer model on Windows
            result = subprocess.check_output(
                ['wmic', 'computersystem', 'get', 'model'],
                stderr=subprocess.DEVNULL
            ).decode()
            models = [line.strip() for line in result.split('\n') if line.strip() and line.strip() != 'Model']
            return models[0] if models else 'Unknown Model'
        except:
            return 'Unknown Model'
    else:
        try:
            with open('/sys/devices/virtual/dmi/id/product_name', 'r') as f:
                return f.read().strip()
        except:
            return 'Unknown Model'

def wm_de():
    system = platform.system()
    
    if system == "Windows":
        # Detect Windows desktop environment
        win_ver = platform.release()
        if int(win_ver) >= 10:
            return 'Windows Desktop (DWM)'
        else:
            return f'Windows {win_ver} Desktop'
    else:
        # Linux/Unix desktop detection
        desktop = os.environ.get('XDG_CURRENT_DESKTOP', '')
        session = os.environ.get('DESKTOP_SESSION', '')
        wm = os.environ.get('WAYLAND_DISPLAY', '')
        
        if desktop:
            return desktop
        elif session:
            return session
        elif wm:
            return 'Wayland'
        else:
            return 'Unknown'

def resfetch():
    print(f"<=== CPU: {cpu()}")
    print(f"<=== GPU: {gpu()}")
    print(f"<=== RAM: {ram()}")
    print(f"<=== MODEL: {model()}")
    print(f"<=== DE/WM: {wm_de()}")