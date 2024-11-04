import glob
from pathlib import Path
from bot.utils import load_plugins
import logging
from . import bot


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        if plugin_name == "mailgetter" or plugin_name == "bid":
            pass
        else:    
            load_plugins(plugin_name.replace(".py", ""))


print("Successfully deployed ")
print("Dont Forget Giving A star on github....")
print("or you can owe me a coffee...")





    



if __name__ == "__main__":
    bot.run_until_disconnected()
    
    
    
    


