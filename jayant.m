% Carregando a imagem
image = imread('imagem.png');

% Transformando a imagem em um array de pontos de cor
points = reshape(image, [], 3);

% Definindo o número de clusters para a quantização vetorial
n_clusters = 16;

% Criando o modelo de KMeans
[idx, centroids] = kmeans(points, n_clusters);

% Obtendo os rótulos de cada ponto de cor
labels = idx;

% Criando a nova imagem com base nos centroides
quantized_image = zeros(size(points));
for i = 1:size(points, 1)
    quantized_image(i, :) = centroids(labels(i), :);
end

% Redimensionando a imagem para a forma original
quantized_image = reshape(quantized_image, size(image));

% Exibindo a imagem original e a imagem quantizada
figure;
subplot(1, 2, 1);
imshow(image);
title('Imagem original');
subplot(1, 2, 2);
imshow(quantized_image);
title('Imagem quantizada');
