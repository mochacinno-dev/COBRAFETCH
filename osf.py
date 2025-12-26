#########################
# Cobrafetch 0.9.1
# OS Information Fetching Module
# Written by: Camila "Mocha" Rose
#########################

# IMPORTS
import platform # For kernel information
import distro # For Linux distribution information
import os # For Windows version information

def osfetch():
    
    # KERNEL
    kernel = platform.system()
    kversion = platform.release()
    kid = platform.machine()

    # DISTRO
    distron = distro.name()
    did = distro.id()
    dversion = distro.version()

    # WINDOWS


    print(f"<=== KERNEL: {kernel} {kversion} {kid}")
    print(f"<=== OS: {distron} {dversion} ({did})")
