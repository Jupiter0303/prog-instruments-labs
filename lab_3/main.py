import csv
import re
from typing import List
from checksum import calculate_checksum, serialize_result
from const import VARIANT, CSV_FILENAME, CSV_DELIMITER, PATTERNS


def read_csv() -> List[dict]:
    try:
        with open(CSV_FILENAME, 'r', encoding="utf-16") as file:
            return list(csv.DictReader(file, delimiter=CSV_DELIMITER))
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        raise

def validate_row(row: dict) -> bool:
    try:
        for field, value in row.items():
            if field in PATTERNS and not re.fullmatch(PATTERNS[field], value.strip()):
                return False
        return True
    except Exception as e:
        print(f"Ошибка валидации строки: {e}")
        return False

def find_invalid_rows() -> List[int]:
    try:
        data = read_csv()
        return [i for i, row in enumerate(data) if not validate_row(row)]
    except Exception as e:
        print(f"Ошибка поиска невалидных строк: {e}")
        raise

def main() -> None:
    try:
        invalid_rows = find_invalid_rows()
        checksum = calculate_checksum(invalid_rows)
        serialize_result(VARIANT, checksum)
        print(f"Найдено невалидных строк: {len(invalid_rows)}")
        print(f"Контрольная сумма: {checksum}")
    except Exception as e:
        print(f"Ошибка в main: {e}")

if __name__ == "__main__":
    main()