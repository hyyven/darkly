TO_CONVERT: str = "users"

def convert_to_char(string: str) -> str:
    chars: list[str] = [str(ord(c)) for c in string]
    return f"char({','.join(chars)})"

def convert_to_hex(string: str) -> str:
    chars: list[str] = [ord(c) for c in string]
    hex_str: str = ""
    for char in chars:
        hex_str += format(char, "x")
    return f"0x{hex_str}"

if __name__ == "__main__":
    print(convert_to_char(TO_CONVERT))
    print(convert_to_hex(TO_CONVERT))