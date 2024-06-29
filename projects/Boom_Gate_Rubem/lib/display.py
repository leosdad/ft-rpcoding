import os
import time
import threading
import ftgui  # type: ignore

display = ftgui.fttxt2_gui_connector("app")
display.run()


def display_monitoring():
    while display.running():
        time.sleep(1)
    os._exit(0)
    exit()


threading.Thread(target=display_monitoring, daemon=True).start()
