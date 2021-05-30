## set up
import sys
import numpy as np
from osgeo import gdal
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QRect

class Appdemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setAcceptDrops(True)
        self.label_1 = QLabel("Drop files here", self)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setStyleSheet("border:2px dashed #242424;")
        self.label_1.setGeometry(QRect(10, 10, 180, 180))
    ## To check whether the item has url. If it has, the event will be accepted. If not, the event will be ignored.
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        ## close all figures
        plt.close('all')
        event.accept()
        url_list = []
        for url in event.mimeData().urls():
            if(url.isLocalFile()):
                res_url = str(url.toLocalFile())
            else:
                res_url = url.toString()
            url_list.append(res_url)
        # print(url_list)
        image_num = 1
        for url in url_list:
            img = gdal.Open(url)
            bandarray = img.GetRasterBand(1).ReadAsArray()
            plt.figure(image_num)
            image_num+=1
            fig = plt.gcf()
            fig.canvas.manager.set_window_title(url.split('/')[-1])
            plt.imshow(bandarray)
            plt.axis('off')
            plt.show()
            min = np.min(np.array(bandarray))
            average = np.average(np.array(bandarray))
            max = np.max(np.array(bandarray))
            col = np.array(bandarray).shape[1]
            row = np.array(bandarray).shape[0]
            stats = "row: "+ str(row) + "\n" + "col: "+ str(col) + "\n" + "min: "+ str(min) + "\n" + "max: "+ str(max) + "\n" + "mean: "+ str(average) + "\n"
            QMessageBox.about(self, url.split('/')[-1], stats)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Appdemo()
    demo.show()
    sys.exit(app.exec())

