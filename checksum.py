import hashlib


def hashCal(path, algo='md5'):
    hasher = hashlib.new(algo)

    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()
