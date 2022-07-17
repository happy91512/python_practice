from cv2 import CV_16S, CV_8U
import numpy as np
import cv2
import os

class get_smooth:
    def gaussian_img(src_img, savePath, kernelSize, detect_depth, sig):
        src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
        X = cv2.getGaussianKernel(ksize=kernelSize, sigma=sig)
        gaussian = X * X.T  # gaussian kernel
        dst = cv2.filter2D(src_img, detect_depth, gaussian, dst=-1)
        dst = dst.astype("uint8")
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        cv2.imwrite(savePath, dst)
        return dst

    def mean_img(src_img, savePath, kernelSize, detect_depth):
        src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
        mean = np.ones((kernelSize, kernelSize), np.float32) / (
            pow(kernelSize, 2)
        )  # mean kernel
        dst = cv2.filter2D(src_img, detect_depth, mean, dst=-1)
        dst = dst.astype("uint8")
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        cv2.imwrite(savePath, dst)
        return dst

    def medium_img(src_img, savePath, kernelSize):
        src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
        dst = cv2.medianBlur(src_img, kernelSize)
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        cv2.imwrite(savePath, dst)

class get_edge(get_smooth):
    def canny_img(src_img, savePath, kernelSize):
        dst = cv2.Canny(src_img, 100, 150, apertureSize=kernelSize)
        cv2.imwrite(savePath, dst)

    def sobel_img(src_img, savePath, kernelSize, detect_depth):
        x_img = cv2.Sobel(src_img, detect_depth, 1, 0, ksize=kernelSize)
        y_img = cv2.Sobel(src_img, detect_depth, 0, 1, ksize=kernelSize)
        absX = cv2.convertScaleAbs(x_img)
        absY = cv2.convertScaleAbs(y_img)
        dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        dst = dst.astype(dtype=np.uint8)
        print(savePath)
        #cv2.imwrite(savePath + "X" + "_8U" + str(count) + ".png", absX)
        #cv2.imwrite(savePath + "Y" + "_8U" + str(count) + ".png", absY)
        #cv2.imwrite(savePath + "_8U" + str(count) + ".png", dst)
        #cv2.imshow("hi", absX)
        #cv2.waitKey(0)
        return dst

    def canny_complex_img(srcimg, ksize, gaussian_blur_savePath, mean_blur_savePath):
        retval = cv2.useOptimized()
        cv2.setUseOptimized(True)
        print("Optimized:", retval)
    #----------------------------------------------------
        gaussian_blur_img = get_smooth.gaussian_img(src_img = srcimg, savePath="./aaaa.jpg", kernelSize=5, detect_depth=CV_16S, sig=1)
        mean_blur_img = get_smooth.mean_img(src_img = srcimg, savePath="./bbbb.jpg", kernelSize=5, detect_depth=CV_16S)
        os.remove("./aaaa.jpg")
        os.remove("./bbbb.jpg")
        gaussian_dst = cv2.Canny(gaussian_blur_img, 100, 150, apertureSize=ksize)
        mean_dst = cv2.Canny(mean_blur_img,50, 80, apertureSize=ksize)
        cv2.imwrite(gaussian_blur_savePath, gaussian_dst) 
        cv2.imwrite(mean_blur_savePath, mean_dst) 

    def sobel_complex_img(srcimg, ksize, gaussian_blur_savePath, mean_blur_savePath):
        gaussian_blur_img = get_smooth.gaussian_img(src_img = srcimg, savePath="./aaaa.jpg", kernelSize=5, detect_depth=CV_16S, sig=1)
        mean_blur_img = get_smooth.mean_img(src_img = srcimg, savePath="./bbbb.jpg", kernelSize=5, detect_depth=CV_16S)
        os.remove("./aaaa.jpg")
        os.remove("./bbbb.jpg")
        gaussian_dst = get_edge.sobel_img(gaussian_blur_img, savePath="./aaaa.jpg", kernelSize=ksize, detect_depth=CV_16S)
        mean_dst = get_edge.sobel_img(mean_blur_img, savePath="./aaaa.jpg", kernelSize=ksize, detect_depth=CV_16S)
        cv2.imwrite(gaussian_blur_savePath, gaussian_dst) 
        cv2.imwrite(mean_blur_savePath, mean_dst) 
    

if __name__ == "__main__":
    img = cv2.imread("filter_pra/lena_gaussian-noise.png", 0)
    for i in range(2):
        smooth_ksize_list = [3, 7, 15]
        edge_ksize_list = [3, 5, 7]
        complex_ksize_list = [3,5]
        """
        get_edge.canny_complex_img(
            srcimg=img,
            gaussian_blur_savePath=f"filter_pra/complex_img/gaussuan_blur-STD{complex_ksize_list[i]}.png",
            mean_blur_savePath=f"filter_pra/complex_img/mean_blur-STD{complex_ksize_list[i]}.png",
            ksize=smooth_ksize_list[i],
            #detect_depth=CV_16S
        )"""
        get_edge.sobel_complex_img(
        srcimg=img,
        gaussian_blur_savePath=f"filter_pra/complex_img/gaussuan_blur-gaussian_noise{complex_ksize_list[i]}.png",
        mean_blur_savePath=f"filter_pra/complex_img/mean_blur-gaussian_noise{complex_ksize_list[i]}.png",
        ksize=smooth_ksize_list[i],
        #detect_depth=CV_16S
        )



        """
        get_edge.canny_img(
            src_img=img,
            savePath=f"/home/tdd/git/filter_pra/canny_img/canny-STD{i}.jpg",
            kernelSize=edge_ksize_list[i],
        )
        get_edge.sobel_img(
            src_img=img,
            savePath=f"filter_pra/sobel_img/sobel-std",
            kernelSize=edge_ksize_list[i],
            detect_depth=CV_8U,
            count=i,
        )
        get_smooth.gaussian_img(
            src_img=img,
            savePath=f"filter_pra/Gaussian_img/gaussian-std{i}.png",
            kernelSize=smooth_ksize_list[i],
            detect_depth=CV_16S,
            sig=(i if i != 0 else 0.5),
        )
        get_smooth.mean_img(
            src_img=img,
            savePath=f"filter_pra/mean_img/mean-std{i}.png",
            kernelSize=smooth_ksize_list[i],
            detect_depth=CV_16S,
        )
        get_smooth.medium_img(
            src_img=img,
            savePath=f"filter_pra/medium_img/medium-std{i}.png",
            kernelSize=smooth_ksize_list[i],
        )"""
