# Create an Executable Program to Quickly Check Raster Files

*Created by Zhen Liu*  
Have questions about this tutorial? Email me at: [zhenliu3@clarku.edu](zhenliu3@clarku.edu)

## Introduction
Have you ever been in a situation that you only want to check a raster file but don't want to open a big software, like ArcGIS Map? If your answer is Yes, this light computer program is just what you need. The program can open a raster file quickly and the user can check the statistics of the file. The video below shows how the program works. The user drag the file and drop it in the program. The image and its statistics will be automatically displayed.
![ResultAnimation.gif](image/ResultAnimation.gif)  
In this tutorial, I will show you how to create it in Python.We are going to use several useful libraries in Pythons. There are PyQt5, Gdal, Matplotlib, and PyInstaller.

## Set up
Before we start coding, we need to install the libraries we need. The most common way is to use **pip** command. Open the terminal, type the commands below to install the required libraries.
```
pip install PyQt5
pip install gdal
pip install matplotlib
pip intsall PyInstaller
```
If you cannot install any of them in your environment, I recommend the other way to install libraries. we can download .whl file in the [website](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Please be careful of the version and requirements when you download the file. For example, GDAL‑3.0.4‑cp36‑cp36m‑win_amd64.whl incicates that the version of Gdal library is 3.0.4. cp36 indicates the version of Python should be 3.6. amd64 denotes the system type should be 64 bit. After download, write the command in the terminal to install the library. The command should be like:
```
pip install  C:/some-dir/some-file.whl
```

## Step 1. Design the Interface
The first step is to design a user interface for the program. QT library is one of the most powerful GUI libraries. PyQt5 is a set of Python bindings for QT applications. There are two ways to design a interface.  
First, you can use software named Qt Designer. Qt Designer is the Qt tool for designing and building graphical user interfaces (GUIs) with Qt Widgets. You can compose and customize your windows or dialogs in a what-you-see-is-what-you-get (WYSIWYG) manner, and test them using different styles and resolutions. The software can be downloaded at [this](https://build-system.fman.io/qt-designer-download). It also provides a detailed [tutorial](https://doc.qt.io/qt-5/gettingstarted.html).  
The second way is to write code using the libary directly. That's what we do in this tutorial. PyQt5 has a set of useful modules. We are going to use two of them:
* **QtWidgets**: The QtWidgets module contains classes that provide a set of UI elements to create classic desktop-style user interfaces.
* **QtCore**: The QtCore module contains the core non-GUI functionality. This module is used for working with time, files and directories, various data types, streams, URLs, mime types, threads or processes.

First, import the modules we need. **QApplication** is to manages the GUI application’s control flow and main settings. It should be put in the main function to initialize and finalize the widgets. **QMainWindow** is the class for a framework for building an application's user interface. **QLabel** is the class for the texts in the interface. **QMessageBox** is the class for dialogs. This is a little popup window that you’ve often seen on your desktop. The modules imported from QtCore are supplements for the interface designing.
```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QRect
```

Let's go through the code.
```
class Appdemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setAcceptDrops(True)
        self.label_1 = QLabel("Drop files here", self)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setStyleSheet("border:2px dashed #242424;")
        self.label_1.setGeometry(QRect(10, 10, 180, 180))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Appdemo()
    demo.show()
    sys.exit(app.exec())
```
In the class Appdemo, we also need to add some functions to make the program react when the user drag files and drop them in the program.
```
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
```
## log
0518: finish the main windows UI design. finish the showing function.1

To do:
1. property window after droping
2. show multiple windows when drop more than one files.
3. dash line label to notify drop files

## reference links
1. The video shows how to use a drag and drop function in PyQt5. https://www.youtube.com/watch?v=KVEIW2htw0A