from PIL import Image
from os import listdir, chdir, getcwd
from os.path import isfile, join

#### SETTINGS HERE ######################################################################
path_img_folder = '/Users/bhcs/code/batch_censor/sample_pics'
# replace the path above with the path to your folder
# ensure that only image files are in your folder.
censor_x = 50
censor_y = 50
# set the coordinates of the top-left corner of the rectangular censor (in pixels)
censor_height = 100
censor_width = 100
# set the height and width of this rectangular censor
censor_colour = (0, 0, 0) # This is black
# set the colour of your censor with the following table:
# black = (0,   0,   0  )
# red   = (255, 0,   0  )
# blue  = (0,   255, 0  )
# green = (0,   0,   255)
# white = (255, 255, 255)
#########################################################################################

# sets python to work on your specified directory
chdir(path_img_folder)
# makes a list of all the image filenames
image_paths = [f for f in listdir(path_img_folder) if isfile(join(path_img_folder, f))]
image_paths = [f for f in image_paths if '.jpg' in f]

# censors the listed files in the manner specified
def censor_and_copy(img_path):
    try:
        image = Image.open(img_path)
        for x in range (censor_x,censor_x + censor_width):
            for y in range (censor_y,censor_y + censor_height):
                pixel_coordinate = (x, y)
                image.putpixel(pixel_coordinate, censor_colour)
        image.save(img_path+'_censored.jpg')
    except Exception as e:
        print("When trying to process " + img_path + " as an image: ")
        print(e)

# Calls the functions and carries out the task.
for img_path in image_paths:
    censor_and_copy(img_path)
