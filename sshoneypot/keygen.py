"""Operations on ssh keys"""
import os

from Crypto.PublicKey import RSA


KEY_DIRECTORY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'ssh_key',
)
KEY_PATH = os.path.join(KEY_DIRECTORY_PATH, 'private.key')


def key_exists():
    """Check if key file already exists"""
    return os.path.isfile(KEY_PATH)


def generate():
    """Generate new key"""
    if not os.path.exists(KEY_DIRECTORY_PATH):
        os.makedirs(KEY_DIRECTORY_PATH)
    key = RSA.generate(2048)
    with open(KEY_PATH, 'wb') as content_file:
        os.chmod(KEY_PATH, 0o600)
        content_file.write(key.exportKey('PEM'))


def generate_unexisting_key():
    if not key_exists():
        generate()