class SymbolTable:
    def __init__(self, hash_key, var_name, data_type):
        self.hash_key = hash_key
        self.var_name = var_name
        self.data_type = data_type