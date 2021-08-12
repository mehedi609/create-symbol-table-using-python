from symbol_table_model import SymbolTable


def generate_hash_key(var_name: str):
    ascii_value = 0

    for ch in var_name:
        ascii_value += ord(ch)

    return ascii_value % 53


def has_match_found(var_name: str, symbol_table: list):
    index = -1

    if len(symbol_table) < 0:
        return False, index

    for index, el in enumerate(symbol_table):
        data: SymbolTable = el
        if data.var_name == var_name:
            return True, index

    return False, index
