#  File objects


#  Not recommended way of opening files
# f = open('Epictetus - The Enchiridion.txt', 'r')
# For reading and writing 'r+'
# print(f.mode)
# print(f.name)
# f.close()
#  If file is not closes, it can cause leaks

#  Opening with context manager
# with open('Epictetus - The Enchiridion.txt', 'r') as f:
#
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#
#     f.seek(0)
#
#     f_contents = f.read(size_to_read)
#     print(f_contents)

    # print(f.tell())


    # while len(f_contents) > 0:
    #     f_contents = f.read(size_to_read)
    #     print(f_contents, end='*')


    # for i, line in enumerate(f):
    #     print(i, line, end='')

# Automatically close file after the block code is executed, or if break occurred

#  Writing
