'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     max_arr = []
#     curr_index = 0

#     # loop over nums
#     # for each num_index, make a new array that slices nums[num_index, k]
#     # then loop over sliced nums for max total

#     while curr_index < len(nums):
#         # initialize to None to handle potential negative integers
#         curr_slice_max = None

#         # current window slice
#         curr_arr_slice = []

#         # the last array must start at k indices from the end
#         if curr_index <= len(nums) - k:
#             curr_arr_slice = nums[curr_index:curr_index + k]
        
#             # get largest all nums in our current window slice
#             for num in curr_arr_slice:
#                 if curr_slice_max is None:
#                     curr_slice_max = num
#                 elif num > curr_slice_max:
#                     curr_slice_max = num
            
#             max_arr.append(curr_slice_max)
        
#         curr_index += 1
    
#     return max_arr
        

# get window
def get_window(i, arr, k):
    return arr[i : i + k]

def get_window_max(arr):
    return max(arr)

# calculate max of first window
# for second window, if last element is greater than the last element of first window, calculate max of second window
# otherwise, skip second window

def sliding_window_max(nums, k):
    num_possible_windows = (len(nums) - k + 1)
    max_arr = [None] * num_possible_windows
    
    prev_window = get_window(0, nums, k)
    prev_window_max_val = get_window_max(prev_window)
    max_arr[0] = prev_window_max_val
    curr_index = 1

    while curr_index < num_possible_windows:
        curr_window = get_window(curr_index, nums, k)

        # if the new curr_window's last element is greater than the previous window's max,
        # then the curr_window's last element is our max
        if curr_window[-1] >= prev_window_max_val:
            max_arr[curr_index] = curr_window[-1]
            prev_window_max_val = curr_window[-1]

        # otherwise if the last element of the prev window is the same value as the prev window's max,
        # our curr_window max is somewhere in the middle
        elif nums[curr_index - 1] == prev_window_max_val:
            curr_window_max = get_window_max(curr_window)
            max_arr[curr_index] = curr_window_max
            prev_window_max_val = curr_window_max

        # if the last element isn't our new max and the last element of the previous window wasn't the max of the previous window, then our new max is somewhere inside of our new window
        else:
            max_arr[curr_index] = prev_window_max_val
        

        curr_index += 1
    
    return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
