from collections import Counter
import math
import json
import sys,os

dir_path = os.path.dirname(os.path.realpath(__file__))
inventory_file_path = os.path.join(dir_path, "inventory.json")
offers_file_path = os.path.join(dir_path, "offers.json")

with open(inventory_file_path) as f:
    inventory = json.load(f)
print(inventory)
with open(offers_file_path) as f:
    offers = json.load(f)
#print(offers)

for offer in offers:
    print(offer)


def offer_calculation(good_price, count, offer_count, discount):
    """
    good_price = int \n
    count = int \n
    offer_count = int \n
    discount = int \n
    e.g. special offers: 3A for 130, 5A for 200, 2B for 45, 2E get one B free, 2F get one F free
    """
    remainder = (count % offer_count) * good_price
    special_cnt = (count - (count % offer_count)) / offer_count
    offer_value = (special_cnt*discount) + remainder

    return offer_value

def offer_handler(basket_skus):
    total_basket_value=0

    basket = Counter(basket_skus)
    print(basket)
    for item, cnt in basket.items():
        # Get price
        item_price = inventory.get(item, -1)
        # check if good is in inventory, else return -1 just in case
        if item_price==-1:
            return -1
        # check for any offers available
        item_offers = [c["offers"] for offer in offers if offer["product"]==item]

        print(item_offers)


    return total_basket_value


def checkout(skus):
    """
    skus = unicode string \n
    NOTE: fos skus to be a valid input it must be uppercase and included in the inventory \n
    inventory = {"A":50, "B":30, "C":20, "D":15, "E":40, "F":10} \n
    e.g. skus = "AABBCDE"
    """
    # If invalid input return -1
    # Check for correct naming or empty basket
    skus = skus.replace(" ", "")
    if not skus:
        return 0
    if not skus.isupper():
        return -1


    offer_handler(basket_skus=skus)
    total_basket_value=0
    # Count items in basket
    basket = Counter(skus)
    print(basket)
    for item, cnt in basket.items():
        # Get price
        item_price = inventory.get(item, -1)
        # check if good is in inventory, else return -1 just in case
        if item_price==-1:
            return -1
            
        ### Update total basket value
        # Special offers calculation
        # A offers
        if item == "A" and cnt>=3:
            # 5A for 200
            offer_mod = cnt%5
            # if remainder less than 3 use just 5A for 200
            if offer_mod < 3:
                special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=5, discount=200)
                total_basket_value+=special_offer_value
            # if remainder more than 3 use both  5A for 200 and 3A for 130
            elif offer_mod >= 3:
                # 5A for 200
                special_offer_value = offer_calculation(good_price=item_price, count=cnt-offer_mod, offer_count=5, discount=200)
                total_basket_value+=special_offer_value
                # 3A for 130
                special_offer_value = offer_calculation(good_price=item_price, count=offer_mod, offer_count=3, discount=130)
                total_basket_value+=special_offer_value

            # 3A for 130
            else:
                special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=3, discount=130)
                total_basket_value+=special_offer_value

        # 2B for 45
        elif item == "B" and cnt>=2:
            special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=2, discount=45)
            total_basket_value+=special_offer_value

        # 2E get one B free
        elif item == "E" and cnt>=2:
            # Add first total cost of E
            total_basket_value+=(inventory["E"]*cnt)
    
            # Check if B exists just to avoid ZeroDivision Errors
            if basket["B"]:
                # Free Bs
                free_bs = math.floor(cnt/2)
                count_b = basket["B"]
                price_b = inventory["B"]
                # Subtract initial B total cost and recalculate based on free_bs
                initial_cost_b = offer_calculation(good_price=price_b, count=count_b, offer_count=2, discount=45)
                total_basket_value-=initial_cost_b

                # If the number of free_bs is less than the number of existing Bs then recalculate with new number of Bs
                if free_bs<count_b:
                    new_b = count_b - free_bs
                    new_cost_b = offer_calculation(good_price=price_b, count=new_b, offer_count=2, discount=45)
                    total_basket_value+=new_cost_b

        # 2F get one F free
        elif item == "F" and cnt>=3:
            special_offer_value = offer_calculation(good_price=item_price, count=cnt+1, offer_count=2, discount=10)
            total_basket_value+=special_offer_value
        
        else:
            total_basket_value+=(item_price*cnt)

    return int(total_basket_value)
    
if __name__ == "__main__":
    print(checkout(skus="AAA"))

