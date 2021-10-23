from collections import Counter

inventory = {"A":50, "B":30, "C":20, "D":15, "E":40}

def offer_calculation(good_price, count, offer_count, discount):
    """
    good_price = int \n
    count = int \n
    offer_count = int \n
    discount = int \n
    special offers: 3A for 130, 5A for 200, 2B for 45, 2E get one B free
    """
    remainder = (count % offer_count) * good_price
    special_cnt = (count - (count % offer_count)) / offer_count
    offer_value = (special_cnt*discount) + remainder

    return offer_value

def checkout(skus):
    """
    skus = unicode string \n
    NOTE: fos skus to be a valid input it must be uppercase and included in the inventory \n
    inventory = {"A":50, "B":30, "C":20, "D":15, "E":40} \n
    e.g. skus = "AABBCDE"
    """
    # If invalid input return -1
    # Check for correct naming or empty basket
    if not skus:
        return 0
    if not skus.isupper():
        return -1

    total_basket_value=0
    # Count items in basket
    basket = Counter(skus)

    for item, cnt in basket.items():
        # Get price
        item_price = inventory.get(item, -1)
        # check if good is in inventory, else return -1 just in case
        if item_price==-1:
            return -1
            
        ### Update total basket value

        # Special offers calculation
        if item == "A" and cnt>=3:
            # 5A for 200
            if cnt>=5:
                remainder = (cnt % 5) * item_price
                special_cnt = (cnt - (cnt % 5)) / 5

                special_offer_value = (special_cnt*200) + remainder
                total_basket_value+=special_offer_value
            # 3A for 130
            else:
                # remainder = (cnt % 3) * item_price
                # special_cnt = (cnt - (cnt % 3)) / 3

                # special_offer_value = (special_cnt*130) + remainder
                # total_basket_value+=special_offer_value

                special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=3, discount=130)
                total_basket_value+=special_offer_value

        # 2B for 45
        elif item == "B" and cnt>=2:
            remainder = (cnt % 2) * item_price
            special_cnt = (cnt - (cnt % 2)) / 2

            special_offer_value = (special_cnt*45) + remainder
            total_basket_value+=special_offer_value

        # 2E get one B free
        elif item == "E" and cnt>=2:
            remainder = (cnt % 2) * item_price
            special_cnt = (cnt - (cnt % 2)) / 2

            special_offer_value = (special_cnt*-30) + remainder
            total_basket_value+=special_offer_value

        else:
            total_basket_value+=(item_price*cnt)

    return int(total_basket_value)
    

print(checkout(""))

