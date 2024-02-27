import importlib.util, sys, os, subprocess, json

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def readFileJson(file):
    f = open(file, 'r')
    data = json.loads(f.read())
    f.close()

    return data

def checkModule(moduleName):
    if importlib.util.find_spec(moduleName) is None:
        print(f"[ X ] {moduleName} is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", moduleName])
    else:
        print(f"[ v ] {moduleName} is installed.")

