from __future__ import annotations

from PySide6.QtDesigner import QDesignerCustomWidgetInterface
from PySide6.QtGui import QIcon, QPainter, QColor, QPixmap
from PySide6.QtCore import Qt

try:
    from .widget import LcdLabel
except ImportError:
    from widget import LcdLabel  # type: ignore


class LcdLabelPlugin(QDesignerCustomWidgetInterface):
    """Plugin interface for LcdLabel in PySide6 Designer.

        This class provides the metadata and factory methods required by
        PySide6 Designer to integrate the LcdLabel widget into its
    toolbox and property editor.
    """

    def __init__(self, parent=None):
        super().__init__()
        self._initialized = False

    def initialize(self, formEditor):
        if self._initialized:
            return
        self._initialized = True

    def isInitialized(self):
        return self._initialized

    def createWidget(self, parent):
        return LcdLabel(parent)

    def name(self):
        return "LcdLabel"

    def group(self):
        return ""

    def icon(self):
        pixmap = QPixmap(22, 22)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setBrush(QColor(255, 0, 0))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(2, 7, 8, 8)

        painter.setPen(QColor(100, 100, 100))
        painter.drawLine(13, 9, 20, 9)
        painter.drawLine(13, 13, 20, 13)

        painter.end()

        return QIcon(pixmap)

    def toolTip(self):
        return "A label that looks like an LCD-display."

    def whatsThis(self):
        return (
            "LcdLabel is a display-only widget showing a text label "
            "with a configurable LCD-style display."
        )

    def isContainer(self):
        return False

    def includeFile(self):
        return "lcdlabel"

    def domXml(self):
        return """
        <ui language="c++">
            <widget class="LcdLabel" name="lcdLabel">
                <property name="geometry">
                    <rect>
                        <x>0</x>
                        <y>0</y>
                        <width>150</width>
                        <height>60</height>
                    </rect>
                </property>
                <property name="text">
                    <string>Pi 1.31</string>
                </property>
                <property name="backgroundPattern">
                    <string>8.</string>
                </property>
                <property name="foregroundColor">
                    <color>
                    <red>255</red>
                    <green>255</green>
                    <blue>255</blue>
                    </color>
                </property>
                <property name="backgroundColor">
                    <color>
                    <red>60</red>
                    <green>60</green>
                    <blue>60</blue>
                    </color>
                </property>
                <property name="length">
                    <number>9</number>
                </property>
                <property name="alignment">
                    <set>Qt::AlignVCenter</set>
                    <set>Qt::AlignRight</set>
                </property>
            </widget>
        </ui>
        """
