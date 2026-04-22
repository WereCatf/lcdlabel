from __future__ import annotations

from src.lcdlabel.plugin import LcdLabelPlugin

from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection


if __name__ == "__main__":
    QPyDesignerCustomWidgetCollection.addCustomWidget(LcdLabelPlugin())
