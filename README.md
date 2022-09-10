
# An Interactive 1 v 1 chess like grid game using python

# Game rules:
There are 2 players playing it
The game is played on a square grid of 5 by 5 blocks
Each player has a team of 5 characters that start from their end


# Move commands:
L - left move
R - right move
F - front move
B - back move

These moves are relative to the player.
 
# Characters:
Pawn: In one move, it moves 1 block straight in any direction (L, R, F, B)

The opponent player’s character dies when a player’s character is moved to the opponent character’s position

# Game flow:
Each player can arrange their characters on their end in any order. They will have 5 pawns to start with and will need to deploy all of them at the start of the game.

The input for initial character positions will be taken as a list of character names, placing them from left to right on the starting lanes. Once this process is complete for both the players, they can start making moves.
 
The application then takes move inputs from the players, alternating between the players, updating the game state in the process.

Input move format: <character_name>:<move>  (e.g. P1:L, P2:R, P3:F, P3:B)

An invalid input move should be handled and prompted to the user(Invalid input format) and make the player retry their turn.

# Invalid moves for a player:
Input command on a character that does not exist
Character going out of grid bounds.
Invalid move presented for a given character.
Targeting a friendly character, i.e a character from our own team.

The game ends when one player (winner) manages to kill all characters of their opponent. 
	
# Screenshots:

![image](https://user-images.githubusercontent.com/87854476/189495126-abe93dd9-0b37-4ddb-aa89-0fbadf1dc913.png)
![image](https://user-images.githubusercontent.com/87854476/189495137-8bc79186-12f4-4a7c-aacb-30b431acbb43.png)
![image](https://user-images.githubusercontent.com/87854476/189495143-fd56413f-9b4d-4287-b914-bdf1745afd70.png)
![image](https://user-images.githubusercontent.com/87854476/189495159-3adfec7c-8287-4cf4-8b0e-7a21456b8a8c.png)
![image](https://user-images.githubusercontent.com/87854476/189495169-a298d764-4bb8-4b47-a1fb-56772dc6a8c2.png)
![image](https://user-images.githubusercontent.com/87854476/189495175-8855e7a4-ca05-449c-9205-9638bd8aefd2.png)

