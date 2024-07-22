import numpy as np
import cv2

# a) Resize các ảnh đầu vào về cùng kích thước:
bg1_image = cv2.imread(
    '/Users/hainguyen/Library/CloudStorage/GoogleDrive-nguyenhai95aio@gmail.com/My Drive/AIO-2024/AIO-2024-EXERCISE/MODULE-2-CALCULUS AND LINEAR ALGEGRA-APP TO AI/WEEK2/GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))
ob_image = cv2.imread(
    '/Users/hainguyen/Library/CloudStorage/GoogleDrive-nguyenhai95aio@gmail.com/My Drive/AIO-2024/AIO-2024-EXERCISE/MODULE-2-CALCULUS AND LINEAR ALGEGRA-APP TO AI/WEEK2/Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread(
    '/Users/hainguyen/Library/CloudStorage/GoogleDrive-nguyenhai95aio@gmail.com/My Drive/AIO-2024/AIO-2024-EXERCISE/MODULE-2-CALCULUS AND LINEAR ALGEGRA-APP TO AI/WEEK2/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


# b) Xây dựng hàm compute_difference():
def compute_difference(bg_img, input_img):
    diff = cv2.cvtColor(input_img - bg_img, cv2.COLOR_BGR2GRAY)
    return diff


# c) Xây dựng hàm compute_binary_mask():
def compute_binary_mask(diff_img):
    mask = np.where(diff_img > 5., 255., 0.)
    return mask


# d) Xây dựng hàm replace_background():
def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = np.repeat(compute_binary_mask(
        difference_single_channel)[..., np.newaxis], 3, axis=2)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


result = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('Replaced art', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
