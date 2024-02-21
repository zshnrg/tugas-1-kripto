import time
from lib.moduleChecker import checkModule, clearConsole, readFileJson

if __name__ == '__main__':
    clearConsole()
    config = readFileJson('./config/index.json')
    print("[ ⭐ ] Checking for required modules...")
    time.sleep(1)
    for module in config['modules']:
        time.sleep(1)
        checkModule(module)