import chess, chess.engine, time, pyautogui, pytesseract
from BoardGetter import GetBoard

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
engine = chess.engine.SimpleEngine.popen_uci(r"C:/Program Files/Stockfish/stockfish_15_x64_avx2.exe")

board = chess.Board()
Positions = {
    "Board": (373, 230, 1018, 1018),
    "Download": (5636, 1479),
    "fen": (5240, 782),
    "Close": (5690, 422),
    "Play": (1931, 429),
    "PlayTab": (93, 260),
    "WhiteTurnIndicator": (1212, 1301),
    "BlackTurnIndicator": (1212, 181),
    "NotTurnIndicator": (1237,1301),
    "KingPos": (921, 1198),
    "Name": (429, 152, 263, 29)
}
step = Positions["Board"][2] / 8
boardpic = None

def get_region(x,y):
    x = (Positions["Board"][0] - step / 2) + x * step
    y = (Positions["Board"][1] + Positions["Board"][3] + step / 2) - y * step
    region = (x - (1/3) * step, y - (1/3) * step, (2/3) * step, (2/3) * step)
    img = pyautogui.screenshot(region=region)
    return img

pieceMap = {}
def registerBoard():
    #top pieces
    pieceMap['q'] = get_region(4,8)
    pieceMap['k'] = get_region(5,8)
    pieceMap['b'] = get_region(6,8)
    pieceMap['n'] = get_region(7,8)
    pieceMap['r'] = get_region(8,8)
    pieceMap['p'] = get_region(8,7)

    #bottom pieces
    pieceMap['Q'] = get_region(4,1)
    pieceMap['K'] = get_region(5,1)
    pieceMap['B'] = get_region(6,1)
    pieceMap['N'] = get_region(7,1)
    pieceMap['R'] = get_region(8,1)
    pieceMap['P'] = get_region(8,2)

    for key in pieceMap:
        pieceMap[key].save("Pieces/" + key + str(ord(key)) + ".png")

#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
amBlack = None
def getBoardCoords(position):
    result = [None, None]
    for x in range(1,9):
        if position[0] < Positions["Board"][0] + x * step:
            result[0] = x
            break
    for y in range(1,9):
        if position[1] < Positions["Board"][1] + y * step:
            result[1] = y
            break
    return result

def getBoard():
    print("getting board")
    result = []
    for i in range(8):
        result.append([None] * 8)
        
    posDict = GetBoard(pieceMap, Positions["Board"])
    for key in posDict:
        for pos in posDict[key]:
            coord = getBoardCoords(pyautogui.center(pos))
            if coord[0] != None and coord[1] != None:
                result[coord[1] - 1][coord[0] - 1] = key
    
    fen = ""
    for row in result:
        carry = 0
        for cell in row:
            if cell == None:
                carry += 1
            else:
                if carry > 0:
                    fen += str(carry)
                    carry = 0
                fen += cell
        if carry > 0:
            fen += str(carry)
        fen += "/"
    return chess.Board(fen[:-1] + (" b" if amBlack else " w") +  " KQkq - 0 1")

def playMove(move):
    time.sleep(.2)
    x = (Positions["Board"][0] - step / 2) + (ord(move[0]) - 96) * step
    y = (Positions["Board"][1] + Positions["Board"][3] + step / 2) - int(move[1]) * step
    pyautogui.click((x, y))
    time.sleep(.2)
    x = (Positions["Board"][0] - step / 2) + (ord(move[2]) - 96) * step
    y = (Positions["Board"][1] + Positions["Board"][3] + step / 2) - int(move[3]) * step
    pyautogui.click((x, y))

game = True
while game:
    board = chess.Board()
    time.sleep(3)
    pyautogui.click(Positions["PlayTab"])
    time.sleep(1)
    pyautogui.click(Positions["Play"])
    time.sleep(1)
    pyautogui.click(Positions["Play"])
    time.sleep(3)
    name = pytesseract.image_to_string(pyautogui.screenshot(region=Positions["Name"])).strip()
    print("name: " + name)
    amBlack = '=' in name and "[0" in name
    print(amBlack)
    registerBoard()
    while not board.is_game_over():
        #wait for turn
        print("waiting for turn")
        while True:
            sc = pyautogui.screenshot()
            if amBlack and sc.getpixel(Positions["BlackTurnIndicator"]) == (255,255,255):
                break
            if not amBlack and sc.getpixel(Positions["WhiteTurnIndicator"]) == (49,46,43) and sc.getpixel(Positions["NotTurnIndicator"]) == (255,255,255):
                break
            time.sleep(.1)
        
        #get move
        board = getBoard()
        print(board.fen)
        move = engine.play(board, chess.engine.Limit(time=.3))
        #play move
        print(move.move)
        playMove(str(move.move))
        board.push(chess.Move.from_uci(str(move.move)))
        if board.is_game_over():
            break
        time.sleep(1)