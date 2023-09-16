import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import pandas as pd
from pandasgui import show


data = pd.DataFrame([
          [1, 9, 2],
          [1, 0, -1],
          [3, 5, 2],
          [3, 3, 2],
          [5, 8, 9],
        ], columns = ['Protein Accession', 'Seq. Cov. / %', '#Peptides'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])


def show_dataframe(data):
    show(data)


