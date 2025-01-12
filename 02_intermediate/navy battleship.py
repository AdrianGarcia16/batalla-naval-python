

class GameBoard:
    def __init__(self, player1, player2, game1, game2, life_player1, life_player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_impact = game1
        self.player2_impact = game2
        self.player1_life = life_player1
        self.player2_life = life_player2
 
    def get_player_board(self, player):
        if player == "1":
            return self.player1
        else:
            return self.player2

    def assign_player_board(self, player, board):
        if player == "1":
            self.player1 = board
        else:
            self.player2 = board
    
    def print_board(self, player):
        if player == "1":
            board = self.player1_impact
        else:
            board = self.player2_impact
        for fila in board:
            print(" ".join(map(str, fila)))
    
    def hit_life(self, player):
        if player == "1":
            self.player1_life -= 1
        else:
            self.player2_life -= 1
        if self.player1_life == 0:
            return "2"
        elif self.player2_life == 0:
            return "1"
        else:
            return ""


class BattleshipGame(GameBoard):
    def __init__(self, player1, player2, game1, game2, life_player1, life_player2):
        super().__init__(player1, player2, game1, game2, life_player1, life_player2)

    def place_ship_on_board(self, assign, ship_details):
        # Determinar el tablero correspondiente
        if assign == "1": 
            board = self.player1
        else:
            board = self.player2

        # Extraer detalles del barco
        row = ship_details['row']
        col = ship_details['col']
        lon = ship_details['lon']
        direction = ship_details['dir']

        # Validar si las coordenadas iniciales son válidas
        if row < 0 or row > 9 or col < 0 or col > 9:
            return False, "Coordenadas iniciales fuera del tablero"

        # Validar si el barco cabe en el tablero
        if direction == "H" and col + lon > 10:
            return False, "El barco sale del tablero horizontalmente"
        if direction == "V" and row + lon > 10:
            return False, "El barco sale del tablero verticalmente"

        # Validar superposición de barcos
        temp_row, temp_col = row, col
        for _ in range(lon):
            if board[temp_row][temp_col] == "B":
                return False, "El barco se sobrepone a otro"
            if direction == "H":
                temp_col += 1
            else:
                temp_row += 1

        # Colocar el barco en el tablero
        for _ in range(lon):
            board[row][col] = "B"
            if direction == "H":
                col += 1
            else:
                row += 1

        # Asignar el tablero actualizado
        self.assign_player_board(assign, board)
        return True, "Barco colocado exitosamente"


    def atack(self, positionX, positionY, defender):
        if defender == "1":
            board = self.player2
            board_impact = self.player2_impact
        else:
            board = self.player1
            board_impact = self.player1_impact
        
        if board[positionX][positionY] == "*":
            # failure
            board_impact[positionX][positionY] = "X"
            return "AGUA!!!!"
            
        elif board_impact[positionX][positionY] == "X" or board_impact[positionX][positionY] == "O":
            return "repetido"
        else:
            # navy
            board_impact[positionX][positionY] = "O"
            # check if the navy is destroyed
            winner = self.hit_life(defender)
            if winner != "":
                return winner
            return "BARCO!!!!"
        pass
        


class validations:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        pass
    
    def check(self):
        if self.tipo == "coordenada":
            if not isinstance(self.valor, int):
                return False
            if self.valor > 9 or self.valor < 0:
                return False
        if self.tipo =="direccion":
            if str(self.valor) not in ["H", "V"]:
                return False
        return True


if __name__ == "__main__":
    print(f'----------------- ----------')
    print(f'----------WELCOME----------')
    print(f'---------------------------')
    print()
    print()
    print()
    navy = [
        ["Portaaviones", 2],
        ["Acorazados", 2],
        #["Cruceros", 3],
        #["Submarinos", 3],
        #["Destructores", 2],
        ]
    size = 10
    max_life = int(sum([nav[1] for nav in navy]))
    matriz1 = [["*" for _ in range(size)] for _ in range(size)]
    matriz2 = [["*" for _ in range(size)] for _ in range(size)]
    matriz_game1 = [["*" for _ in range(size)] for _ in range(size)]
    matriz_game2 = [["*" for _ in range(size)] for _ in range(size)]
    players = ["1", "2"]
    game = BattleshipGame(matriz1, matriz2, matriz_game1, matriz_game2, max_life, max_life)
    
    for player in players:
        for nav in navy:
            repetir = True
            while repetir: 
                print(F'Jugador  {player} coloca sus barcos.................')
                print(F'Las coodenadas son valores del 0 al 9........')
                correcto = False
                print(f'{nav[0]} de tamaño {nav[1]}', )
                while not(correcto):
                    x = input("Fila inicial: ")
                    if validations(x, "coordenada"):
                        correcto = True
                    else:
                        print(f"ERROR {y} no es un numero de 0 al 9")
                correcto = False
                while not(correcto):
                    y = input("Columna inicial: ")
                    if validations(y, "coordenada"):
                        correcto = True
                    else:
                        print(f"ERROR {y} no es un numero de 0 al 9")
                
                correcto = False
                while not(correcto):
                    d = input("Dirección (H para horizontal y V para vertical): ")
                    if isinstance(d, str):
                        d = d.upper()
                    if validations(d, "coordenada"):
                        correcto = True
                    else:
                        print(f"ERROR {d} no es un valor indicado")
                # end capture of navy
                #Data navy
                ship_details = {
                    "row": int(x),
                    "col": int(y),
                    "lon": nav[1],
                    "dir": d,
                }
                #insert navy on board
                verifier, message = game.place_ship_on_board(player, ship_details )
                if not(verifier):
                    print(f"ERROR, {message}")
                else:
                    repetir = False
                print()
                print()
                print()
                print()
                print()
                print()
    game.print_board("1")
    print()
    game.print_board("2")
    print()
    print()
    print()
    print()
    winner_player = ""
    atacante = "1"
    while winner_player == "":
        print(f"Jugador {atacante} ataca")
        repetir = True
        while repetir:
            correcto = False
            while not(correcto):
                x = input("Fila: ")
                if validations(x, "coordenada"):
                    correcto = True
                else:
                    print(f"ERROR {y} no es un numero de 0 al 9")
            correcto = False
            while not(correcto):
                y = input("Columna: ")
                if validations(y, "coordenada"):
                    correcto = True
                else:
                    print(f"ERROR {y} no es un numero de 0 al 9")
            
            result = game.atack(int(x), int(y), atacante)
            if result == "AGUA!!!!":
                print("AGUA!!!!")
                repetir = False
            elif result == "repetido":
                print("Ya atacaste esa casilla")
            else:
                print("BARCO!!!!")
                repetir = False
            
        if atacante == "1":
            atacante = "2"
        else:
            atacante = "1"
        print()
        print()
        print()
        print()
        print()
        print()
        print(f"Tablero del jugador {atacante}")
        game.print_board(atacante)
        print()
        print()
        print()
        print()
        print()
        print()
        if result == "1":
            winner_player = "1"
        elif result == "2":
            winner_player = "2"
    print(f"El ganador es el jugador {winner_player}")
        

