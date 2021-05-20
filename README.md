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
If you cannot install anyone of them in your environment, I recommend the other way to install libraries. we can download .whl file in the [website](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Please be careful of the version and requirements when you download the file. For example, GDAL‑3.0.4‑cp36‑cp36m‑win_amd64.whl incicates that the version of Gdal library is 3.0.4. cp36 indicates the version of Python should be 3.6. amd64 denotes the system type should be 64 bit. After download, write the command in the terminal to install the library. The command should be like:
```
pip install  C:/some-dir/some-file.whl
```
## log
0518: finish the main windows UI design. finish the showing function.1

To do:
1. property window after droping
2. show multiple windows when drop more than one files.
3. dash line label to notify drop files

## reference links
1. The video shows how to use a drag and drop function in PyQt5. https://www.youtube.com/watch?v=KVEIW2htw0A