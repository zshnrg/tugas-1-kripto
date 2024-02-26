import time
from lib.moduleChecker import checkModule, clearConsole, readFileJson
import webbrowser
from app import app

if __name__ == '__main__':

    clearConsole()
    config = readFileJson('./config/index.json')
    print("[ ⭐ ] Checking for required modules...")
    for module in config['modules']:
        checkModule(module)
    print("[ ✔ ] All required modules are installed.")
    print("[ ⭐ ] Starting the application...")

    # webbrowser.open(f"http://{config['host']}:{config['port']}")
    app.run(host=config['host'], port=config['port'], debug=config['debug'])