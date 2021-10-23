from collections import Counter

inventory = {"A":50, "B":30, "C":20, "D":15}

def checkout(skus):
    """
    skus = unicode string \n
    special offers: 3A for 130, 2B for 45
    """
    # If invalid input return -1
    # Check for correct naming
    if not skus.isupper():
        return -1

    total_basket_value=0
    # Count items in basket
    basket = Counter(skus)

    for item, cnt in basket.items():
        # Get price
        item_price = inventory.get(item, -1)
        # check if good is in inventory, else return -1
        if item_price==-1:
            return -1
            
        ### Update total basket value
        # add special offers calculation
        if item == "A" and cnt>=3:
            remainder = (cnt % 3) * item_price
            special_cnt = (cnt - (cnt % 3)) / 3

            special_offer_value = (special_cnt*130) + remainder
            total_basket_value+=special_offer_value

        elif item == "B" and cnt>=2:
            remainder = (cnt % 2) * item_price
            special_cnt = (cnt - (cnt % 2)) / 2

            special_offer_value = (special_cnt*45) + remainder
            total_basket_value+=special_offer_value

        else:
            total_basket_value+=(item_price*cnt)

    return int(total_basket_value)
    

