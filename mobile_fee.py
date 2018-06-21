no_show = ['XueGuang', 'Xu', 'QiuYuan']
names = ['857-407-8735', 'XueGuang', 'QianHan', 'Xu', 'QiuYuan', 'MingNa', 'YuZhao', '949-402-9822', 'TianYi', 'TianXiao']
monthly_fee = 85

def split(lst, mth_fee=monthly_fee, i=0):
    lst[i] -= mth_fee
    each = mth_fee/len(lst)
    return [round(n+each, 2) for n in lst]

def validate_mth(mth):
    return mth if mth <= 12 else mth%12

def print_fee(fees, mth_no):
    m = '{}月10日至{}月10日'.format(validate_mth(mth_no), validate_mth(mth_no+1)) if type(mth_no) is int else mth_no
    print('{}话费如下：'.format(m))
    for i, name in enumerate(names):
        if name not in no_show:
            print('{}: {}'.format(name, fees[i]))
    print('\n')

def print_multi_mth(fees_matrix, starting_mth):
    for i, fees in enumerate(fees_matrix):
        print_fee(fees, starting_mth+i)

def save_fee(fees):
    with open('save.csv', 'w') as outfile:
        outfile.write(','.join(names)+'\n')
        outfile.write(','.join(map(str, fees))+'\n')

def main(fees_matrix, starting_mth):
    if not fees_matrix:
        print('gimme some fees!'); return
    if not all(len(l) == len(fees_matrix[0]) for l in fees_matrix):
        print('please pass in a well-shaped matrix - -'); return
    print('亲爱的大家：')
    fees_matrix = [split(f, i=1) for f in fees_matrix]
    print_multi_mth(fees_matrix, starting_mth)
    total_fees = [round(sum(fees_matrix[j][i] for j in range(len(fees_matrix))), 2) for i in range(len(fees_matrix[0]))]
    save_fee(total_fees)
    print_fee(total_fees, '总共')

def one_mth(fees, mth):
	main([fees,], mth)

if __name__ == '__main__':

    #   ['857-407-8735', 'XueGuang', 'Qianhan', 'Xu', 'QiuYuan', 'MingNa', 'YuZhao', '949-402-9822', 'TianYi', 'TianXiao']
    main([[14.61, 110.95, 37.94, 66.61, 25.95, 25.95, 25.95, 32.75, 25.95, 46.93],
          [14.61, 110.95, 37.94, 66.61, 25.95, 25.95, 25.95, 25.95, 25.95, 29.15],
          [15.13, 111.43, 38.42, 67.09, 26.43, 26.43, 26.43, 26.43, 26.43, 26.43],
          [15.13, 111.46, 38.42, 35.42, 26.43, 26.43, 26.43, 26.43, 26.43, 26.43],
          [15.96, 112.26, 39.25, 36.25, 27.26, 27.26, 27.26, 27.26, 27.26, 27.26    ]],1)