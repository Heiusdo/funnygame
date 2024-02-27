day = int(input())
month = int(input())
match month:
    case 1:
        if 1 <= day <= 19:
            print('ma ket')
        elif 20 <= day <= 31:
            print('bao binh')
        else:
            print('invalid day')
    case 2:
        if 1 <= day <= 18:
            print('bao binh')
        elif 19 <= day <= 28:
            print('song ngu')
        else:
            print('invalid day')
    case 3:
        if 1 <= day <= 21:
            print('song ngu')
        elif 22 <= day <= 31:
            print('bach duong')
        else:
            print('invalid day')
    case 4:
        if 1 <= day <= 20:
            print('bach duong')
        elif 21 <= day <= 30:
            print('kim nguu')
        else:
            print('invalid day')
    case 5:
        if 1 <= day <= 20:
            print('kim nguu')
        elif 21 <= day <= 31:
            print('song tu')
        else:
            print('invalid day')
    case 6:
        if 1 <= day <= 21:
            print('song tu')
        elif 22 <= day <= 30:
            print('cu giai')
        else:
            print('invalid day')
    case 7:
        if 1 <= day <= 22:
            print('cu giai')
        elif 23 <= day <= 31:
            print('su tu')
        else:
            print('invalid day')
    case 8:
        if 1 <= day <= 22:
            print('su tu')
        elif 23 <= day <= 31:
            print('xu nu')
        else:
            print('invalid day')
    case 9:
        if 1 <= day <= 22:
            print('xu nu')
        elif 23 <= day <= 30:
            print('thien binh')
        else:
            print('invalid day')
    case 10:
        if 1 <= day <= 23:
            print('thien binh')
        elif 24 <= day <= 31:
            print('bo cap')
        else:
            print('invalid day')
    case 11:
        if 1 <= day <= 22:
            print('bo cap')
        elif 23 <= day <= 30:
            print('nhan ma')
        else:
            print('invalid day')
    case 12:
        if 1 <= day <= 21:
            print('nhan ma')
        elif 22 <= day <= 31:
            print('ma ket')
        else:
            print('invalid day')
    case _:
        print("invalid month")
#ngu


