#Using Function
n = 64

binary = bin(n)
octal = oct(n)
hexademical = hex(n)

print(f"Binary is {binary} | octal : {octal} | hexademical is {hexademical}")

#  ============================================


def binaryFunc(num):
    binaryVal = ""
    while num > 0:
        binaryVal = str(num % 2) + binaryVal
        num //= 2
    binaryVal = "0b" + binaryVal if binaryVal else "0b0"
    print(f"Binary is {binaryVal}")

def ocatalFunc(num):
    ocatalVal = ""
    while num > 0:
        ocatalVal = str(num % 8) + ocatalVal
        num //= 8
    ocatalVal = "0o" + ocatalVal if ocatalVal else "0o0"
    print(f"Ocatal is {ocatalVal}")

def hexademicalFunc(num):
    hexademicalVal = ""
    while num > 0:
        hexRemainder = num % 16
        if hexRemainder < 10:
            hexademicalVal = str(hexRemainder) + hexademicalVal
        else:
            hexademicalVal = str(65 + hexRemainder - 10) + hexademicalVal
        num //= 16
    hexademicalVal = "0x" + hexademicalVal if hexademicalVal else "0x0"
    print(f"Hexademical is {hexademicalVal}")

binaryFunc(n)
ocatalFunc(n)
hexademicalFunc(n)
    