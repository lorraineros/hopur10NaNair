#!/usr/bin/env python3
from .ui.ui import App

if __name__ == "__main__":
    app = App()
    try:
        app.run()
    except KeyboardInterrupt:
        pass
    print("Thank you for using NaNAir")
