def is_age_diverse(lst):
    
    set_with_ages = set()
    
    for person in lst:
        age = person['age']
        if age >= 100:
            set_with_ages.add(10)
        else:
            set_with_ages.add(age // 10)
        
    return sorted(set_with_ages & set(range(1, 11))) == list(range(1, 11))
