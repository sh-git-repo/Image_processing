'''
NAME:
    solution.py

DESCRIPTION:
    Demo solution of how we can use all the classes.

FUNCTIONS:
    solution()
    ---------------------
        Self explanatory.
    ---------------------
'''
from filters import MedianFilter
from noise import SnPNoise
from PIL import Image

IMAGE_PATH = "sample_image//peppers.jpg"

def solution():
    ''' Self explanatory. '''
    original_image = Image.open(IMAGE_PATH).convert('L')
    original_image.show()

    snp_noise = SnPNoise(IMAGE_PATH, 0.02)
    noisy_mat = snp_noise.add_noise()
    noisy_img = Image.fromarray(noisy_mat)
    noisy_img.show()

    med_filter = MedianFilter(IMAGE_PATH, 3)
    med_filter.img = noisy_mat
    filtered_img = Image.fromarray(med_filter.filter())
    filtered_img.show()


if __name__ == "__main__":
    solution()

