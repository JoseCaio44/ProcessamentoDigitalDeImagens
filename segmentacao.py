import cv2

# Carrega a imagem em escala de cinza
img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica a limiarização com um valor de limiar fixo
limiar, img_limiar = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Exibe a imagem original e a imagem limiarizada
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Limiarizada', img_limiar)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------- Watershed

# Carrega a imagem em escala de cinza
img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica o filtro da transformada de distância
dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 5)
ret, img_threshold = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

# Aplica a transformada de Watershed para segmentar a imagem
img_labels = cv2.connectedComponents(img_threshold)[1]
img_labels = cv2.watershed(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), img_labels)

# Desenha as bordas dos objetos segmentados na imagem original
img[img_labels == -1] = [0, 0, 255]
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Exibe a imagem original com as bordas dos objetos segmentados
cv2.imshow('Imagem Watershed', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------- Crescimento de Regiões

# Carrega a imagem em escala de cinza
img = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

# Define as sementes para o algoritmo de crescimento de regiões
seed_points = [(100, 100), (200, 200), (300, 300)]

# Define a função que será usada para determinar se um pixel é semelhante a um ponto semente
def is_similar(pixel_value, seed_value, tolerance=10):
    return abs(int(pixel_value) - int(seed_value)) < tolerance

# Inicializa a imagem resultante com zeros
img_result = np.zeros_like(img)

# Itera sobre as sementes e executa o algoritmo de crescimento de regiões
for seed in seed_points:
    # Inicializa a lista de pixels a serem analisados com a semente
    pixel_list = [seed]

    # Inicializa a lista de pixels já visitados
    visited_pixels = []

    # Enquanto houver pixels na lista de pixels a serem analisados
    while len(pixel_list) > 0:
        # Seleciona o próximo pixel da lista de pixels a serem analisados
        pixel = pixel_list.pop()

        # Adiciona o pixel aos pixels já visitados
        visited_pixels.append(pixel)

        # Obtém o valor do pixel na imagem original
        pixel_value = img[pixel[1], pixel[0]]

        # Define o valor do pixel na imagem resultante
        img_result[pixel[1], pixel[0]] = 255

        # Verifica se os vizinhos do pixel são semelhantes ao ponto semente
        for i in range(pixel[0]-1, pixel[0]+2):
            for j in range(pixel[1]-1, pixel[1]+2):
                if (i >= 0 and i < img.shape[1] and j >= 0 and j < img.shape[0] and 
                        (i,j) not in visited_pixels and 
                        is_similar(img[j, i], img[seed[1], seed[0]])):
                    pixel_list.append((i, j))

# Exibe a imagem resultante
cv2
