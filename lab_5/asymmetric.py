import logging

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger('CryptoApp')


class Asymmetric:
    @staticmethod
    def generate_keys() -> tuple:
        logger.debug("Генерация RSA ключей: начало")
        try:
            keys = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            logger.info("RSA ключи успешно сгенерированы")
            return keys, keys.public_key()
        except Exception as e:
            logger.error(f"Ошибка генерации RSA ключей: {e}")
            raise

    @staticmethod
    def encrypt_str(original_data: str, public_key) -> bytes:
        logger.debug(f"Шифрование строки ({len(original_data)} символов)")
        try:
            text = bytes(original_data, 'UTF-8')
            encrypted  = public_key.encrypt(text,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(),
                                                   label=None
                                                   )
                                      )
            logger.info(f"Строка зашифрована ({len(encrypted)} байт)")
            return encrypted
        except Exception as e:
            logger.error(f"Ошибка шифрования строки: {e}")
            raise

    @staticmethod
    def encrypt_bytes(original_bytes: bytes, public_key):
        try:
            logger.debug(f"Шифрование байтового массива ({len(original_bytes)} байт)")
            encrypted =  public_key.encrypt(original_bytes,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256())
                                                   , algorithm=hashes.SHA256(),
                                                   label=None
                                                   )
                                            )
            logger.info(f"Байтовый массив зашифрован ({len(encrypted)} байт)")
            return encrypted
        except Exception as e:
            logger.error(f"Ошибка шифрования байтов: {e}")
            raise

    @staticmethod
    def decrypt(encrypt_text: bytes, private_key) -> str:
        logger.debug(f"Дешифрование данных ({len(encrypt_text)} байт)")
        try:
            decrypted  = private_key.decrypt(encrypt_text,
                                             padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                     algorithm=hashes.SHA256(),
                                                          label=None
                                                          )
                                             )
            logger.info(f"Данные дешифрованы ({len(decrypted)} байт)")
            return decrypted
        except Exception as e:
            logger.error(f"Ошибка дешифрования: {e}")
            raise
