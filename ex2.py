import sys

if __name__ == '__main__':
    # Enter the list in one line.
    a = list(map(int, input().split()))
    # If the list is empty, terminate the program.
    if not a:
        print("Given list is empty", file=sys.stderr)
        exit(1)

    # Determine the indices of the minimum and maximum elements.
    a_min = a_max = a[0]
    i_min = i_max = 0
    for i, item in enumerate(a):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item

            # Check indexes and swap them.
            if i_min > i_max:
                i_min, i_max = i_max, i_min

            # Count the number of positive elements.
            count = 0
            for item in a[i_min + 1:i_max]:
                if item > 0:
                    count += 1
            print(count)