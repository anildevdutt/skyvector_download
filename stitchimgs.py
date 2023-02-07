import numpy as np
import cv2

#coordinates are same as before but this time we are reading images from our local disk
#so plug in the same numbers as you have done in download script
#you can change the number if you want, as long as that range of imgs are download you are good to go.
xstart = 1300
xend = 1565
ystart = 775
yend = 1021

#each image is 256x256 if you want to reduce the size  before making a big image then reduce the pct number (1-100)
#here its set to 95% which is 95% of the original width and 95% of original height(so technically the final img is much smaller than 95% but whatever)
pct = 95
res = int(256 * pct/100.0)

#just crerating a blank plate for the final image
finalimg = np.zeros((res*(yend-ystart+1), res*(xend-xstart+1), 3), dtype=np.uint8)

r = 0
c = 0

#same story as downloading script, 2 loops to go over all the coordinates
for x in range(xstart, xend+1):
    c = 0
    for y in range(ystart, yend+1):
        #reading the image from the vfr folder
        fnm = 'vfr/' + str(x) + '_' + str(y) + '.jpg'
        img = cv2.imread(fnm)
        #resizing the image based on the pct given
        imgresized = cv2.resize(img, (res, res))
        #adding this img to the final img in a grid pattern
        #final img is a big square, each img is a small square.
        #we are filling up this big square by adding small squares at right location.
        finalimg[c:c+imgresized.shape[0], r:r+imgresized.shape[1]] += imgresized
        c += res    
    r += res

#writing the final image to disk, you can change the file name
cv2.imwrite("finalvfr.jpg", finalimg)