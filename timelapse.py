# Python s60 Nokia 6630 -- Time Lapse Photography
# By Eirik Solheim -- http://eirikso.com
# Based on:
# Python s60 3rd Edition -- Time lapse Photography for Nokia N80
# Code by Anteater -- http://blog.foozia.com

import camera
import appuifw
from time import sleep

nameOfProject = appuifw.query(u"Name of project:", "text")
numImages = appuifw.query(u"Number of images:", "number")
delay = appuifw.query(u"Delay in seconds:", "number")

print "Starting..."

x = 0
while x != numImages:
    try:
        print "Snapping image number: " + str(x)
        image = camera.take_photo(size=(640,480))
        filename="e:\\timelapse\\%s_%04d.jpg"%( nameOfProject, x )
        print "Saving image %s"%filename
        image.save(filename)
        sleep(delay)
    except Exception, e:
        print("Error: %s", e)

    x +=1

print "All done"