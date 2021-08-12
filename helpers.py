def generate_hash_key(var_name: str):
    ascii_value = 0

    for ch in var_name:
        ascii_value += ord(ch)

    return ascii_value % 53


def is_match_found(var_name: str, symbol_table: list):
    index = -1

    if len(symbol_table) < 0:
        return False, index

    for index, el in enumerate(symbol_table):
        if el.var_name == var_name:
            return True, index
    else:
        return False, index
