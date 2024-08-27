user=([1,'admin1','@1234',1],[2,'ad_min','1234',1],[3,'tuan','@1234',0],[4,'abc','dino',0],[5,'anh vu','HI1234',0])
user={
    'admin1':{
        'id':1,
        'pass':'@1234',
        'quyen':'admin'
    },
    'ad_min':{
        'id':2,
        'pass':'1234',
        'quyen':'admin'
    },
    'tuan':{
        'id':3,
        'pass':'@1234',
        'quyen':'user'
    },
    'abc':{
        'id':4,
        'pass':'dino',
        'quyen':'user'
    },
    'anh vu':{
        'id':5,
        'pass':'HI1234',
        'quyen':'user'
    },
}

role={
    'admin':{
        'menu':['quan li user', 'quan li thong ke','quan li hang hoa']
    },
    
    'user':{
        'menu':['mua hang','kiem tra lich su mua','gio hang']
    }
}