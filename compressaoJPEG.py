import numpy as np
import cv2
import math
import scipy.fftpack as fftpack

def jpeg_compress(image, quality=50):
    # Converte a imagem para o formato YCrCb
    image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Divide a imagem em blocos de 8x8 pixels
    blocks = np.zeros_like(image_ycrcb)
    for i in range(0, image_ycrcb.shape[0], 8):
        for j in range(0, image_ycrcb.shape[1], 8):
            blocks[i:i+8, j:j+8, :] = image_ycrcb[i:i+8, j:j+8, :]

    # Aplica a Transformada de Cosseno Discreta (DCT) a cada bloco
    dct_blocks = fftpack.dct(fftpack.dct(blocks, axis=0, norm='ortho'), axis=1, norm='ortho')

    # Define a matriz de quantização para a luminância (Y)
    QY = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 58, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

    # Define a matriz de quantização para a crominância (Cr e Cb)
    QC = np.array([[17, 18, 24, 47, 99, 99, 99, 99],
                   [18, 21, 26, 66, 99, 99, 99, 99],
                   [24, 26, 56, 99, 99, 99, 99, 99],
                   [47, 66, 99, 99, 99, 99, 99, 99],
                   [99, 99, 99, 99, 99, 99, 99, 99],
                   [99, 99, 99, 99, 99, 99, 99, 99],
                   [99, 99, 99, 99, 99, 99, 99, 99],
                   [99, 99, 99, 99, 99, 99, 99, 99]])

    # Calcula os fatores de qualidade de acordo com o parâmetro "quality"
    if quality < 50:
        scale = math.floor(5000
