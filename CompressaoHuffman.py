import heapq
import os

class HuffmanNode:
    def __init__(self, freq, pixel=None):
        self.freq = freq
        self.pixel = pixel
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

class HuffmanTree:
    def __init__(self, pixels):
        self.pixels = pixels
        self.tree = self.build_tree()

    def build_tree(self):
        heap = [HuffmanNode(freq=pixels.count(pixel), pixel=pixel) for pixel in set(pixels)]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = HuffmanNode(left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]

    def encode_table(self):
        table = {}
        self.build_table(table, self.tree, '')
        return table

    def build_table(self, table, node, code):
        if node is None:
            return

        if node.pixel is not None:
            table[node.pixel] = code

        self.build_table(table, node.left, code + '0')
        self.build_table(table, node.right, code + '1')

    def encode(self, data):
        table = self.encode_table()
        encoded_data = ''.join(table[pixel] for pixel in data)
        return encoded_data, table

    def decode(self, data, table):
        current_code = ''
        decoded_data = []
        inverse_table = {code: pixel for pixel, code in table.items()}

        for bit in data:
            current_code += bit
            if current_code in inverse_table:
                pixel = inverse_table[current_code]
                decoded_data.append(pixel)
                current_code = ''

        return decoded_data


def compress_Huffman(data):
    tree = HuffmanTree(data)
    encoded_data, table = tree.encode(data)

    # Salva a tabela de codificação em um arquivo auxiliar
    with open('table.txt', 'w') as f:
        for pixel, code in table.items():
            f.write(f"{pixel}: {code}\n")

    # Escreve a imagem comprimida em um arquivo
    with open('compressed.bin', 'wb') as f:
        # Salva a tabela como uma string binária
        table_str = str(table).encode('utf-8')
        table_size = len(table_str)
        f.write(table_size.to_bytes(4, byteorder='big'))
        f.write(table_str)

        # Salva a imagem codificada como uma string binária
        encoded_str = ''.join(format(ord(pixel), '08b') for pixel in encoded_data)
        encoded_size = len(encoded_str)
        f.write(encoded_size.to_bytes(4, byteorder='big'))
        f.write(int(encoded_str, 2).to_bytes((encoded_size + 7) // 8, byteorder='big'))


def decompress_Huffman():
    # Lê a tabela de codificação do arquivo auxiliar
    table = {}
    with open('table.txt', 'r') as f:
        for line in f:
            pixel, code = line.strip().split(': ')
            table[pixel] = code

    # Lê a imagem comprimida do arquivo
    with open('compressed.bin', 'rb')
