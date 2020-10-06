'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_arr = []
    curr_index = 0

    # loop over nums
    # for each num_index, make a new array that slices nums[num_index, k]
    # then loop over sliced nums for max total

    while curr_index < len(nums):
        # initialize to None to handle potential negative integers
        curr_slice_max = None

        # current window slice
        curr_arr_slice = []

        # the last array must start at k indices from the end
        if curr_index <= len(nums) - k:
            curr_arr_slice = nums[curr_index:curr_index + k]
        
            # get largest all nums in our current window slice
            for num in curr_arr_slice:
                if curr_slice_max is None:
                    curr_slice_max = num
                elif num > curr_slice_max:
                    curr_slice_max = num
            
            max_arr.append(curr_slice_max)
        
        curr_index += 1
    
    return max_arr
        


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
