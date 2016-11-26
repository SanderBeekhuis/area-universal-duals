#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this example we draw 6 lines using
different pen styles.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
import networkx as nx
import math
from collections import namedtuple


Coord = namedtuple("Coord", ['x','y'])

VERTEXWIDTH = 5



def eventDistance


class Canvas(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.graph  = self.initGraph()
        self.leftdown = None
        self.initUI()

    def initGraph(self):
        G = nx.Graph()
        v1 = Coord(x=5, y=7)
        v2 = Coord(14, 124)
        G.add_node(v1)
        G.add_node(v2)
        G.add_edge(v1,v2, color='red')
        print(G.nodes())
        print(G.edges())

        return G

    def initUI(self):

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftdown = event

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and not leftdown is None :
            if distance(self.leftdown, event) <10:
                G.add_node


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)

        redpen = QPen(Qt.red,2)
        bluepen = QPen(Qt.blue,2)
        blackpen = QPen(2)
        pens={'black':blackpen, 'red':redpen, 'blue':bluepen}



        for e in self.graph.edges_iter(data='color'):
            #dges are returned as tuples with optional data in the order (node, neighbor, data).
            qp.setPen(pens[e[2]])
            qp.drawLine(e[0].x, e[0].y, e[1].x, e[1].y)

        qp.setPen(pens['black'])
        for v in self.graph.nodes():
            qp.drawEllipse(v.x - .5*VERTEXWIDTH, v.y - .5*VERTEXWIDTH, VERTEXWIDTH, VERTEXWIDTH)

        qp.end()



def main():

    app = QApplication(sys.argv)
    ex = Canvas()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
