import cv2
import numpy as np

def apply_mirror_convolution(image, kernel):
    # Adiciona uma borda de zeros à imagem para não perder pixels durante a convolução
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)

    # Inverte o kernel horizontalmente e verticalmente
    kernel = np.flip(kernel, axis=0)
    kernel = np.flip(kernel, axis=1)

    # Aplica a convolução espelhada
    result = np.zeros_like(image)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            sub_image = image[i-1:i+2, j-1:j+2]
            sub_result = np.multiply(sub_image, kernel)
            result[i, j] = np.sum(sub_result)

    # Remove a borda adicionada anteriormente
    result = result[1:-1, 1:-1]

    return result

# Exemplo de uso
if __name__ == '__main__':
    # Carrega a imagem
    image = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

    # Define o kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # Aplica a convolução espelhada
    result = apply_mirror_convolution(image, kernel)

    # Mostra a imagem original e a imagem resultante
    cv2.imshow('Original', image)
    cv2.imshow('Resultado', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

/*A convolução espelhada é uma técnica comum de processamento de imagens utilizada para filtrar uma imagem. 
Ela consiste em aplicar um kernel (uma matriz de números) na imagem, multiplicando cada valor do kernel com 
os valores dos pixels correspondentes na imagem e somando os resultados. Essa operação é feita em todos os 
pixels da imagem, gerando uma nova imagem resultante.
Na convolução espelhada, o kernel é invertido horizontalmente e verticalmente antes de ser aplicado à imagem. 
Isso é feito para garantir que o efeito do kernel seja aplicado corretamente na imagem. Além disso, é comum 
adicionar uma borda de pixels de valor zero ao redor da imagem antes de aplicar a convolução, para evitar que 
pixels sejam perdidos durante o processo
*/