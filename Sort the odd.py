def sort_array(source_array):
    
    dict_with_evens = {}
    dict_with_odds = {}
    
    for i in range(len(source_array)):
        
        number = source_array[i]
        
        if number % 2 and number != 0:
            dict_with_odds[i] = number
            
        else:
            dict_with_evens[i] = number
            
    dict_with_odds = dict(zip(sorted(dict_with_odds.keys()), 
                              sorted(dict_with_odds.values())))
    
    
    
    dict_for_all = {**dict_with_odds, **dict_with_evens}
    
    return [dict_for_all[i] for i in range(len(source_array))]
