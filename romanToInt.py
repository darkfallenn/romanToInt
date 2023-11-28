# This function converts any valid roman numeral to its corresponding numerical value.
# We can achieve this by knowing that: any smaller roman before a larger roman is considered substraction.
# Any smaller roman after a larger roman is considered addition.

def romanToInt(roman):
    m = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000} # Maps each numeral stage (I is first stage, V is second, etc.)
    ans = 0

    for i in range(len(roman)): # Iterate over each character in the roman
        if i < len(roman)-1 and m[roman[i]] < m[roman[i+1]]: # If there is still an element ahead of the current, and the current is less than that element...
            ans += m[roman[i]] # Then add it to the answer
        else:
            ans -= m[roman[i]] # Otherwise subtract it
    return ans 

# Time Complexity: O(n) 
# (If you don't know what time complexity is, don't worry!)