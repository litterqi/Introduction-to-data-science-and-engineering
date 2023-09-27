def decimal_to_binary(decimal):
    binary = ""
    # 将小数部分拆分成整数和小数两部分
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    # 将整数部分转换为二进制
    while integer_part > 0:
        binary = str(integer_part % 2) + binary
        integer_part //= 2
    # 添加小数点
    binary += "."
    # 将小数部分转换为二进制
    while fractional_part > 0:
        if len(binary) > 32:  # 控制小数部分位数
            break
        fractional_part *= 2
        bit = int(fractional_part)
        binary += str(bit)
        fractional_part -= bit
    return binary
decimal_number = float(input("请输入一个数："))
binary_number = decimal_to_binary(decimal_number)
print("Decimal:", decimal_number)
print("Binary:", binary_number)