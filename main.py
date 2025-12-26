#########################
# Cobrafetch 0.9.1
# Main Functionality Module
# Written by: Camila "Mocha" Rose
#########################

from osf import osfetch
from resf import resfetch
from rbutil import shellf

def main():
    print("<=== COBRAFETCH ===>")
    osfetch()
    resfetch()
    shellf()

if __name__ == "__main__":
    main()