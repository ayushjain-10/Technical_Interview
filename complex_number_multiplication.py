# Given : two complex numbers
# Output: string of the complex number that represents their multiplications

'''
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
'''

'''
First, we need to parse our numbers, just find symbol + inside. For this we can use python functionality with function .index: we can be sure that this index exists. Then we create real and imaginary parts for both of numbers, using found indexes.
Finally we use definition of complex numbers multiplication and return answer.
'''

class Solution:
    def complexNumberMultiply(self, a, b):
        # .index function helps us parse the real and imaginary numbers
        ind1 = a.index("+")
        ind2 = b.index("+")
        # creating two parts for both numbers
        x1, y1 = int(a[:ind1]), int(a[ind1+1:-1])
        x2, y2 = int(b[:ind2]), int(b[ind2+1:-1])
        # multiply and add the strings to return output
        return str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"
    
#a= 2+ -3i
#b= 1+ -4i
#ind1 = 1
#ind2 = 1
# x1= 2
# x2= 1
# y1= 3i
# y2= 4i

#Output= "-10+ -11i"
