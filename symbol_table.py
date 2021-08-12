from helpers import generate_hash_key, is_match_found


class SymbolTable:
    def __init__(self, hash_key, var_name, data_type):
        self.hash_key = hash_key
        self.var_name = var_name
        self.data_type = data_type


symbol_table = []


# functionalities of symbol table
def insert(data: str):
    if ',' in data:
        data_list = data.split(',')
        var_name = data_list[0].strip()
        data_type = data_list[1].strip()
        hash_key = generate_hash_key(var_name)

        symbol_table_obj = SymbolTable(hash_key, var_name, data_type)

        match_found, index = is_match_found(var_name=var_name, symbol_table=symbol_table)

        if match_found:
            return "Name already exists! \n"
        else:
            symbol_table.append(symbol_table_obj)
            return "Insert Successful! \n"

    return "Sorry! You didn't enter comma separated value. \n"


def update():
    pass


def delete():
    pass


def search():
    pass


def show():
    for el in symbol_table:
        print(f"Hash key is: {el.hash_key} --> Name: {el.var_name}  --&&-- DataType: {el.data_type} \n")
