from collections import Counter

inventory = {"A":50, "B":30, "C":20, "D":15}

def checkout(skus):
    """
    skus = unicode string \n
    special offers: 3A for 130, 2B for 45 
    """
    if not skus.isalpha():
        return -1
    else:
        basket = Counter(skus.upper())
        
    return basket


print(checkout("abcfev"))
    

