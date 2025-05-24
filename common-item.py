def item_in_common(list1, list2):
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    
    return any(item in my_dict for item in list2)
    
    
    
    # return any(item1 == item2 for item1 in list1 for item2 in list2)
    
    
    # for item1 in list1:
    #     for item2 in list2:
    #         if item1 == item2:
    #             return True
    # return False
g