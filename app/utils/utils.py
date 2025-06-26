import re

def validate_cpf_cnpj(cpf_cnpj: str) -> bool:
    numeric_cpf_cnpj = re.sub(r'[^0-9]', '', cpf_cnpj)

    if len(numeric_cpf_cnpj) == 11:
        return _validate_cpf(numeric_cpf_cnpj)
    elif len(numeric_cpf_cnpj) == 14:
        return _validate_cnpj(numeric_cpf_cnpj)
    else:
        return False

def _validate_cpf(cpf: str) -> bool:
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    
    numbers = [int(digit) for digit in cpf]
    
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False
    
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False
    
    return True

def _validate_cnpj(cnpj: str) -> bool:
    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False
    
    numbers = [int(digit) for digit in cnpj]
    
    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_of_products = sum(a*b for a, b in zip(numbers[0:12], weights))
    expected_digit = 0 if (11 - (sum_of_products % 11)) > 9 else (11 - (sum_of_products % 11))
    if numbers[12] != expected_digit:
        return False
    
    weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_of_products = sum(a*b for a, b in zip(numbers[0:13], weights))
    expected_digit = 0 if (11 - (sum_of_products % 11)) > 9 else (11 - (sum_of_products % 11))
    if numbers[13] != expected_digit:
        return False
    
    return True

def validate_farm_area(total_area: float, agricultural_area: float, vegetation_area: float) -> bool:
    return (agricultural_area + vegetation_area) <= total_area