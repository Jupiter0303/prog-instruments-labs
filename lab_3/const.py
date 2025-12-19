VARIANT = 10
CSV_FILENAME  = "10.csv"
CSV_DELIMITER  = ";"

PATTERNS = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": r"^\d{3} [A-Z][a-z]+(?: [A-Z][a-z]+)*$",
    "snils": r"^\d{11}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "ip_v4": r"^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$",
    "longitude": r"^-?(?:180(?:\.0+)?|1[0-7]\d(?:\.\d+)?|\d?\d(?:\.\d+)?)$",
    "blood_type": r"^(A|B|AB|O)[+\u2212]$",
    "isbn": r"^(?:\d{3}-)?\d-\d{5}-\d{3}-\d$",
    "locale_code": r"^[a-z]{2,3}(?:-[a-z]{2})?$",
    "date": r"^20\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$"
}