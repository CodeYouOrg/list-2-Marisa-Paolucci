# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

def remove_adjacent(nums):
    if not nums:
        return []
    new_list = [nums[0]]
    for num in nums[1:]:
        if num != new_list[-1]:
            new_list.append(num)
    return new_list

# defined function remove_adjacent and passing parameter "nums" through it.
# second line checks to see if the list is empty.
# created variable list1. [nums[0]] makes sure that the first element in the list is always included.
# the for loop iterates over the elements of 'nums' starting from the second element [1:]. This creates a sublist that excludes the first number.
# the if statement checks to see if the current element 'num' is different from the last element in the new_list list. 'new_list[-1]' refers to the last element in the new_list list. 
# new_list.append(num) appends the current element 'num' to the 'new_list' list if it is different from the last result in new_list.


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

def linear_merge(list1, list2):
    a, b = 0, 0
# a, b are used as pointers for list1 and list2 as empty lists to store the merged results
    merged_list = []

    while a < len(list1) and b < len(list2):
# creates a loop to go through the entire list.
        if list1[a] < list2[b]:
# compares the two lists. If list1[a] is smaller, it appends list1[a] to merged_list and increments 'a'.
            merged_list.append(list1[a])
            a += 1
        else: 
            merged_list.append(list2[b])
            b += 1
# otherwise it appends list2[b] to merged_list and increments b.

    while a < len(list1):
        merged_list.append(list1[a])
        a += 1
# in case there are remaining elements in list1, this while loop will append the elements to the merged_list

    while b < len(list2):
        merged_list.append(list2[b])
        b += 1
# in case there are remaining elements in list2, this while loop will append the elements to the merged_list
    return merged_list

# I originally tried a simple sorted function. However, I learned that this is not efficient for linear time. The two-pointer approach is more efficient and can be used for larger lists.

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print()
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
