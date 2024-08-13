def binary_to_decimal(binaryStr):
    decimalValue = 0
    binaryStr = binaryStr[::-1]  # Reverse the binary string
    for i in range(len(binaryStr)):
        decimalValue += int(binaryStr[i]) * (2 ** i)
    return decimalValue

def decimal_to_binary(decimalNumber):
    if decimalNumber == 0:
        return "0"
    
    binaryStr = ""
    while decimalNumber > 0:
        binaryStr = str(decimalNumber % 2) + binaryStr
        decimalNumber = decimalNumber // 2
    
    return binaryStr

# Example usage:
binaryNumber = input("Give me a binary number:\n> ")
decimalResult = binary_to_decimal(binaryNumber)
print(f"Binary {binaryNumber} to Decimal is {decimalResult}")

decimalNumber = int(input("Give me a decimal number:\n> "))
binaryResult = decimal_to_binary(decimalNumber)
print(f"Decimal {decimalNumber} to Binary is {binaryResult}")
