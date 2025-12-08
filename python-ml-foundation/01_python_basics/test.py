

# Read the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the length of the string (we don't actually need this)
    n = int(input())
    
    # Read the string and remove any trailing whitespace
    s = input().strip()
    
    # Find the maximum character in the string (alphabetically largest)
    # For example: max("aab") returns 'b'
    max_char = max(s)
    
    # Calculate total operations needed
    # For each character, find how many steps to reach max_char
    # ord() converts a character to its ASCII value
    # ord('b') - ord('a') = 98 - 97 = 1 (means 'a' needs 1 step to become 'b')
    total_ops = sum(ord(max_char) - ord(char) for char in s)
    
    # Output the result for this test case
    print(total_ops)