#!/usr/bin/env python3
from .ui.ui import App

if __name__ == "__main__":
    app = App()
    try:
        app.run()
    except KeyboardInterrupt:
        pass
    print(
    """
        _   _       _   _      _    _
       | \ | | __ _| \ | |    / \  (_)_ __
       |  \| |/ _` |  \| |   / _ \ | | '__|
       | |\  | (_| | |\  |  / ___ \| | |
       |_| \_|\__,_|_| \_| /_/   \_\_|_|

----------- Thank you for using NaNAir ----------- """) 

