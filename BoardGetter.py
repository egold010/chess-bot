import pyautogui as pg
import PIL

CONFIDENCE = 0.75
DETECTION_NOISE_THRESHOLD = 8

def changeBackground(imgPath, color):
    img = PIL.Image.open(imgPath)
    datas = img.getdata()
    newData = []
 
    for item in datas:
        if sum(item) > 10 and sum(item) < 750:
            newData.append(color)
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(imgPath)

def GetBoard(pieceMap, region):
    piece_locations = {
        'k': [],
        'q': [],
        'r': [],
        'b': [],
        'n': [],
        'p': [],
        'N': [],
        'P': [],
        'K': [],
        'Q': [],
        'R': [],
        'B': []
    }
    
    for piece in pieceMap:
        changeBackground("Pieces/" + piece + str(ord(piece)) + ".png", (238, 238, 210))
        for location in pg.locateAllOnScreen("Pieces/" + piece + str(ord(piece)) + ".png", region=region, confidence=CONFIDENCE):
            for position in piece_locations[piece]:
                if abs(position.left - location.left) < DETECTION_NOISE_THRESHOLD and abs(position.top - location.top) < DETECTION_NOISE_THRESHOLD:
                    continue

            piece_locations[piece].append(location)
        
        changeBackground("Pieces/" + piece + str(ord(piece)) + ".png", (118, 150, 86))
        for location in pg.locateAllOnScreen("Pieces/" + piece + str(ord(piece)) + ".png", confidence=CONFIDENCE):
            for position in piece_locations[piece]:
                if abs(position.left - location.left) < DETECTION_NOISE_THRESHOLD and abs(position.top - location.top) < DETECTION_NOISE_THRESHOLD:
                    continue
            
            piece_locations[piece].append(location)
            
    return piece_locations