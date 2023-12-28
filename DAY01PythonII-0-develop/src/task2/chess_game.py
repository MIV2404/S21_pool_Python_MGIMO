def reach_pos(pos0, pos1, piece):
    dx, dy = abs(int(pos0[0]) - int(pos1[0])), abs(int(pos0[1]) - int(pos1[1]))
    dct = {'king':(dx, dy) in ((1, 0), (0, 1), (1, 1)),
        'rook':(dx == 0) or (dy == 0),
        'bishop':(dx == dy),
        'knight':((dx == 1 and dy == 2) or (dx == 2 and dy == 1)) and not (dx == 0 or dy == 0)}
    return dct[piece] if piece in dct else False

def validation_coord(coord):
    valid = coord.isdigit() and 0 < int(coord) < 9
    # if not valid:
    #     print('Координаты введены не корректно\nДолжны быть заданы целыми числами в диапазоне от 1 до 8')
    return valid

def validation_figure(figure):
    valid = figure.isalpha() and (figure.lower() in ('knight', 'rook', 'bishop', 'king'))
    # if not valid:
    #     print('Название фигуры введено не корректно\nМогут быть заданы фигуры knight, rook, bishop или king')
    return valid

while True:
    try:
        pos0 = input().split()
        pos1 = input().split()
        piece = input()
        
        if validation_coord(pos0[0]) and validation_coord(pos0[1]):
            x0, y0 = pos0[0], pos0[1]
            if validation_coord(pos1[0]) and validation_coord(pos1[1]):
                x1, y1 = pos1[0], pos1[1]
                if validation_figure(piece):
                    piece = piece.lower()
       
        print(reach_pos([x0, y0], [x1, y1], piece))
    
    except EOFError:
        break
