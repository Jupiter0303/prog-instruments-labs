import os
import logging

from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding

logger = logging.getLogger('CryptoApp')


class Symmetric:

    @staticmethod
    def encrypt(original_text: str, key: bytes) -> bytes:
        logger.debug(f"Начало симметричного шифрования ({len(original_text)} символов)")
        try:
            iv = os.urandom(8)
            logger.debug(f"Сгенерирован iv вектор ({len(iv)} байт)")

            cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
            encryptor = cipher.encryptor()

            padder = padding.ANSIX923(16).padder()
            text = bytes( original_text, 'UTF-8')
            padded_text = padder.update(text) + padder.finalize()
            logger.debug(f"Добавлен padding, размер данных: {len(padded_text)} байт")

            c_text = encryptor.update(padded_text) + encryptor.finalize()
            res = iv + c_text
            logger.info(f"Текст успешно зашифрован (итого {len(res)} байт)")

            return res
        except Exception as e:
            logger.error(f"Ошибка симметричного шифрования: {e}")
            raise

    @staticmethod
    def decrypt(encrypt_text:bytes, key) -> bytes:
        try:
            iv = encrypt_text[:8]
            logger.debug(f"Извлечен iv вектор ({len(iv)} байт)")

            cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
            decryptor = cipher.decryptor()

            dc_text = decryptor.update(encrypt_text[8:]) + decryptor.finalize()
            logger.debug(f"Данные дешифрованы, размер: {len(dc_text)} байт")

            unpadder = padding.ANSIX923(64).unpadder()
            unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
            logger.debug(f"Padding удален, финальный размер: {len(unpadded_dc_text)} байт")

            logger.info("Текст успешно дешифрован")

            return unpadded_dc_text
        except Exception as e:
            logger.error(f"Ошибка симметричного дешифрования: {e}")
            raise

    @staticmethod
    def generate_key() ->bytes:
        logger.debug("Генерация симметричного ключа IDEA")

        try:
            key = os.urandom(16)
            logger.info(f"Симметричный ключ сгенерирован ({len(key)} байт)")
            return key
        except Exception as e:
            logger.error(f"Ошибка генерации ключа: {e}")
            raise