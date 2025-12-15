import platform
import distro

def osfetch():
    
    # KERNEL
    kernel = platform.system()
    kversion = platform.release()
    kid = platform.machine()

    # DISTRO
    distron = distro.name()
    did = distro.id()
    dversion = distro.version()

    print(f"<=== KERNEL: {kernel} {kversion} {kid}")
    print(f"<=== OS: {distron} {dversion} ({did})")
