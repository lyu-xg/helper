no_show = ['XueGuang', 'Xu', 'QiuYuan']
names = ['XueGuang', 'Xu', 'QiuYuan', 'MingNa', 'YuZhao', 'TianYi', 'TianXiao', 'QianHan']
monthly_fee = 85

def split(lst, mth_fee=monthly_fee, i=0):
    lst[i] -= mth_fee
    each = mth_fee/len(lst)
    return [n+each for n in lst]

def validate_mth(mth):
    return mth if mth <= 12 else mth%12

def print_fee(fees, mth_no):
    m = '{}月10日至{}月10日'.format(validate_mth(mth_no), validate_mth(mth_no+1)) if type(mth_no) is int else mth_no
    print('{}话费如下：'.format(m))
    for i, name in enumerate(names):
        if name not in no_show:
            print('{}: {}'.format(name, round(fees[i], 2)))
    print('\n')

def print_multi_mth(fees_matrix, starting_mth):
    for i, fees in enumerate(fees_matrix):
        print_fee(fees, starting_mth+i)

def main(fees_matrix, starting_mth):
    if not fees_matrix:
        print('gimme some fees!'); return
    if not all(len(l) == len(fees_matrix[0]) for l in fees_matrix):
        print('please pass in a well-shaped matrix - -'); return
    print('亲爱的大家：')
    fees_matrix = [split(f) for f in fees_matrix]
    print_multi_mth(fees_matrix, starting_mth)
    total_fees = [sum(fees_matrix[j][i] for j in range(len(fees_matrix))) for i in range(len(fees_matrix[0]))]
    print_fee(total_fees, '总共')

def one_mth(fees, mth):
	main([fees,], mth)

if __name__ == '__main__':

    #   ['XueGuang', 'Xu', 'QiuYuan', 'MingNa', 'YuZhao', 'TianYi', 'TianXiao', 'QianHan']
    main([[110.88 + 14.57, 66.54, 25.88, 25.88, 25.88, 25.88, 25.88, 37.87],
          [110.95 + 14.61, 66.61, 25.95, 25.95, 165.65, 25.95, 25.95, 173.27]],11)