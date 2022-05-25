from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

message_code = {
        1062: "Користувач з таким логіном уже існує",
        2003: "Підключення не встановлено, оскільки кінцевий комп'ютер відкинув запит на підключення"
    }


def warning(message: str = None, exception: Exception = None, title: str = ' ', info=False) -> None:
    msg = QMessageBox()
    msg.setWindowTitle(title)
    if exception is not None:
        try:
            code = exception.args[0]
        except:
            code = None

        if code in message_code:
            msg.setText(message_code[code])
        else:
            msg.setText(str(exception))
    else:
        msg.setText(message)

    if not info:
        msg.setWindowIcon(QIcon("icon/warning.png"))
        msg.setIcon(QMessageBox.Icon.Warning)
    else:
        msg.setWindowIcon(QIcon("icon/information.png"))
        msg.setIcon(QMessageBox.Icon.Information)

    msg.setStandardButtons(QMessageBox.Ok)
    _ = msg.exec_()
