#########################
# Cobrafetch 0.9.1
# Ruby subprocess Module
# Written by: Camila "Mocha" Rose
#########################

import os
import subprocess

def shellf():
    try:
        ruby = os.path.join(os.path.dirname(__file__), 'shf.rb')
        subprocess.run(['ruby', ruby], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Ruby script: {e}")
    except FileNotFoundError:
        print("Ruby not found. Please install Ruby to use this feature.")