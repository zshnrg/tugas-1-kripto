import time
from lib.moduleChecker import checkModule, clearConsole, readFileJson
import webbrowser

if __name__ == '__main__':

    clearConsole()
    config = readFileJson('./config/index.json')
    print("[ * ] Checking for required modules...")
    for module in config['modules']:
        checkModule(module)
    print("[ v ] All required modules are installed.")
    print("[ * ] Starting the application...")

    from app import app
    webbrowser.open(f"http://{config['host']}:{config['port']}")
    app.run(host=config['host'], port=config['port'])