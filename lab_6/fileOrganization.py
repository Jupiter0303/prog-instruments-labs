import logging
from config import PUBLIC_PEM, PRIVATE_PEM
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

logger = logging.getLogger('CryptoApp')


def serialization_public_key(public_key)->None:
    logger.debug(f"Сериализация публичного ключа в файл: {PUBLIC_PEM}")
    try:
        with open(PUBLIC_PEM, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                 format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logger.info(f"Публичный ключ успешно сохранен в {PUBLIC_PEM}")
    except Exception as e:
        logger.error(f"Ошибка при сериализации публичного ключа: {e}")
        raise

def deserialization_public_key():
    logger.debug(f"Десериализация публичного ключа из файла: {PUBLIC_PEM}")
    try:
        with open(PUBLIC_PEM, 'rb') as pem_in:
            public_bytes = pem_in.read()
            logger.info(f"Публичный ключ успешно загружен из {PUBLIC_PEM}")
            return load_pem_public_key(public_bytes)
    except Exception as e:
        logger.error(f"Ошибка при десериализации публичного ключа: {e}")
        raise

def serialization_private_key(private_key)->None:
    logger.debug(f"Сериализация приватного ключа в файл: {PRIVATE_PEM}")
    try:
        with open(PRIVATE_PEM, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                  encryption_algorithm=serialization.NoEncryption()))
        logger.info(f"Приватный ключ успешно сохранен в {PRIVATE_PEM}")
    except Exception as e:
        logger.error(f"Ошибка при сериализации приватного ключа: {e}")
        raise

def deserialization_private_key():
    logger.debug(f"Десериализация приватного ключа из файла: {PRIVATE_PEM}")
    try:
        with open(PRIVATE_PEM, 'rb') as pem_in:
            private_bytes = pem_in.read()
        logger.info(f"Приватный ключ успешно загружен из {PRIVATE_PEM}")
        return load_pem_private_key(private_bytes, password=None)
    except Exception as e:
        logger.error(f"Ошибка при десериализации приватного ключа: {e}")
        raise

def save_bytes_to_file(data: bytes, file_path: str) -> None:
    logger.debug(f"Сохранение данных в файл: {file_path}")
    try:
        with open(file_path, 'wb') as f:
            f.write(data)
        logger.info(f"Данные успешно сохранены в {file_path} ({len(data)} байт)")
    except Exception as e:
        logger.error(f"Ошибка при сохранении данных в файл {file_path}: {e}")
        raise

def load_bytes_from_file(file_path: str) -> bytes:
    logger.debug(f"Загрузка данных из файла: {file_path}")
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        logger.info(f"Данные успешно загружены из {file_path} ({len(data)} байт)")
        return data
    except Exception as e:
        logger.error(f"Ошибка при загрузке данных из файла {file_path}: {e}")
        raise

import os


def check_file_not_empty(file_path: str) -> bool:
    logger.debug(f"Проверка файла: {file_path}")
    try:
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            logger.warning(f"Файл пустой: {file_path}")
            return False
        logger.debug(f"Файл проверен успешно: {file_path} ({file_size} байт)")
        return True

    except Exception as e:
        logger.error(f"Ошибка при проверке файла {file_path}: {e}")
        return False

def read_txt_file(file_path: str)->str:
    logger.debug(f"Чтение текстового файла: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        logger.info(f"Текстовый файл успешно прочитан: {file_path} ({len(content)} символов)")
        return content
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise


def write_file_txt(data: str, file_path: str)->None:
    logger.debug(f"Запись текста в файл: {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        logger.info(f"Текст успешно записан в файл: {file_path} ({len(data)} символов)")
    except Exception as e:
        logger.error(f"Ошибка при записи в файл {file_path}: {e}")
        raise
