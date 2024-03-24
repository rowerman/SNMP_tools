from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGroupBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Matplotlib Figure in QGroupBox')

        # 创建一个QGroupBox
        self.groupBox = QGroupBox('Matplotlib Figure')
        self.setCentralWidget(self.groupBox)

        # 创建一个matplotlib图像
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 创建一个matplotlib导航工具栏，并添加到QGroupBox中
        self.toolbar = NavigationToolbar(self.canvas, self.groupBox)

        # 使用QVBoxLayout布局，并将matplotlib图像和工具栏添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.groupBox.setLayout(layout)

        # 在matplotlib图像上绘制一些数据
        self.plot_data()

    def plot_data(self):
        ax = self.figure.add_subplot(111)
        ax.plot([1, 2, 3, 4, 5])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
