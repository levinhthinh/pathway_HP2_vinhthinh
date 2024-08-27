# hanghoa={
#     {
#         'ma_hang':'AL',
#         'id':1,
#         'ten_hang':'ao len',
#         'gia_tien':200000,
#         'so luong':10,
#         'loai':1
#     },
#     {
#         'ma_hang':'ASM',
#         'id':2,
#         'ten_hang':'ao somi',
#         'gia_tien':25000,
#         'so luong':9,
#         'loai':2
#     },
#     {
#         'ma_hang':'A',
#         'id':3,
#         'ten_hang':'ao a',
#         'gia_tien':15000,
#         'so luong':2,
#         'loai':2

#     },
#     {
#         'ma_hang':'B',
#         'id':4,
#         'ten_hang':'ao b',
#         'gia_tien':10000,
#         'so luong':0,
#         'loai':3

#     },
#     {
#         'ma_hang':'C',
#         'id':5,
#         'ten_hang':'ao C',
#         'gia_tien':500,
#         'so luong':6,
#         'loai':1
#     },
# }

loai={
    1: 'ao len',
    2: 'ao somi',
    3: 'ao hoodie',
}
loai2={1,2,3,'hi'}
val='none'
copied=loai.copy()
print(copied)
# copied.clear()
# print(copied)
# print(copied.pop(3))
# print(dict.fromkeys(loai2,val))
# print(copied.get(3))
# print(copied.popitem())
# print(copied.items())
# print(copied.values())
# print(copied.setdefault(3,'None'))
# print(copied.setdefault(2,'None'))
# print(copied.update({5:'ao'}))
# print(copied)
max=list(copied.keys())
print(max)

