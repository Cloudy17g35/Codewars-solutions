def sum_or_product(array, n):
    array = sorted(array, reverse=True)
    product = 1

    for element in array[-n:]:

        product *= element

    array_sum = sum(array[:n])

    if array_sum > product:
        return 'sum'
    elif array_sum < product:
        return 'product'
    else:
        return 'same'
