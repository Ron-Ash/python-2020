def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
  
# Driver Code 
if __name__ == '__main__': 
      
      
    # Calling function 
    for i in range(14):
        DecimalToBinary(int(input("convert to binary:")))
        print('\n')

def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)    
      
  
# # Driver code 
# if __name__ == '__main__': 
#     binaryToDecimal(int(input("convert to binary:")))