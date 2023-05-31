import cv2
import numpy as np

def calculate_lbp(image):
    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calcular o LBP para cada pixel
    lbp = np.zeros_like(gray, dtype=np.uint8)
    for i in range(1, gray.shape[0] - 1):
        for j in range(1, gray.shape[1] - 1):
            center = gray[i, j]
            code = 0
            code |= (gray[i-1, j-1] > center) << 7
            code |= (gray[i-1, j] > center) << 6
            code |= (gray[i-1, j+1] > center) << 5
            code |= (gray[i, j+1] > center) << 4
            code |= (gray[i+1, j+1] > center) << 3
            code |= (gray[i+1, j] > center) << 2
            code |= (gray[i+1, j-1] > center) << 1
            code |= (gray[i, j-1] > center) << 0
            lbp[i, j] = code
    
    return lbp

def calculate_lbp_histogram(lbp):
    # Calcular o histograma do LBP
    histogram = np.histogram(lbp.ravel(), bins=256, range=[0, 256])[0]
    return histogram

# Carregar a imagem
image = cv2.imread('caminho/para/a/imagem.jpg')

# Calcular o LBP
lbp = calculate_lbp(image)

# Calcular o histograma do LBP
histogram = calculate_lbp_histogram(lbp)

# Imprimir o vetor de características (histograma)
print(histogram)
