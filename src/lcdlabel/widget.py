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
    import lcdlabel.fonts  # noqa: F401
except ImportError:
    import src.lcdlabel.fonts  # noqa: F401


class LcdLabel(QWidget):
    stateChanged = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._length = 9
        self._backgroundPattern = "8."

        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Classic-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14Classic-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Classic-Italic.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Classic-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14Classic-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-Bold.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-Italic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-Light.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ClassicMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14Classic-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Modern-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14Modern-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Modern-Italic.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Modern-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14Modern-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-Bold.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-Italic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-Light.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG14ModernMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG14Modern-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Classic-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7Classic-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Classic-Italic.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Classic-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7Classic-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-Bold.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-Italic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-Light.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ClassicMini-Regular.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Classic-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Modern-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7Modern-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Modern-Italic.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7Modern-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7Modern-LightItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(":/fonts/fonts/DSEG7ModernMini-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ModernMini-BoldItalic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ModernMini-Italic.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ModernMini-Light.ttf"
        )
        QtGui.QFontDatabase.addApplicationFont(
            ":/fonts/fonts/DSEG7ModernMini-LightItalic.ttf"
        )
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
        self._backgroundLabel.setText(self._backgroundPattern * self._length)
        self._foregroundLabel.setText("1.4159")
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
            if self._foregroundLabel.alignment() != value:
                self._foregroundLabel.setAlignment(value)
                self._backgroundLabel.setAlignment(value)

    def setAlignment(self, alignment: Qt.AlignmentFlag) -> None:
        self.alignment = alignment

    if TYPE_CHECKING:
        length: int
    else:

        @Property(int)
        def length(self) -> int:
            return self._length

        @length.setter
        def length(self, value: int) -> None:
            if self._length != value and value > 0:
                self._length = value
                self._backgroundLabel.setText("8." * self._length)
                self._foregroundLabel.setText(
                    self._foregroundLabel.text()[: self._length]
                )

    def setLength(self, length: int) -> None:
        self.length = length

    if TYPE_CHECKING:
        text: str
    else:

        @Property(str)
        def text(self) -> str:
            return self._foregroundLabel.text()

        @text.setter
        def text(self, value: str) -> None:
            newText = value[
                : self._length
            ].replace(
                " ", "⠀"
            )  # Replace spaces with non-breaking spaces, the font doesn't render regular spaces correctly
            if self._foregroundLabel.text() != newText:
                self._foregroundLabel.setText(newText)

    def setText(self, text: str) -> None:
        self.text = text

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

    if TYPE_CHECKING:
        backgroundPattern: str
    else:

        @Property(str)
        def backgroundPattern(self) -> str:
            return self._backgroundPattern

        @backgroundPattern.setter
        def backgroundPattern(self, value: str) -> None:
            if self._backgroundPattern != value:
                self._backgroundPattern = value
                self._backgroundLabel.setText(self._backgroundPattern * self._length)

    def setBackgroundPattern(self, pattern: str) -> None:
        self.backgroundPattern = pattern
