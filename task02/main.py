def merge_k_lists(lists):
    merged = []
    for lst in lists:
        merged = merge_two_sorted_lists(merged, lst)
    return merged

def merge_two_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # add rest elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


if __name__ == "__main__":
    initial_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(initial_lists)
    print("Sorted list:", merged_list)
