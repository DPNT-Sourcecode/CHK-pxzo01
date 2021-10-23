from collections import Counter
import math
import json
import sys,os

dir_path = os.path.dirname(os.path.realpath(__file__))
inventory_file_path = os.path.join(dir_path, "inventory.json")
offers_file_path = os.path.join(dir_path, "offers.json")

with open(inventory_file_path) as f:
    inventory = json.load(f)

with open(offers_file_path) as f:
    offers = json.load(f)

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
    """
    OFFER HANDLER \n
    basket_skus = unicode string \n
    """
    total_basket_value=0

    basket = Counter(basket_skus)
    for item, cnt in basket.items():
        # Get price
        item_price = inventory.get(item, -1)
        # check if good is in inventory, else return -1 just in case
        if item_price==-1:
            return -1
        # check for any offers available
        item_offers = [c["offers"] for c in offers if c["product"]==item]
        
        if item_offers:
            offer_type = [c["type"] for c in offers if c["product"]==item][0]
            offer_quantities = [q["quantity"] for q in item_offers[0]]
            offer_prices = [q["price"] for q in item_offers[0]]

            max_qt = max(offer_quantities)
            min_qt = min(offer_quantities)
            max_price = max(offer_prices)
            min_price = min(offer_prices)

            if offer_type=="discount":
                if len(item_offers[0])>1:
                    # Check remainder for multiple offers
                    offer_qts = cnt%max_qt
                    # if remainder less than min quantity use just Big offer
                    if offer_qts < min_qt:
                        special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=max_qt, discount=max_price)
                        total_basket_value+=special_offer_value
                    # if remainder more than min quntity use both  Big and Small offers
                    elif offer_qts >= min_qt:
                        # Big offer
                        special_offer_value = offer_calculation(good_price=item_price, count=cnt-offer_qts, offer_count=max_qt, discount=max_price)
                        total_basket_value+=special_offer_value
                        # Small Offer
                        special_offer_value = offer_calculation(good_price=item_price, count=offer_qts, offer_count=min_qt, discount=min_price)
                        total_basket_value+=special_offer_value
                    # Only small offer
                    else:
                        special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=min_qt, discount=min_price)
                        total_basket_value+=special_offer_value
                else:
                    special_offer_value = offer_calculation(good_price=item_price, count=cnt, offer_count=min_qt, discount=min_price)
                    total_basket_value+=special_offer_value

            elif offer_type=="free":
                free_item = min_price
                if item!=free_item:
                    # Add first total cost of Product
                    total_basket_value+=(inventory[item]*cnt)
                    # Check if B exists just to avoid ZeroDivision Errors
                    if basket[free_item]:
                        # Free Bs
                        free_bs = math.floor(cnt/2)
                        count_b = basket[free_item]
                        price_b = inventory[free_item]
                        # Find offer for free item
                        free_item_offers = [c["offers"] for c in offers if c["product"]==free_item]
                        if free_item_offers:
                            for offer in free_item_offers[0]:
                                print("Free Item offers: " , offer)
                                # Subtract initial B total cost and recalculate based on free_bs
                                initial_cost_b = offer_calculation(good_price=price_b, count=count_b, offer_count=offer["quantity"], discount=offer["price"])
                                total_basket_value-=initial_cost_b

                            # If the number of free_bs is less than the number of existing Bs then recalculate with new number of Bs
                            if free_bs<count_b:
                                new_b = count_b - free_bs
                                new_cost_b = offer_calculation(good_price=price_b, count=new_b, offer_count=offer["quantity"], discount=offer["price"])
                                total_basket_value+=new_cost_b
                else:
                    special_offer_value = offer_calculation(good_price=item_price, count=cnt+1, offer_count=min_qt, discount=inventory.get(item))
                    total_basket_value+=special_offer_value
        else:
            total_basket_value+=(item_price*cnt)

    return int(total_basket_value)


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

    total_basket_value=offer_handler(basket_skus=skus)
    
    return total_basket_value
    
    
if __name__ == "__main__":
    print(checkout(skus="AAABBCCCBEEFF"))



