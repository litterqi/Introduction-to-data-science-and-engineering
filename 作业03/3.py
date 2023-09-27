import re
def validate_id_number(id_number):
    pattern = r"^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$"
    return re.match(pattern, id_number) is not None
id_number = input("请输入身份证号：")
is_valid = validate_id_number(id_number)
print(is_valid)