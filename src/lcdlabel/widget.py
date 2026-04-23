from __future__ import annotations
from typing import TYPE_CHECKING

from PySide6 import QtGui
from PySide6.QtCore import Property, Signal, QEvent
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QStackedLayout,
    QWidget,
)
from PySide6.QtCore import Qt

try:
    import lcdlabel.rc_fonts  # noqa: F401
except ImportError:
    import src.lcdlabel.rc_fonts  # noqa: F401


class LcdLabel(QWidget):
    stateChanged = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14Classic-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Modern-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Classic-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ModernMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Modern-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7SEGGCHANMINI-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7SEGGCHAN-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEGWeather.ttf")

        self._foregroundLabel = QLabel(self)
        self._foregroundLabel.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction
        )
        self._backgroundLabel = QLabel(self)
        self._backgroundLabel.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction
        )
        self._foregroundLabel.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self._backgroundLabel.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self._foregroundLabel.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight
        )
        self._backgroundLabel.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight
        )

        self._layout = QStackedLayout(self)
        self._layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self._layout.addWidget(self._foregroundLabel)
        self._layout.addWidget(self._backgroundLabel)
        self._foregroundColor = QColor(255, 255, 255)
        self._backgroundColor = QColor(60, 60, 60)
        palette = self._backgroundLabel.palette()
        palette.setColor(QPalette.ColorRole.WindowText, self._backgroundColor)
        self._backgroundLabel.setPalette(palette)
        palette = self._foregroundLabel.palette()
        palette.setColor(QPalette.ColorRole.WindowText, self._foregroundColor)
        self._foregroundLabel.setPalette(palette)
        font = QFont("DSEG7 Classic Mini", pointSize=18)
        self.setFont(font)
        self.backgroundText = "8.88888"
        self.text = "3.14159"

    def changeEvent(self, event):
        super().changeEvent(event)
        if event.type() == QEvent.Type.FontChange:
            self._foregroundLabel.setFont(self.font())
            self._backgroundLabel.setFont(self.font())

    if TYPE_CHECKING:
        alignment: Qt.AlignmentFlag
    else:

        @Property(Qt.AlignmentFlag)
        def alignment(self) -> Qt.AlignmentFlag:
            return self._foregroundLabel.alignment()

        @alignment.setter
        def alignment(self, value: Qt.AlignmentFlag) -> None:
            self._foregroundLabel.setAlignment(value)
            self._backgroundLabel.setAlignment(value)

    def setAlignment(self, alignment: Qt.AlignmentFlag) -> None:
        self.alignment = alignment

    if TYPE_CHECKING:
        text: str
    else:

        @Property(str)
        def text(self) -> str:
            return self._foregroundLabel.text()

        @text.setter
        def text(self, value: str) -> None:
            self._foregroundLabel.setText(value)

    def setText(self, text: str) -> None:
        self.text = text

    if TYPE_CHECKING:
        backgroundText: str
    else:

        @Property(str)
        def backgroundText(self) -> str:
            return self._backgroundLabel.text()

        @backgroundText.setter
        def backgroundText(self, value: str) -> None:
            self._backgroundLabel.setText(value)
            self.update()

    def setBackgroundText(self, text: str) -> None:
        self.backgroundText = text

    if TYPE_CHECKING:
        foregroundColor: QColor | str
    else:

        @Property(QColor)
        def foregroundColor(self) -> QColor:
            return self._foregroundColor

        @foregroundColor.setter
        def foregroundColor(self, value: QColor | str) -> None:
            color = QColor().fromString(value) if isinstance(value, str) else value
            if self._foregroundColor != color:
                self._foregroundColor = color
                palette = self._foregroundLabel.palette()
                palette.setColor(QPalette.ColorRole.WindowText, self._foregroundColor)
                self._foregroundLabel.setPalette(palette)

    def setforegroundColor(self, color: QColor | str) -> None:
        self.foregroundColor = color

    if TYPE_CHECKING:
        backgroundColor: QColor | str
    else:

        @Property(QColor)
        def backgroundColor(self) -> QColor:
            return self._backgroundColor

        @backgroundColor.setter
        def backgroundColor(self, value: QColor | str) -> None:
            color = QColor().fromString(value) if isinstance(value, str) else value
            if self._backgroundColor != color:
                self._backgroundColor = color
                palette = self._backgroundLabel.palette()
                palette.setColor(QPalette.ColorRole.WindowText, self._backgroundColor)
                self._backgroundLabel.setPalette(palette)

    def setbackgroundColor(self, color: QColor | str) -> None:
        self.backgroundColor = color
