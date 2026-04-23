"""Demo script for LcdLabel widget.

Run with: poetry run python -m LcdLabel
"""

import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

from lcdlabel.ui_example import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Animation timer
        self._anim_timer = QTimer(self)
        self._anim_timer.timeout.connect(self.update_clock)
        self._anim_timer.start(1000)  # Update every second
        self._show_colon = True

    def update_clock(self):
        """Update the clock display with the current time."""
        from datetime import datetime

        now = datetime.now()
        time_str = now.strftime("%H:%M.%S").replace(
            ".", "" if not self._show_colon else "."
        )
        self.ui.clock1.setText(time_str.replace(":", " " if self._show_colon else ":"))
        self.ui.clock2.setText(time_str.replace(":", " " if self._show_colon else ":"))
        self._show_colon = not self._show_colon


def main() -> int:
    """Run the demo application."""
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
