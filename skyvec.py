import requests

# sample url of VFR https://t.skyvector.com/V7pMh4zRihflnr61/301/2301/1/1407/802.jpg

# URL of the image without inculding the Y, X coordinate infomration from above URl
skyvecurl = 'https://t.skyvector.com/V7pMh4zRihflnr61/301/2301/1/'

#In skyvec Zoom in as munch as possible on top left cornor and find the url of that image.
#Plug in the Y, X information from that URL in the Xstart , Ystart variables
#do the same at bottom right cornor and plug in those numebrs

xstart = 1300
xend = 1565
ystart = 770
yend = 1022


#two loops that go over every coordinate eg([[1300, 770], [1300,771]...[1300, 1022]] [[1301, 770]....])

for x in range(xstart, xend+1):
    for y in range(ystart, yend+1):
        # adding the x, y coordinate to the skyvecurl URL and storing it in requrl
        requrl = skyvecurl + str(x)+ '/' + str(y) + '.jpg'
        print(requrl)
        res = requests.get(requrl, stream = True)
        #saving the image to vfr folder (you need to create this folder in the same directory where your script is)
        with open('vfr/' + str(x) + '_' + str(y) + '.jpg', 'wb') as f:
            f.write(res.content)
