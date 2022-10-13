import time

def tiempo_ejecucion(my_function, my_list):
    start_time = time.time()
    my_function(my_list)
    end_time = time.time()
    total_time = end_time - start_time
    
    return total_time
    
def buble_sort(data):
    for i in range(len(data)-1):
        check_sort = True
        for j in range((len(data)-1)-i):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
                check_sort = False
        if(check_sort):
            break
    return data       


def insertion_sort(data):    
    for i in range(1,len(data)):
        j = i
        temp = data[i]
        while (j>0 and data[j-1]>temp):
            data[j]=data[j-1]
            j-=1
        data[j] = temp
    return data 

def selection_sort(data):    
    for i in range(0,len(data)):
        minor = i
        for j in range(i+1,len(data)):
            if data[j]<data[minor]:
                minor = j
        data[i],data[minor]=data[minor],data[i]
    return data 

def quick_sort_new(data):
    
    if len(data)<=1:
        return data
    else:
        menores,mayores = divide_data(data,data[0])
        return quick_sort_new(menores) + [data[0]] + quick_sort_new(mayores)
      
        
def divide_data(data,n):    
    menores = []
    mayores = []
    for i in data:
        if i<n:
            menores.append(i)
        elif i>n:
            mayores.append(i)
    return menores,mayores
            
def create_partition(data, start,end):
    refer = start
    pivot_data = data[end-1]
    for i in range (start,end):
        if(data[i]<pivot_data):
            data[i], data[refer]= data[refer], data[i]
            refer+=1    
    data[end-1],data[refer]=data[refer],data[end-1]
    return refer

def quick_sort(data):
    def qs(data, start, end):        
        
        if(start<end):
            refer = create_partition(data, start,end)
            qs(data,start,refer)
            qs(data,refer+1,end)
        return data
    qs(data, 0, len(data))
    return data
            
def merge_sort(data):
    return divide_data_merge(data,0,len(data)-1)
    
def divide_data_merge(data,start,end):
    if(start<end):
        mid = (start + end)//2
        divide_data_merge(data,start,mid)
        divide_data_merge(data,mid+1,end)
        join_data(data,start,mid,end)        
    return data
def join_data(data,start,mid,end):  
    rejoin = []
    i = start
    j = mid + 1
    while i<=mid and j<=end:
        if data[i]<data[j]:            
            rejoin.append(data[i])
            i += 1
        else:            
            rejoin.append(data[j])
            j += 1
        
    while(i<=mid):        
        rejoin.append(data[i])
        i += 1
        
        
    while(j<=end):        
        rejoin.append(data[j])
        j += 1    
    #llevar los datos de rejoin al parámetro de entrada: data  
    k = 0
    for i in range(start, end+1):
        data[i] = rejoin[k]
        k+=1
    
def create_heap(data,end):  
    for i in range(end//2,-1,-1):
        validate_heap(data,i,end)

def validate_heap(data,i,end):
    left = 2 * i + 1
    right = left + 1    
    maximum = i
    
    if left<=end and data[left] > data[maximum]:
        maximum = left
    if right<=end and data[right] > data[maximum]:
        maximum = right
        
    if maximum != i:
        data[maximum],data[i] = data[i],data[maximum]
        validate_heap(data,maximum,end)
def heap_sort(data):    
    def heap_sort_i(data,end):        
        create_heap(data,end)
        while(end > 0):
            data[0],data[end] = data[end],data[0]
            end -= 1
            validate_heap(data,0,end)
    heap_sort_i(data, len(data)-1)
    


def counting_sort(data):
    total = [0] * len(data)
    counting = [0] * (max(data) + 1) #creacion de array
    
    for i in data:
        counting[i] += 1
   
    for i in range(1,len(counting)):
        counting[i] += counting[i-1]
    
    #for i in range(len(data)-1,-1,-1):
    for i in range(len(data)):
        total[counting[data[i]]-1] = data[i]
        counting[data[i]] -= 1
        
    for i in range(len(data)):
        data[i] = total[i]