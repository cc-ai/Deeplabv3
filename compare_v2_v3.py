
import os
import numpy as np
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

path_imgs_v2 ='/network/tmp1/ccai/data/provinces_images/'
path_masks_v2 = '/network/tmp1/ccai/data/provinces_masks/'

path_v3 = './results_2/'

masks_v3 = sorted([os.path.join(path_v3, x) for x in os.listdir(path_v3) if x.endswith('pred.png')], key =  lambda x: int(os.path.basename(x).split("_")[0]))
image_v3 = sorted([os.path.join(path_v3, x) for x in os.listdir(path_v3) if x.endswith('image.png')], key =  lambda x: int(os.path.basename(x).split("_")[0]))

image_v2 = sorted([os.path.join(path_imgs_v2, x) for x in os.listdir(path_imgs_v2)])
masks_v2 = sorted([os.path.join(path_masks_v2, x) for x in os.listdir(path_masks_v2)])

def overlay(image, pred):
    image = image.resize(pred.size)
    fig = plt.figure(figsize =(15,10))
    plt.imshow(image)
    plt.axis('off')
    plt.imshow(pred, alpha=0.5)
    ax = plt.gca()
    ax.xaxis.set_major_locator(matplotlib.ticker.NullLocator())
    ax.yaxis.set_major_locator(matplotlib.ticker.NullLocator())
    plt.show()
    return(fig)
    #plt.savefig(os.path.join(opts.save_val_results_path,'%d_overlay.png' % img_id), bbox_inches='tight', pad_inches=0)

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def main():
    save_path = './overlays'

    for i in range(len(masks_v2)):
        figv2 = overlay(Image.open(image_v2[i]), Image.open(masks_v2[i]))
        figv3 = overlay(Image.open(image_v3[i]), Image.open(masks_v3[i]))
        figv2.savefig("tmpv2.png")
        figv3.savefig("tmpv3.png")
        imgv2 = Image.open("tmpv2.png")
        imgv3 = Image.open("tmpv3.png")
        im = get_concat_v(imgv2, imgv3).save(os.path.join(save_path, os.path.basename(image_v2[i])))
        
if __name__ == "__main__":
    main()




