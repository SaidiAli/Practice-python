a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]

def no_duplicate(a_list):
    new = []
    for i in a_list:
        if i in new:
            continue
        else:
            new.append(i)
    return new

# using sets

def no_dup(a):
    return list(set(a))

print(no_dup(a))