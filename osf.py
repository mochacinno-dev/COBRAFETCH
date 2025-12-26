#########################
# Cobrafetch 0.9.1
# OS Information Fetching Module
# Written by: Camila "Mocha" Rose
#########################

# IMPORTS
import platform # For kernel information
import distro # For Linux distribution information
import os # For Windows version information
import sys # For system-specific parameters and functions

def osfetch():
    
    # KERNEL
    kernel = platform.system()
    kversion = platform.release()
    kid = platform.machine()

    # Check if running on Windows
    if kernel == "Windows":
        # Get Windows version info
        win_ver = platform.version()
        win_edition = platform.win32_edition() if hasattr(platform, 'win32_edition') else 'Windows'
        
        print(f"<=== KERNEL: {kernel} {kversion} {kid}")
        print(f"<=== OS: {win_edition} {kversion}")
    else:
        # DISTRO (Linux)
        distron = distro.name()
        did = distro.id()
        dversion = distro.version()

        print(f"<=== KERNEL: {kernel} {kversion} {kid}")
        print(f"<=== OS: {distron} {dversion} ({did})")