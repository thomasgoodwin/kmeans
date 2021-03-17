#thomas goodwin
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np

def process_image(image_prefix_name, filetype, min, max):
    for i in range(min, max + 1):

        im = Image.open(image_prefix_name + filetype)
        picture = im.load()
        pixels = list(im.getdata())

        pixels = np.array(pixels)
        kmeans = KMeans(n_clusters=i, random_state=0,).fit(pixels)
        for x in range(im.width):
            for y in range(im.height):
                temp = tuple(kmeans.cluster_centers_[kmeans.labels_[x + im.width *y]])
                if(filetype == '.png'):
                    picture[x,y] = (int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]))
                elif(filetype == '.jpg'):
                    picture[x,y] = (int(temp[0]), int(temp[1]), int(temp[2]))
        im.save(image_prefix_name + str(i) + filetype)

#process_image('regal', '.jpg', 3, 10)
#process_image('cat', '.jpg', 3, 10)
#process_image('flower', '.jpg', 3, 10)

