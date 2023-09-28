def waterPlant():
    cap1 = int(input("\nEnter capacity of first watering can: "))
    cap2 = int(input("\nEnter capacity of second watering can: "))
    limit = min(cap1,cap2)
    print("\nNote that plant needs cannot exceed ",limit," units of water.")
    arr = []
    i = 0
    n = int(input("\nEnter number of plants: "))
    while i<n:
        need = int(input("\nEnter the amount of water the plant needs: "))
        if need>limit:
            print("\nPlease do not exceed the water limit.")
    
        else:
            arr.append(need)
            i = i+1
    mid = 0
    count = 2 #They refill each once at the beginning
    remwater1 = cap1
    remwater2 = cap2
    if n%2 == 0:
        sub1 = arr[:(n//2)]
        sub2 = arr[(n//2):]
        sub2 = sub2[::-1]
    else:
        sub1 = arr[:(n//2)]
        print(sub1)
        mid = n//2
        print(mid)
        sub2 = arr[(mid+1):]
        sub2 = sub2[::-1]
        print(sub2)
    for i in sub1:
        if i <= remwater1:
            remwater1 = remwater1 - i
        else:
            remwater1 = cap1 - i
            count = count + 1
    for i in sub2:
        if i <= remwater2:
            remwater2 = remwater2 - i
        else:
            remwater2 = cap2 - i
            count = count + 1
    if mid == 0:
        return count
    else:
        if arr[mid] > (remwater1 + remwater2):
            count = count + 1
            return count
        else:
            return count
#main environment
y = waterPlant()
print("Number of total refills: ",y)