# Given : palindrome number
# Output: true or False
# Check if an integer is palindrome or not
# Example: 121

'''
Create an empty array andd use a while loop to extract the last digit of the number and store it in the array
Reverse the array and check if they are equal
Return the output
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 0:
            temp = x
            rev_int_elements = []
            # Adding the digits to the List
            while temp > 0:
                # Extracting Last Digit
                digit = temp % 10
                # Adding it to the array
                rev_int_elements.append(digit)
                # Flooring the number
                temp = temp // 10
            # Reverses the array
            org_int_elements = rev_int_elements[::-1]
            # Checks if the reverse is equal to the original
            return rev_int_elements == org_int_elements
        #Return output
        elif x == 0:
            return True
        else:
            return False

print(Solution().isPalindrome(121))


#x= input
#temp=x
#rev_int_elements=[]
#digit = temp % 10

#Output= True


        