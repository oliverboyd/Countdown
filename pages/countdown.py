store_array=[]
results_array=[]

def countdown(total, array):
    global A
    A=0
    store_array.clear()
    results_array.clear()
    countdown_inner(total,array)
    if A == 0:
        return "Impossible"
    elif A == 1:
        return "Trivial"
    elif A == 2:
        return(results_array)
    
def countdown_inner(total,array):
    global A
    L = len(array)
    oparray = ['+','-','*','/']
    if L == 1:
        if total == array[0]:
            A=1
    elif L > 1:
        for i in range(0,L-1):
            for j in range(i+1,L):
                for k in range(0,4):
                    x = operation(array[i],array[j],oparray[k])
                    if x == -1:
                        continue
                    else:
                        store_array.append([array[i], array[j], oparray[k],x])
                        if x == total:
                            A=2
                            results_array.append(store_array.copy())
                        else:
                            array2 = array.copy()
                            array2.pop(j)
                            array2.pop(i)
                            array2.append(x)
                            countdown_inner(total,array2)
                        store_array.pop()

def operation(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        if a > b:
            return a-b
        else:
            return b-a
    elif op == '*':
        return a*b
    elif op=='/':
        if b==0  or a==0:
            return 0
        elif a % b == 0:
            return int(a/b)
        elif b % a == 0:
            return int(b/a)
        else:
            return -1

def generated_set(array):
    # returns all generated numbers
    array2=[]
    L=len(array)
    for i in range(0,L):
        array2.append(array[i][3])
    return array2

def subset_used(array):
    # returns the subset of the original numbers used
    array2=[]
    L=len(array)
    for i in range(0,L):
        array2.append(array[i][0])
        array2.append(array[i][1])
    for i in range(0,L-1):
        if array[i][3] in array2:
            array2.remove(array[i][3])
    return array2

def op_type(op):
    if op == "+" or op == "-":
        return "A"
    elif op == "*" or op ==  "/":
        return "M"

def tree(array):
    L=len(array)
    x = array[L-1][0] 
    y = array[L-1][1] 
    opt = op_type(array[L-1][2]) 
    N = array[L-1][3] 
    tree1 = [opt,N,[]] 
    S = subset_used(array) 
    T = generated_set(array)
    tracker = []
    ta = tree_alg(x,L-1,array,S,T,tracker,opt,tree1)
    tree1 = ta[0]
    S = ta[1]
    tracker = ta[2]
    ta = tree_alg(y,L-1,array,S,T,tracker,opt,tree1)
    tree1 = ta[0]
    tracker = ta[2]
    if len(tracker) != L-1:
        return ["redundant", tree1]
    else:
        return tree1

def tree_inner(K,array,S,T,tracker):
    N = array[K][3]
    x = array[K][0]
    y = array[K][1]
    opt = op_type(array[K][2])
    tree1 = [opt, N, []]
    ta = tree_alg(x,K,array,S,T,tracker,opt,tree1)
    tree1 = ta[0]
    S = ta[1]
    tracker = ta[2]
    ta = tree_alg(y,K,array,S,T,tracker,opt,tree1)
    tree1 = ta[0]
    return tree1

def tree_alg(x,K,array,S,T,tracker,opt,tree1):
    K2=-1
    for i in range(0,K):
        if x == T[K-1-i] and K-1-i not in tracker:
            K2 = K-1-i
            tracker.append(K2)
            break
    if K2 == -1:
        for i in range(0,len(S)):
            if x == S[i]:
                S.pop(i)
                break
        tree1[2].append(x)
    else:
        if op_type(array[K2][2]) != opt:
            tree1[2].append(tree_inner(K2,array,S,T,tracker))
        else:
            ti = tree_inner(K2,array,S,T,tracker)
            tree1[2].extend(ti[2])
    return [tree1,S,tracker]

def tree_equal(tree1,tree2):
    if tree1[0] != tree2[0] or tree1[1] != tree2[1]:
        return 0
    else:
        l1 = len(tree1[2])
        l2 = len(tree2[2])
        if l1 != l2:
            return 0
        else:
            array1 = tree1[2]
            array2 = tree2[2]
            for i in range(0,l1):
                A=0
                l2 = len(array2)
                for j in range(0,l2):
                    if isinstance(array1[i],list) and isinstance(array2[j],list) and tree_equal(array1[i],array2[j]):
                        array2.pop(j)
                        A=1
                        break
                    if isinstance(array1[i],int) and isinstance(array2[j],int) and array1[i] == array2[j]:
                        array2.pop(j)
                        A=1
                        break
                if A == 0:
                    return 0
            return 1

def min_arrays(array):
    # returns an array containing the indices of the smallest arrays in an array of arrays
    L = len(array)
    mins=[0]
    for i in range(1,L):
        if len(array[mins[0]]) > len(array[i]):
            mins=[i]
        elif len(array[mins[0]]) == len(array[i]):
            mins.append(i)
    return mins

def min_only(array):
    # removes all non-minimum arrays from an array of arrays
    if array == "Impossible":
        return "Impossible"
    elif array == "Trivial":
        return "Trivial"
    else:
        array2=[]
        for i in min_arrays(array):
            array2.append(array[i])
        return array2

def array_equal(array1,array2):
    # returns 1 if the arrays are equal, otherwise returns 0
    A = 1
    l1=len(array1)
    l2=len(array2)
    if l1==l2:
        for i in range(0,l1):
            if (array1[i][2] == array2[i][2] and array1[i][3] == array2[i][3]) and ((array1[i][0] == array2[i][0] and array1[i][1] == array2[i][1]) or (array1[i][0] == array2[i][1] and array1[i][1] == array2[i][0])):
                continue
            else:
                A=0
    else:
        A=0
    return A

def filter_duplicates(array):
    # removes all duplicates 
    if array == "Impossible":
        return "Impossible"
    elif array == "Trivial":
        return "Trivial"
    else:    
        array2 = []
        L = len(array)
        for i in range(0,L):
            A=0
            for j in range(i+1,L):
                if array_equal(array[i],array[j]):
                    A=1
                    break
            if A == 0:
                array2.append(array[i])
        return array2

def filter_equiv(array):
    # removes equivalent arrays
    if array == "Impossible":
        return "Impossible"
    elif array == "Trivial":
        return "Trivial"
    else:
        array2 = []
        L = len(array)
        for i in range(0,L):
            A = 0
            for j in range(i+1,L):
                if tree_equal(tree(array[i]),tree(array[j])):
                    A = 1
                    break
            if A == 0:
                array2.append(array[i])
        return array2

def filter_redundant(array):
    # removes redundant arrays
    if array == "Impossible":
        return "Impossible"
    elif array == "Trivial":
        return "Trivial"
    else:    
        array2=[]
        L = len(array)
        for i in range(0,L):
            if tree(array[i])[0] != 'redundant':
                array2.append(array[i])
        return array2

def filter_redundant2(array):
    # removes arrays which contain add or subtract 0 or times or divide by 1
    array2=[]
    L=len(array)
    for i in range(0,L):
        if redundant2_array(array[i]) == 0:
            array2.append(array[i])            
    return array2

def redundant2_array(array):
    # returns 1 if the array contains an operation which adds/subtracts 0 or multiplies/divides by 1, returns 0 otherwise
    L=len(array)
    for i in range(0,L):
        if op_type(array[i][2])=="M" and (array[i][0] == 1 or array[i][1] == 1):
            return 1
        elif op_type(array[i][2])=="A" and (array[i][0] == 0 or array[i][1] == 0):
            return 1
    return 0