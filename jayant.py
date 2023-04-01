from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
image = plt.imread('imagem.png')

# Transformando a imagem em um array de pontos de cor
points = image.reshape((-1, 3))

# Definindo o número de clusters para a quantização vetorial
n_clusters = 16

# Criando o modelo de KMeans
kmeans = KMeans(n_clusters=n_clusters)

# Treinando o modelo com os pontos de cor
kmeans.fit(points)

# Obtendo os centroides dos clusters
centroids = kmeans.cluster_centers_

# Obtendo os rótulos de cada ponto de cor
labels = kmeans.labels_

# Criando a nova imagem com base nos centroides
quantized_image = np.zeros_like(points)
for i in range(len(points)):
    quantized_image[i] = centroids[labels[i]]

# Redimensionando a imagem para a forma original
quantized_image = quantized_image.reshape(image.shape)

# Exibindo a imagem original e a imagem quantizada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Imagem original')
plt.subplot(1, 2, 2)
plt.imshow(quantized_image)
plt.title('Imagem quantizada')
plt.show()