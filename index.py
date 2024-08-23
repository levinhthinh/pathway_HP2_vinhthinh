import main

# user([id],ten,mk,id dac biet(1=super user))
user=([1,'tuan','abc',1])

# giohang=([id_user, id_giohang])
giohang=([1,1])

# giohang_chitiet=([id_giohang, id_hang, so luong, gia tien])
giohang_chitiet=([1,'AL',3,200000],[1,'ASM',2,25000])

# hanghoa=(['id_hang','ten', 'gia tien', 'hang ton'])
hanghoa = (['AL','áo len',200000,10],['ASM','áo sơmi',25000,9],['A','áo a',15000,2],['B','áo b',10000,0],['C','áo c',500,6])

# menu = ([ten chuc nang, quyen duoc xem])
menu=(['kiem tra gio hang',[1,2]])
run=True
while run:
    ten=input('ten tai khoan: ')
    mk=input('mat khau tai khoan: ')
    for i in range(len(user)):
        if user[i][1]==ten and user[i][2]==mk:
            print('đăng nhập thành công')
            break
    else:
        print('tên hoặc mật khẩu bị sai, hãy đăng nhập lại')

main.getDataArray()