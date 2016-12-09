#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Todo

- Change color

"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
import networkx as nx
import math
from collections import namedtuple


Coord = namedtuple("Coord", ['x','y'])

VERTEXWIDTH = 5



def coordDistanceSq(c, e):
    return (c.x - e.x)**2 + (c.y - e.y)**2


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Graph Shower')

        but = QPushButton('Save', self)
        but.move(10,10)

        canv = Canvas(self)
        canv.move(10, 50)

        self.show()



class Canvas(QWidget):

    def __init__(self, parent):
        super(Canvas, self).__init__(parent)
        self.graph  = self.initGraph()
        self.leftdown = None

    def initGraph(self):
        G = nx.Graph()
        v1 = Coord(x=5, y=7)
        v2 = Coord(14, 124)
        G.add_node(v1)
        G.add_node(v2)
        G.add_edge(v1,v2, color='red')
        # print(G.nodes())
        # print(G.edges())
        return G

    def closestNode(self, coord):
        distance = 10000000
        candidate = None
        for n in self.graph.nodes():
            if coordDistanceSq(n, coord) < distance:
                candidate = n
                distance = coordDistanceSq(n,coord)
        if distance < 100:
            return candidate




    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftdown = Coord(event.x(), event.y())

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton and not self.leftdown is None :
            leftup = Coord(event.x(), event.y())

            if coordDistanceSq(self.leftdown, leftup) <10:
                print("Distance is: {}. Adding node".format(coordDistanceSq(self.leftdown, leftup)))
                if not closestNode(self.leftdown) is None:
                    print("To close to an other node. Abort")
                    self.leftdown=None
                    return

                self.graph.add_node(self.leftdown)
                self.leftdown = None
                self.update()

            else:
                v1 = self.closestNode(self.leftdown)
                v2 = self.closestNode(leftup)

                if not v1 is None and not v2 is None:
                    print("Adding edge")
                    self.graph.add_edge(v1, v2, color = 'black')
                    self.leftdown = None
                    self.update()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)

        redpen = QPen(Qt.red,2)
        bluepen = QPen(Qt.blue,2)
        blackpen = QPen(Qt.black, 2)
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
    ex = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
