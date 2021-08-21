import sys
import gui

import db


def main():
    connection = db.create_connection_postgre(
        server="localhost",
        database="ubs",
        username="trabalho_db_ubs",
        password="trabalho_db_ubs",
        port=5432
    )

    app = gui.QApplication(sys.argv)

    main_window = gui.MainWindow()

    main_window.load_window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
