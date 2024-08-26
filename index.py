# import main

def mua_hang_hoa(id):
    bracket=[]
    print(id)
    global giohang_chitiet, giohang
    for x in range(len(giohang)):
        if id in giohang[x]:
            id_gio_hang=giohang[x][1]
            break
    else:
        id_gio_hang='GH'+str(len(giohang)+1)
        giohang.append([id,id_gio_hang])

    print(giohang)
    print(id_gio_hang)
    for i in range(len(hanghoa)):
        print(f'{i+1}.{hanghoa[i][1]:<8} gia:{hanghoa[i][2]:<6} con:{hanghoa[i][3]:<2}')
    print('nhap "0" khi da mua xong')
    
    while True:
        a=int(input('loai ao muon mua '))
        if a == 0 :
            break

        b=int(input('so luong '))
        for i in range(len(bracket)):
            if bracket[i][0] == hanghoa[a-1][0]:
                if bracket[i][1]+b >hanghoa[a-1][3]:
                    print('khong du hang')
                    break
                else:
                    bracket[i][1]+=b
                    break
        else:
            if b>hanghoa[a-1][3]:
                print('khong du hang')
            else:
                bracket.append([hanghoa[a-1][0],b,hanghoa[a-1][2]])
    
    for y in range(len(bracket)):
        giohang_chitiet.append([id_gio_hang])
        for i in range(3):
            giohang_chitiet[len(giohang_chitiet)-1].append(bracket[y][i])
    print(bracket)
    print(giohang_chitiet)
    return  

def kiem_tra_gio_hang(id):
    pass
# user([id,ten,mk,id dac biet #1=super_user,0=user,)
user=([1,'admin1','@1234',1],[2,'ad_min','1234',1],[3,'tuan','@1234',0],[4,'abc','dino',0],[5,'anh vu','HI1234',0])

# giohang=[[id_user, id_giohang],]
giohang=[[1,'GH1'],[2,'GH2'],]

# giohang_chitiet=[[id_giohang, id_hang, so luong, gia tien],]
giohang_chitiet=[['GH1','AL',3,200000],['GH1','ASM',2,25000]]

# hanghoa=(['id_hang','ten', 'gia tien', 'hang ton'])
hanghoa = (['AL','áo len',200000,10],['ASM','áo sơmi',25000,9],['A','áo a',15000,2],['B','áo b',10000,0],['C','áo c',500,6])

# menu = ([ten chuc nang, quyen duoc xem],func)
menu=(['mua hang hoa',[0],mua_hang_hoa()],['kiem tra gio hang',[0]],['tinh tien',[0]],['kiem tra lich su mua hang',[0]],['quan li hang hoa',[1]],['quan li khach hang',[1]],['thong ke',[1]],['thoat trinh',[0,1]])

while True:
    ten=input('ten tai khoan: ')
    mk=input('mat khau tai khoan: ')
    for i in range(len(user)):
        if user[i][1]==ten and user[i][2]==mk:
            print('đăng nhập thành công')
            id=user[i][0]
            quyen=user[i][3]
            using=True
            break
    else:
        print('tên hoặc mật khẩu bị sai, hãy đăng nhập lại')
        using=False
    # while using:
    #     a=1
    #     for i in range(len(menu)):
    #         if quyen in menu[i][1]:
    #             print(f'{a}.{menu[i][0]}')
    #             a+=1
    #     input('ban muon lam gi: ')
    mua_hang_hoa(id)
