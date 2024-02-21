import importlib.util, sys, os, subprocess, json

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def readFileJson(file):
    f = open(file, 'r')
    data = json.loads(f.read())
    f.close()

    return data

def checkModule(moduleName):
    if moduleName in sys.modules:
        print(f"Module {moduleName} is already installed ✔️")
    elif (spec := importlib.util.find_spec(moduleName)) is not None:
        print(f"Module {moduleName} is needed, installing...")
        module = importlib.util.module_from_spec(spec)
        sys.modules[moduleName] = module
        spec.loader.exec_module(module)
        print(f"Module {moduleName} installed ✔️")
    else:
        print(f"Module {moduleName} is not installed ❌")
        print(f"Installing {moduleName}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
