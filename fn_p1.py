'''
we have 5 mem in team nreed to split resturant bill of 2586
'''

def split_bill(total_amount,total_mem):
    if total_mem > 1:
        split_amount=total_amount/total_mem
        return split_amount
    else:
        return total_amount

t_mem=1
t_amount=5789
each_persorn_pay=split_bill(t_amount,t_mem)
print("each person need to pay:",each_persorn_pay)


print("**************************************")

'''
purchase val greater than 500 10% discont applicable
'''
def discount_cal(pur_val,discount):
    if pur_val >= 500:
        per_cal=(discount/100) * pur_val
        return per_cal
    
    
cart_val=500
dis=15
dis_amount=discount_cal(cart_val,dis)
final_amount=cart_val-dis_amount
if cart_val >=500 :
    print("your purchase val is greater than 500, you are applicable for disount")
    print("your cart value is",cart_val)
    print("after discouted amount to pay:",final_amount)
else:
    print("your purchase val is less than 500, you are not applicable for disount")
    print("your cart value is",cart_val)


print("**************************************")




    

