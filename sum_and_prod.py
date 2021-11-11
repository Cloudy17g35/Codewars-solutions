def sum_or_product(array, n):
    array = sorted(array, reverse=True)[:n]
    product = 1

    for element in array:
        product *= element

    return product, sum(array)
