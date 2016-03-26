"""
heap.heap_test
~~~~~~~~~~~~~~

My implementation of Heaps algorithm
Version 3
"""


def heap_perm(n, A):
    """
    Generates a permutation.
    """
    if n == 1:
        yield A
    else:
        for i in range(n-1):
            for hp in heap_perm(n-1, A):
                yield hp
            j = 0 if (n % 2) == 1 else i
            A[j],  A[n-1] = A[n-1], A[j]
        for hp in heap_perm(n-1, A):
            yield hp


def perm_num(lst):
    """
    Finds out how many permutations there are.
    """
    count = 1
    for x in range(len(lst)):
        y = x+1
        count = count * y
    return count


def heap_gen(gen, n):
    """
    Runs all the possible recursions from the generator. 
    """
    perms = []
    for x in range(n):
        perms.append(''.join(list(gen.__next__())))
    return perms


def main():
    """
    Test function.
    """
    lst = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i']
    gen = heap_perm(len(lst), lst)
    num = perm_num(lst)
    perms = heap_gen(gen, num)
    # print(perms)
    print(len(perms))

if __name__ == '__main__':
    main()
