def index_order(n,k):
    index_order = []
    for i in range(k,n-k):
        index_order.append([k,i])
    for i in range(k+1,n-k):
        index_order.append([i,n-k-1])
    for i in range(n-1-(k+1),k,-1):
        index_order.append([n-k-1,i])
    for i in range(n-(k+1),k,-1):
        index_order.append([i,k])
    
    return index_order

def borderSort(matrix):
    n = len(matrix)
    for k in range(0,int(n/2)):
        io = index_order(n,k)
        temp_arr = [ matrix[ i[0] ][ i[1] ] for i in io]
        temp_arr = sorted(temp_arr)
        for tr in range(0,len(temp_arr)):
            matrix[ io[tr][0] ][ io[tr][1] ] = temp_arr[tr]
    
    return matrix

arr = [[16,15,14,13],
      [5,4,3,12],
      [6,1,2,11],
      [7,8,9,10]]

arr_sorted = borderSort(arr)
for line in arr_sorted:
    print(line)
