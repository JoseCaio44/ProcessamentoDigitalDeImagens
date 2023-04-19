import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carrega a imagem
img = cv2.imread('imagem.jpg', 0)

# Calcula a Transformada de Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Aplica um filtro passa-baixa
rows, cols = img.shape
crow, ccol = rows//2, cols//2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0

# Apresenta o espectro de magnitude
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Imagem de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Espectro de magnitude'), plt.xticks([]), plt.yticks([])

# Aplica uma transformada inversa de Fourier para voltar para o domínio espacial
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Apresenta a imagem com filtro passa-baixa aplicado
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Imagem com filtro passa-baixa'), plt.xticks([]), plt.yticks([])
plt.show()

# Pergunta se o usuário deseja aplicar um filtro passa-alta
filtro_passa_alta = input("Deseja aplicar um filtro passa-alta? (S/N)")

if filtro_passa_alta.upper() == 'S':
    # Aplica um filtro passa-alta
    fshift[crow-10:crow+10, ccol-10:ccol+10] = 0
    fshift[0:rows//4, 0:cols//4] = 0
    fshift[3*rows//4:rows, 3*cols//4:cols] = 0

    # Apresenta o espectro de magnitude
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Espectro de magnitude com filtro passa-alta'), plt.xticks([]), plt.yticks([])

    # Aplica uma transformada inversa de Fourier para voltar para o domínio espacial
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    # Apresenta a imagem com filtro passa-alta aplicado
    plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
    plt.title('Imagem com filtro passa-alta'), plt.xticks([]), plt.yticks([])
    plt.show()
