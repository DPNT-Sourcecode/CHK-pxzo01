from collections import Counter

inventory = {"A":50, "B":30, "C":20, "D":15}

def checkout(skus):
    """
    skus = unicode string \n
    special offers: 3A for 130, 2B for 45 
    """

    total_basket_value=0
    basket = Counter(skus.upper())


    for item, cnt in basket.items():
        item_price = inventory.get(item, -1)
        print(item, ":", cnt)
        total_basket_value+=item_price
        

    return total_basket_value


print(checkout("abcfev"))
    



