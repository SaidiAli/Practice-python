a = [i**2 for i in range(10)]
def list_ends(l):
    # new = []
    # new.append(l[:1].pop(0))
    # new.append(l[-1:].pop(0))
    # return new
    return [l[0], l[len(l)-1]]

print(list_ends(a))