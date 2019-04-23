def split(lst):
    # lst[i] -= mth_fee
    each = monthly_fee/(sum(i>0 for i in lst)-1)
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
    fees_matrix = [split(f) for f in fees_matrix]
    print_multi_mth(fees_matrix, starting_mth)
    total_fees = [round(sum(fees_matrix[j][i] for j in range(len(fees_matrix))), 2) for i in range(len(fees_matrix[0]))]
    save_fee(total_fees)
    print_fee(total_fees, '总共')

def one_mth(fees, mth):
	main([fees,], mth)

if __name__ == '__main__':
    monthly_fee = 86
    no_show = ['iPad', 'XueGuang', 'Xu', 'QiuYuan']
    names = ['iPad', 'Xu', 'QiuYuan', 'XueGuang', 'MingNa', 'YuZhao', 'TianYi Brother', 'TianYi', 'TianXiao', 'QianHan']
    #   ['857-407-8735', 'XueGuang', 'Qianhan', 'Xu', 'QiuYuan', 'MingNa', 'YuZhao', '949-402-9822', 'TianYi', 'TianXiao']
    main([
        [15.93, 36.20, 27.21, 37.36, 27.21, 27.21, 27.21, 27.21, 30.19, 39.20],
        [15.93, 36.20, 27.21, 27.21, 58.72, 39.73, 27.21, 27.21, 27.21, 39.20],
        [29.46, 36.20, 0,     27.21, 28.64, 89.86, 27.21, 27.21, 27.21, 39.20],
        [0,     78.06, 0,     27.40, 27.40, 27.40, 27.40, 27.40, 39.39, 22.89],
        [0,     78.06, 0,     27.40, 27.40, 27.40, 27.40, 27.40, 39.39, 23.24],
        [0,     78.06, 0,     27.40, 27.40, 27.40, 27.40, 28.50, 39.39, 23.24],
        [23.24, 84.26, 0,     27.90, 198.56,27.90, 27.90, 27.90, 27.90, 85.73],
        [23.24, 228.00,0,     25.34, 52.99 ,25.34, 25.34, 25.34, 25.34, 83.17],
        
	  	],7)
