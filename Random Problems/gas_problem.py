def can_trav(gas,cost,start):
    ile_s = len(gas)
    ile_gas = 0
    start_stac = start
    started = False

    while start_stac != start or not started:
        started = True
        ile_gas += gas[start_stac] - cost[start_stac]
        if ile_gas < 0:
            return False
        start_stac = (start_stac+1)%ile_s

    return True

def gas_station(gas, cost):
    for i in range(len(gas)):
        if can_trav(gas, cost, i):
            return i 
    return -1


print(gas_station([1,5,3,3,5,3,1,3,4,5],[5,2,2,8,2,4,2,5,1,2]))