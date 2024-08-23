def findRestaurant(l1, l2):
    hashMap = {v: i for i, v in enumerate(l1)}

    index_min = float('inf')
    result = []

    for i, v in enumerate(l2):
        if v in hashMap:
            idx_sum = i + hashMap[v]
            if idx_sum < index_min:
                index_min = idx_sum
                result = [v]
            elif idx_sum == index_min:
                result.append(v)
    print(result)
    return result

findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
findRestaurant(["happy","sad","good"], ["sad","happy","good"])
findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"]
, ["KFC","Shogun","Burger King"])

