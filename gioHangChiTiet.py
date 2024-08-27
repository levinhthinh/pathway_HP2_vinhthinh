def kiem_tra_gio_hang(id, giohang, giohang_chitiet):
    print(id)
    for i in range(len(giohang)):
        if id == giohang[i][0]:
            id_gio_hang=giohang[i][1]

    for i in range(len(giohang_chitiet)):
        if id_gio_hang==giohang_chitiet[i][0]:
            print(f'loai ao:{giohang_chitiet[i][1]:<8} so luong:{giohang_chitiet[i][2]:<2} gia:{giohang_chitiet[i][3]:<6}')    
    return