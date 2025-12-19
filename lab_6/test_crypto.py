import pytest
from unittest.mock import Mock, patch
import tempfile
import os

from symmetric import Symmetric
from asymmetric import Asymmetric
from fileOrganization import save_bytes_to_file, load_bytes_from_file

# Тест 1: Проверка уникальности ключей
def test_key_uniqueness():
    key1 = Symmetric.generate_key()
    key2 = Symmetric.generate_key()
    assert key1 != key2
    assert len({key1, key2}) == 2

# Тест 2: Разные результаты при повторном шифровании
def test_encryption_produces_different_output():
    text = "Same message"
    key = Symmetric.generate_key()

    result1 = Symmetric.encrypt(text, key)
    result2 = Symmetric.encrypt(text, key)

    assert result1 != result2
    assert len(result1) == len(result2)

# Тест 3: RSA работает с разными данными
def test_rsa_encryption_with_different_inputs():
    private, public = Asymmetric.generate_keys()

    inputs = [b"a", b"ab", b"abc", b"abcd", b"abcde"]
    for data in inputs:
        encrypted = Asymmetric.encrypt_bytes(data, public)
        decrypted = Asymmetric.decrypt(encrypted, private)
        assert decrypted == data

    assert len({Asymmetric.encrypt_bytes(data, public) for data in inputs}) == len(inputs)

# Тест 4: Файлы сохраняются корректно
def test_file_operations_with_random_data():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        path = f.name

    random_data = os.urandom(256)
    save_bytes_to_file(random_data, path)

    with open(path, 'rb') as f:
        file_content = f.read()

    loaded = load_bytes_from_file(path)

    assert loaded == random_data
    assert loaded == file_content
    assert len(loaded) == 256

    os.unlink(path)

# Тест 5: Работа с пустыми строками
def test_empty_and_whitespace_strings():
    key = Symmetric.generate_key()

    cases = ["", " ", "  ", "\t", "\n", "\r\n", "\t\n\r"]
    for text in cases:
        encrypted = Symmetric.encrypt(text, key)
        decrypted = Symmetric.decrypt(encrypted, key)
        assert decrypted.decode() == text

# Тест 6: Параметризованный тест длин - проверка граничных случаев
@pytest.mark.parametrize("text,description", [
    ("A", "single_char"),                      # Минимальная длина
    ("AB", "two_chars"),                       # Нечетная длина
    ("ABCD", "four_chars"),                    # Кратна 2, но не 8
    ("ABCDEFGH", "eight_chars"),               # Половина блока шифрования
    ("ABCDEFGHIJKLMNOP", "sixteen_chars"),     # Ровно один блок (16 символов = ~16 байт)
])
def test_encryption_with_different_lengths(text, description):
    key = Symmetric.generate_key()
    encrypted = Symmetric.encrypt(text, key)
    decrypted = Symmetric.decrypt(encrypted, key)

    # Проверяем, что данные не теряются
    assert decrypted.decode() == text
    # Проверяем, что шифрование добавляет данные (IV + padding)
    assert len(encrypted) >= len(text)

# Тест 7: Mock для логгера - проверка побочных эффектов
def test_logging_behavior_with_mock():
    """
        Проверяем, что функция шифрования корректно логирует свои действия.
        Используется mock для изоляции теста от файловой системы.
    """
    # используем фейковый логгер, имитирующий реальный
    mock_logger = Mock()
    mock_logger.info = Mock()
    mock_logger.debug = Mock()

    with patch('symmetric.logger', mock_logger):
        key = b'\x00' * 16
        result = Symmetric.encrypt("test", key)

        assert mock_logger.info.call_count >= 1
        assert mock_logger.debug.call_count >= 1

        info_calls = [str(call) for call in mock_logger.info.call_args_list]
        assert any("зашифрован" in call.lower() for call in info_calls)
