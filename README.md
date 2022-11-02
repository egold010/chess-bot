# chess-bot
Bot to automatically play ladder on chess.com.
Disclaimer: I do not support the use of unbeatable bots to cheat in chess.

Uses the Stockfish engine to generate moves and pytesseract to identify which side of the board the bot is playing for.

For the code to work:
-You will probably have to change the Positions dictionary to fit your screen.
-You must also have Stockfish and Tesseract-OCR and set the paths to the executable.
-Board and Pieces settings on chess.com must be set to the following:
Pieces: Alpha
Board: Green
Move Method: Click Squares
Highlight Moves: Off
White always on bottom: On
Show Legal Moves: Off
-The indicator of the player's username must be changed to match your username (line 117)
