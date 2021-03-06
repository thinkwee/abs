dup_index = []


def init():
    res_list = []
    f = open('./data/headline_middle_sen.txt', 'r')
    index = 0

    for line in f.readlines():
        if line not in res_list:
            res_list.append(line)
            dup_index.append(index)
        index += 1

    f.close()
    print("init complete")


def make_dedup_file(file_name):
    file = open('./data/' + file_name + '_middle_sen.txt', 'r')
    file_dedup = open('./data/' + file_name + '_middle_sen_dedup.txt', 'w')
    index = 0
    for line in file:
        if index in dup_index:
            file_dedup.write(line)
        index += 1
    print(file_name + " output complete")


def make_dedup_index():
    file = open('./data/sen_index_raw.txt', 'r')
    index_sen = file.read().split()
    file.close()
    file = open('./data/sen_index_raw_dedup.txt', 'w')
    for index in dup_index:
        file.write(index_sen[index] + ' ')
    print('dedup sen index output complete')


init()
# print(len(dup_index))
# make_dedup_file('headline')
# make_dedup_file('article')
make_dedup_index()
