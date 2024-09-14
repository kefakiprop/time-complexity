# Function to calculate sum using a loop
def fun2(n):
    sum = 0  # Initialize the sum to 0
    # Loop from 1 to n
    for i in range(1, n+1):
        sum += i  # Add each i to sum
    return sum  # Return the final sum

# Example: Calculating the sum for n=4
print(f"Fun2 result for n=4: {fun2(4)}")
