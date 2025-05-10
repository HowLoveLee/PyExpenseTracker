"""
    This was one of the main draws I thought of back then.
    Will explain further down the line but its basically phone reminders
    AI would be cool here.
"""

from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QComboBox, QSpinBox, QSpacerItem, QSizePolicy, QProgressBar, QScrollArea)


def createBudgetInputLine():
    containerLayout = QHBoxLayout()

    budgetLayout = QHBoxLayout()
    budgetLayout.addWidget(QLabel("For the next"))
    timeFrameDropDown = QComboBox()
    timeFrameDropDown.addItems(["Week", "Month", "6 Months", "Year"])
    budgetLayout.addWidget(timeFrameDropDown)

    budgetLayout.addWidget(QLabel("I want to set a budget of"))
    amountInput = QLineEdit()
    amountInput.setMaximumWidth(100)
    budgetLayout.addWidget(amountInput)

    budgetLayout.addWidget(QLabel("for the category"))
    categoryDropDown = QComboBox()
    budgetLayout.addWidget(categoryDropDown)

    budgetLayout.addWidget(QLabel("I want to stay within"))
    percentageInput = QSpinBox()
    percentageInput.setRange(0, 100)
    percentageInput.setSuffix('%')
    budgetLayout.addWidget(percentageInput)

    spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
    budgetLayout.addItem(spacer)

    containerLayout.addLayout(budgetLayout)

    progressbar = QProgressBar()
    progressbar.setValue(50)
    progressbar.setContentsMargins(0, 0, 0, 0)
    progressbar.setMaximumWidth(500)
    randomcolor = f"rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})"
    progressbar.setStyleSheet(f"QProgressBar::chunk {{ background-color: {randomcolor}; }}")

    containerLayout.addWidget(progressbar)

    return containerLayout


class ConditionalStatements(QWidget):
    def __init__(self, categories=None):
        super().__init__()

        self.scrollArea = QScrollArea(self)

        self.scrollArea.setWidgetResizable(True)

        self.scrollWidget = QWidget()

        self.scrollArea.setWidget(self.scrollWidget)

        mainLayout = QVBoxLayout(self.scrollWidget)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.budgetSetUpLayout = QVBoxLayout()

        budgetLayout = createBudgetInputLine()
        self.budgetSetUpLayout.addLayout(budgetLayout)

        buttonLayout = QHBoxLayout()
        self.submitButton = QPushButton("Set Budget")
        buttonLayout.addWidget(self.submitButton)

        mainLayout.addLayout(self.budgetSetUpLayout)
        mainLayout.addLayout(buttonLayout)

        # Use a layout for the main BudgetPanel to add the scroll area
        scrollLayout = QVBoxLayout(self)
        scrollLayout.addWidget(self.scrollArea)
        self.setLayout(scrollLayout)

    def addBudgetLine(self):
        newBudgetLine = createBudgetInputLine()
        self.budgetSetUpLayout.insertLayout(0, newBudgetLine)
        self.update()

    def adjustForScreenSize(self):
        screen = QGuiApplication.screens()[0]
        screensize = screen.size()

        if screensize.width() > 1920:
            self.squishButtonsToCenter()
        else:
            self.setDefaultButtonSpacing()

    def squishButtonsToCenter(self):

        for index in range(self.budgetSetUpLayout.count()):
            layout = self.budgetSetUpLayout.itemAt(index).layout()

            if not isinstance(layout.itemAt(0), QSpacerItem):
                leftspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
                layout.insertItem(0, leftspacer)
            if not isinstance(layout.itemAt(layout.count() - 1), QSpacerItem):
                rightspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
                layout.addItem(rightspacer)

    def setDefaultButtonSpacing(self):

        for index in range(self.budgetSetUpLayout.count()):
            layout = self.budgetSetUpLayout.itemAt(index).layout()

            if isinstance(layout.itemAt(0), QSpacerItem):
                layout.takeAt(0).widget().deleteLater() if layout.itemAt(0).widget() else layout.takeAt(0)

            if isinstance(layout.itemAt(layout.count() - 1), QSpacerItem):
                layout.takeAt(layout.count() - 1).widget().deleteLater() if layout.itemAt(
                    layout.count() - 1).widget() else layout.takeAt(layout.count() - 1)
