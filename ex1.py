import sys

if __name__ == '__main__':
    # Enter the list in one line.
    A = list(map(int, input().split()))
    # Check the number of elements in the list.
    if len(A) != 10:
        print("Wrong list size", file=sys.stderr)
        exit(1)
    # Find the required amount.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)