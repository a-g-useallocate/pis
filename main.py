import logging
import tkinter as tk
from tkinter import messagebox

from db import init_db
from logger_setup import setup_logging
from ui import LoginWindow


if __name__ == "__main__":
    setup_logging()
    try:
        init_db()
        app = LoginWindow()
        app.mainloop()
    except Exception as exc:  # production fallback: error is shown and written to log
        logging.exception("Critical application error")
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "StylModa v3",
            "Приложение не смогло запуститься. Подробности сохранены в logs/stylmoda_production.log.\n\n" + str(exc),
        )
        root.destroy()
