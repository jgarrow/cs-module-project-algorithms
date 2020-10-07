'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n):

    # total = 0

    # check if n - 3 > 0
        # total += eating_cookeis(n - 3)

    # check if n - 2 > 0
        # total += eating_cookeis(n - 2)

    # check if n - 1 > 0
        # total += eating_cookeis(n - 1)


    # if n == 1,2,3
        # add 1 to total
    
    total = 0
    
    if n == 0:
        return 1

    if n - 3 > 0:
        total += eating_cookies(n - 3)
    
    if n - 2 > 0:
        total += eating_cookies(n - 2)
    
    if n - 1 > 0:
        total += eating_cookies(n - 1)
    
    if n == 1 or n == 2 or n == 3:
        total += 1

    return total


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
