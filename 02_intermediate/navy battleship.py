

class GameBoard:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

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
            board = self.player1
        else:
            board = self.player2
        for fila in board:
            print(" ".join(map(str, fila)))


class BattleshipGame(GameBoard):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def place_ship_on_board(self, assign, ship_details):
        if assign == "1": 
            board = self.player1
        else:
            board = self.player2
        row = ship_details['row']
        col = ship_details['col']
        for i in range(ship_details['lon']):
            if row > 9 or col > 9:
                return False, "El barco sale del tablero" 
            if board[row][col] == "B":
                return False, "El barco se sobre pone en otro"
            board[row][col] = "B"
            if ship_details['dir'] == "H":
                col +=1
            else:
                row +=1
        self.assign_player_board(assign,board)
        return True, "Nice"

    def atack(self, positionX, positionY):
        if self.defender == "1":
            board = self.player2()
        else:
            board = self.player1()
        
        if board[positionX][positionY] != "B":
            # failure
            board[positionX][positionY] = "X"
            
            return "AGUA!!!!"
        else:
            # navy
            board[positionX][positionY] = "O"
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
        ["Portaaviones", 5],
        ["Acorazados", 4],
        #["Cruceros", 3],
        #["Submarinos", 3],
        #["Destructores", 2],
        ]
    size = 10
    matriz1 = [["*" for _ in range(size)] for _ in range(size)]
    matriz2 = [["*" for _ in range(size)] for _ in range(size)]
    players = ["1", "2"]
    game = BattleshipGame(matriz1, matriz2)
    
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
