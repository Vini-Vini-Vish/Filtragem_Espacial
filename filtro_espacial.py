import numpy as np
from PIL import Image
from numpy import asarray
from scipy import ndimage


def main():
    # Abre a imagem
    #img/tbt_silvie.png
    image = Image.open('img_f/silvie_ff.jpg')
    #image.show()

    # Converte a imagem para np array
    npImage = np.array(image).astype(int)

    # values os a windows 5 X 5
    print(npImage[0:5, 0:5])

    # Kernel's
    kernelA = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    kernelB = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])

    kernelC = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

    kernelD = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    kernelE = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    kernelF = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    kernelF = (kernelF*(1/9))

    kernelG = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    kernelG = (kernelG*(1/16))

    kernelH = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4],
                        [6, 24, 36, 24, 6], [4, 16, 24, 16, 4],
                        [1, 4, 6, 4, 1]])
    kernelH = (kernelH*(1/256))

    kernelI = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4],
                        [6, 24, -476, 24, 6], [4, 16, 24, 16, 4],
                        [1, 4, 6, 4, 1]])
    kernelI = (kernelI * (-1 / 256))

    # Aplicando os Kernel's
    imageA = ndimage.convolve(npImage, kernelA, mode='reflect')

    imageB = ndimage.convolve(npImage, kernelB, mode='reflect')

    imageC = ndimage.convolve(npImage, kernelC, mode='reflect')

    imageD = ndimage.convolve(npImage, kernelD, mode='reflect')

    imageE = ndimage.convolve(npImage, kernelE, mode='reflect')

    imageF = ndimage.convolve(npImage, kernelF, mode='reflect')

    imageG = ndimage.convolve(npImage, kernelG, mode='reflect')

    imageH = ndimage.convolve(npImage, kernelH, mode='reflect')

    imageI = ndimage.convolve(npImage, kernelI, mode='reflect')

    # Converte o np array para imagem Pillow
    resultadoA = Image.fromarray(imageA)
    resultadoA.convert('L').save('img_num/A.tiff')

    resultadoB = Image.fromarray(imageB)
    resultadoB.convert('L').save('img_num/B.tiff')

    resultadoC = Image.fromarray(imageC)
    resultadoC.convert('L').save('img_num/C.tiff')

    resultadoD = Image.fromarray(imageD)
    resultadoD.convert('L').save('img_num/D.tiff')

    resultadoE = Image.fromarray(imageE)
    resultadoE.convert('L').save('img_num/E.tiff')

    resultadoF = Image.fromarray(imageF)
    resultadoF.convert('L').save('img_num/F.tiff')

    resultadoG = Image.fromarray(imageG)
    resultadoG.convert('L').save('img_num/G.tiff')

    resultadoH = Image.fromarray(imageH)
    resultadoH.convert('L').save('img_num/H.tiff')

    resultadoI = Image.fromarray(imageI)
    resultadoI.convert('L').save('img_num/I.tiff')

if __name__ == "__main__":
    main()
