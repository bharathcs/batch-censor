# Batch Censor Image files with Python.
I needed to batch censor 1600 images with the exact same dimensions with the exact same censoring rectangle in the same position and couldn't find an easy tool to do so online. So I made my own. 

## Pre-requisite:
First off, you need python installed. You've likely used anaconda or you've installed it directly.

If you have anaconda installed, you probably already have Pillow installed or can easily install it by using its Anaconda's package manager. If your python isn't from Anaconda, use the command 'pip install Pillow' to install it.

## How to run it?

Lines 5 - 20 in 'batch_censor.py' are for you to set:
- the target folder of JPGs 
- the top-left most pixel to be censored (the x and y coordinates of the top-left pixel in the censor rectangle)
- the height and width of the censor rectangle
- the colour of the censor (black by default)

Once done, go to your terminal and run the edited python file:
For Windows:
C:\python27\python.exe {path to batch_censor.py}
For Mac:
python {path to batch_censor.py}

## Sample Pictures

They're from NASA. As such there's no copyright :)
Src: https://www.nasa.gov/multimedia/imagegallery/index.html