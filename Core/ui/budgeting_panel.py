# Placeholder, nothing here makes sense.

from PyQt6.QtWidgets import QPushButton, QSizePolicy
from PyQt6 import QtWidgets

class BudgetPanel(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()



        mainLayout = QtWidgets.QVBoxLayout()

        buttonLayout = QtWidgets.QHBoxLayout()

        conditionalStatementsBtn = QPushButton("Conditional Statements")
        conditionalStatementsBtn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        budgetingGoalsBtn = QPushButton("Budgeting Goals")
        budgetingGoalsBtn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        debtManagementBtn = QPushButton("Debt Management")
        debtManagementBtn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        buttonLayout.addWidget(conditionalStatementsBtn)
        buttonLayout.addWidget(budgetingGoalsBtn)
        buttonLayout.addWidget(debtManagementBtn)

        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
