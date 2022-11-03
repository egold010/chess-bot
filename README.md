# chess-bot
Bot to automatically play ladder on chess.com.<br/>
Disclaimer: I do not support the use of unbeatable bots to cheat in chess.<br/>

Uses the Stockfish engine to generate moves and pytesseract to identify which side of the board the bot is playing for.

For the code to work:<br/>
-You will probably have to change the Positions dictionary to fit your screen.<br/>
-You must also have Stockfish and Tesseract-OCR and set the paths to the executable.<br/>
-Board and Pieces settings on chess.com must be set to the following:<br/>
Pieces: Alpha<br/>
Board: Green<br/>
Move Method: Click Squares<br/>
Highlight Moves: Off<br/>
White always on bottom: On<br/>
Show Legal Moves: Off<br/>
-The indicator of the player's username must be changed to match your username (line 117)<br/>
