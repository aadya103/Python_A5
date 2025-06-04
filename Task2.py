org_list = list(i for i in range(1, 11))
ext_list = org_list[:5]
rev_list = ext_list[::-1]

print("Original list: {}".format(org_list))
print("Extracted first five elements: {}".format(ext_list))
print("Reversed first five elements: {}".format(rev_list))