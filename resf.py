import cpuinfo
import subprocess
import os
import psutil

def cpu():
    cpu = cpuinfo.get_cpu_info()
    return cpu.get('brand_raw', 'Unknown CPU')

def gpu():
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
    try:
        with open('/sys/devices/virtual/dmi/id/product_name', 'r') as f:
            return f.read().strip()
    except:
        return 'Unknown Model'

def wm_de():
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