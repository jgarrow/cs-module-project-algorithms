'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    product_arr = []
    curr_index = 0

    while curr_index < len(arr):
        # reset curr_product after every full iteration through the array
        curr_product = 0

        for i in range(len(arr)):
            # if i is not our curr_index, we want to multiply it
            if i is not curr_index:
                # if this is the first index that's different from curr_index, set curr_product to this element
                if curr_product == 0:
                    curr_product = arr[i]

                # otherwise multiply curr_product by this element
                else: 
                    curr_product *= arr[i]
        
        # after we're done multiplying for this iteration, append the product to our product_arr
        product_arr.append(curr_product)

        # then increment curr_index        
        curr_index += 1
    
    return product_arr



    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
