'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # loop over arr
    # hold onto current index value
    # if nothing else in the arr matches that value, return it
    # otherwise remove the current index value & its match and loop again
    # get rid of both the current index value and its match to make the arr shorter so each iteration takes less time

    curr_index = len(arr) - 1
    while curr_index > 0:
        
        next_index = curr_index - 1

        while next_index >= 0:
            
            # if curr_index and next_index values match, remove both and update the indices
            if arr[next_index] == arr[curr_index]:
                arr.pop(curr_index)
                arr.pop(next_index)

                curr_index = len(arr) - 1
                next_index = curr_index - 1

            # if we reached the end of the array and never found a match, curr_index is what we want
            elif next_index - 1 == 0:
                return arr[curr_index]

            # if they didn't match, update next_index to move onto the next element
            else: 
                next_index -= 1
        
    return arr[0]
            


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")