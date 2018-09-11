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
#     #  seek() jumping to file start, read() continues from last read
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
#  if i use 'r+' it doesnt behave like 'w' -> w seek w = w; 'r+' = ww
'''
with open('test.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

    print('Writing file {}, size: {} bytes'.format(f.name, f.tell()))
'''

#  Let's do some copying, working with multiple files
'''
with open('Epictetus - The Enchiridion.txt', 'r') as rf:
    with open('test.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            print('\nWriting line: {} file size: {} bytes'.format(line, wf.tell()))
'''

#  How to copy non text files (use byte)
with open('git_workflow.png', 'rb') as rf:
    with open('git_workflow_copy.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            print(wf.tell())

