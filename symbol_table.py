from helpers import generate_hash_key, has_match_found
from symbol_table_model import SymbolTable

symbol_table = []


# functionalities of symbol table
def insert(data: str):
    if ',' not in data:
        return "Sorry! You didn't enter comma separated value. \n"

    if data[0].isdigit():
        return "You cannot start a variable name with number \n"

    if len(symbol_table) > 54:
        return "Symbol table is full! \n"

    data_list = data.split(',')

    var_name = data_list[0].strip()
    data_type = data_list[1].strip()

    is_match_found = has_match_found(var_name=var_name, symbol_table=symbol_table)[0]

    if is_match_found:
        return "Name already exists! \n"

    hash_key = generate_hash_key(var_name)
    symbol_table.append(SymbolTable(hash_key=hash_key, var_name=var_name, data_type=data_type))
    return "Insert Successful! \n"


def update(var_name):
    is_match_found, index = has_match_found(var_name=var_name, symbol_table=symbol_table)

    if not is_match_found:
        return "Sorry! No Match. Name not found! \n"

    data_type = input("\n Enter new data type to update: ")

    symbol_table_data: SymbolTable = symbol_table[index]

    if symbol_table_data.data_type == data_type:
        return "You enter same data type. Nothing to update! \n"

    symbol_table_data.data_type = data_type
    symbol_table[index] = symbol_table_data
    return "Update Successful \n"


def delete(var_name):
    is_match_found, index = has_match_found(var_name=var_name, symbol_table=symbol_table)

    if not is_match_found:
        return "Sorry! No Match. Name not found! \n"

    del symbol_table[index]
    return "Delete successful! \n"


def search(var_name: str):
    is_match_found, index = has_match_found(var_name=var_name, symbol_table=symbol_table)

    if not is_match_found:
        return "Sorry! No Match. Name not found! \n"

    symbol_table_data: SymbolTable = symbol_table[index]
    return f"Match found. Hash key is -> {symbol_table_data.hash_key} and Data Type -> {symbol_table_data.data_type}"


def show():
    for el in symbol_table:
        _el: SymbolTable = el
        print(f"Hash key is: {_el.hash_key} --> Name: {_el.var_name}  --&&-- DataType: {_el.data_type}")
    print()
