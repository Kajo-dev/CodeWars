def delete_nth(order,max_e):
    wynik=[]
    kopia=order.copy()
    order=order[::-1]
    for o in kopia:
        ile=order.count(o)
        if ile>max_e:
            for i in range(ile-max_e):
                order.remove(o)
    order=order[::-1]   
    return order

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))


#([20,37,20,21], 1), [20,37,21])

#[37, 21, 20] should equal [20, 37, 21]