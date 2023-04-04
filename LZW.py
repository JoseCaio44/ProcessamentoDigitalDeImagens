import struct

def compress_LZW(data):
    dictionary_size = 256
    dictionary = dict((i, chr(i)) for i in range(dictionary_size))

    result = []
    w = ""
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dictionary_size
            dictionary_size += 1
            w = c

    if w:
        result.append(dictionary[w])

    return result

def encode_LZW(data):
    compressed_data = compress_LZW(data)
    return struct.pack('>' + 'H' * len(compressed_data), *compressed_data)

def decode_LZW(data):
    dictionary_size = 256
    dictionary = dict((chr(i), i) for i in range(dictionary_size))

    compressed_data = struct.unpack('>' + 'H' * (len(data) // 2), data)

    result = []
    w = compressed_data[0]
    result.append(chr(w))
    for k in compressed_data[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dictionary_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.append(entry)

        dictionary[dictionary_size] = w + entry[0]
        dictionary_size += 1

        w = entry

    return ''.join(result)
