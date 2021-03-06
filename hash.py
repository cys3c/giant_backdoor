# Opens a file given by targetFile, steps through block by block
# and generates a sha256.  Displays the resulting sha256
import hashlib

def calculate_sha256(targetFile):
    sha256 = hashlib.sha256()

    with open(targetFile, 'rb') as f:
        for block in iter(lambda: f.read(65536), b''):
            sha256.update(block)

    return sha256.hexdigest()

def calculate_md5(targetFile):
    hash_md5 = hashlib.md5()

    with open(targetFile, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            hash_md5.update(block)

    return hash_md5.hexdigest()