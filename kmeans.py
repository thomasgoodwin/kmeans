#thomas goodwin
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np

X = np.array([[0,0,0], [1,1,1], [3,2,2], [0, 1, 1], [1, 3, 1], [2, 3, 1],
              [3,3,1], [2,2,2], [1,0,1], [3,2,1]])

starting_cen = np.array([[0,0,0], [1,1,1]])
kmeans = KMeans(n_clusters=2, random_state=0, init=starting_cen).fit(X)

for i in range(0,len(X)):
    print(X[i],kmeans.labels_[i])

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

