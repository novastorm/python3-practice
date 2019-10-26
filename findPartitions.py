def find_partitions(input_list):
    results = []

    fIdx = 0

    for i in range(len(input_list)):
        if i == len(input_list) - 1 or input_list[i + 1] - 1 != input_list[i]:
            if fIdx == i :
                results.append("{}".format(input_list[fIdx]))
            else:
                results.append("{}-{}".format(input_list[fIdx], input_list[i]))
            fIdx = i + 1

    return results

print(find_partitions([1,3,5,7]))
print(find_partitions([1,3,5]))
print(find_partitions([1,2,3,6,7,8,10,11]))
print(find_partitions([1,2,5,8,10]))
