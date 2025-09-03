def lengthLongestPath(input):
    
    input = input.split('\n')
    print(input)
    res = 0
    level = {
        0: 0
    }

    for entry in input:
        # remove \t
        remove_tab = entry.replace('\t', '')
        num_tabs = entry.count('\t')
        print(remove_tab, entry, num_tabs)
        print(level)
        if '.' in entry:
            # this is a file
            res = max(res, level[num_tabs] + len(remove_tab))
        else:
            level[num_tabs+ 1] = level[num_tabs] + len(remove_tab) + 1 # +1 for /
    
    print(res)
    return res
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# dir/subdir2/file.ext
lengthLongestPath(input)

{
# key is level value is length until this level
# at first it should be 0: 0
# for each element in side splitted input by \n
# decide folder level by the number of \t
# current folder level length is equal current name length + previous level folder
# if current entry is a file
# calculate it length and decide if that file is the longest
# current file length is equal to current file length + folder level length, how to get current level
# length -> number of \t
}