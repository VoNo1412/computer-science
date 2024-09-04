def k_frequency(nums, k):    # Step 1: Count the frequencies
    hashCountNum = {}
    for num in nums:
        if num not in hashCountNum:
            hashCountNum[num] = 1
        else:
            hashCountNum[num] += 1
    
    # Step 2: Sort by frequency and pick top k elements
    sorted_items = sorted(hashCountNum.items(), key=lambda item: item[1], reverse=True)
        # Extract the keys of the top k elements
    top_k_elements = [item[0] for item in sorted_items[:k]]
        
    return top_k_elements
print(k_frequency([1,1,1,2,2,3], 2))
print(k_frequency([1], 1))
print(k_frequency([4,1,-1,2,-1,2,3], 2))
