# Python s60 Nokia 6630 -- Time Lapse Photography
# By Eirik Solheim -- http://eirikso.com
# Based on:
# Python s60 3rd Edition -- Time lapse Photography for Nokia N80
# Code by Anteater -- http://blog.foozia.com

import camera
import appuifw

from time import sleep, time
import urllib


nameOfProject = appuifw.query(u"Name of project:", "text")

numImages = 1000000 # Just fill the card.
#numImages = appuifw.query(u"Number of images:", "number")

delay = appuifw.query(u"Delay in seconds (0 for 'as fast as possible'):", "number")

print "Starting..."

x = 0
while x < numImages:
    start = time()

    try:
        print "Snapping image number: " + str(x)
        image = camera.take_photo(size=(640,480))
        filename="e:\\timelapse\\%s_%04d.jpg"%( nameOfProject, x )
        print "Saving image %s"%filename
        image.save(filename)
    except Exception, e:
        print("Error taking photo: %s", e)
    
    # work out how long taking the photo took. Sleep long enough
    # to maintain a constant frame rate.
    finish = time()
    sleeptime = delay - ( finish - start )
    if sleeptime >= 0:
        sleep(sleeptime)
    elif delay > 0:
        # nothing we can do, but might as well warn about it.
        print("Warning: Photo took %f seconds to take, which is longer than the photo delay."%( finish - start ) )

    x +=1

print "All done"