"""Demo script for LcdLabel widget.

Run with: poetry run python -m LcdLabel
"""

import sys

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont

from . import LcdLabel


def create_demo_widget() -> QWidget:
    """Create a demo widget showcasing LcdLabel features."""
    container = QWidget()
    container.setWindowTitle("LcdLabel Demo")
    container.resize(500, 300)

    layout = QVBoxLayout(container)
    layout.setSpacing(20)

    font14 = QFont("DSEG14 Classic Mini", pointSize=18)

    label1 = LcdLabel()
    label1.text = "3.14159"
    label1.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(label1)
    label1.setFont(QFont("DSEG7 Classic Mini", pointSize=24))

    label10 = LcdLabel()
    label10.text = "3.14159"
    label10.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(label10)
    label10.setFont(QFont("DSEG14 Classic Mini", pointSize=24))

    label2 = LcdLabel()
    label2.text = "3.14159"
    label2.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
    layout.addWidget(label2)
    label2.foregroundColor = QColor(0, 255, 0)

    label11 = LcdLabel()
    label11.text = "3.14159"
    label11.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
    layout.addWidget(label11)
    label11.foregroundColor = QColor(0, 255, 0)
    label11.setFont(font14)

    label3 = LcdLabel()
    label3.text = "3.14159"
    label3.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(label3)
    label3.backgroundColor = QColor(0, 0, 255)

    label12 = LcdLabel()
    label12.text = "3.14159"
    label12.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(label12)
    label12.setFont(font14)
    label12.backgroundColor = QColor(0, 0, 255)

    label4 = LcdLabel()
    label4.text = "TEST"
    label4.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(label4)

    label13 = LcdLabel()
    label13.text = "TEST"
    label13.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(label13)
    label13.setFont(font14)

    label5 = LcdLabel()
    label5.text = "RIGHT"
    label5.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
    layout.addWidget(label5)

    label7 = LcdLabel()
    label7.text = "RIGHT"
    label7.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
    label7.setFont(font14)
    layout.addWidget(label7)

    label6 = LcdLabel()
    label6.text = "LEFT"
    label6.setEnabled(False)
    label6.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(label6)

    label8 = LcdLabel()
    label8.text = "LEFT"
    label8.setEnabled(False)
    label8.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
    label8.setFont(font14)
    layout.addWidget(label8)

    # Add some spacing at the bottom
    layout.addStretch()

    return container


def main() -> int:
    """Run the demo application."""
    app = QApplication(sys.argv)

    demo = create_demo_widget()
    demo.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
