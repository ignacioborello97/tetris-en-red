from ..block.block import Block

class Piece:
    templates = {
        'S':[
            ['.....'
            ,'..S..'
            ,'..SS.'
            ,'...S.'
            ,'.....'],
            ['.....'
            ,'..SS.'
            ,'.SS..'
            ,'.....'
            ,'.....']
        ],
        'Z':[
            ['.....'
            ,'...Z.'
            ,'..ZZ.'
            ,'..Z..'
            ,'.....'],
            ['.....'
            ,'.ZZ..'
            ,'..ZZ.'
            ,'.....'
            ,'.....']
        ],
        'L':[
            ['.....'
            ,'..L..'
            ,'..L..'
            ,'..LL.'
            ,'.....'],
            ['.....'
            ,'.....'
            ,'.LLL.'
            ,'.L...'
            ,'.....'],
            ['.....'
            ,'.LL..'
            ,'..L..'
            ,'..L..'
            ,'.....'],
            ['.....'
            ,'...L.'
            ,'.LLL.'
            ,'.....'
            ,'.....']
        ],
        'J':[
            ['.....'
            ,'..J..'
            ,'..J..'
            ,'.JJ..'
            ,'.....'],
            ['.....'
            ,'.J...'
            ,'.JJJ.'
            ,'.....'
            ,'.....'],
            ['.....'
            ,'..JJ.'
            ,'..J..'
            ,'..J..'
            ,'.....'],
            ['.....'
            ,'.JJJ.'
            ,'...J.'
            ,'.....'
            ,'.....']
        ],
        'T':[
            ['.....'
            ,'.....'
            ,'.TTT.'
            ,'..T..'
            ,'.....'],
            ['.....'
            ,'..T..'
            ,'.TT..'
            ,'..T..'
            ,'.....'],
            ['.....'
            ,'..T..'
            ,'.TTT.'
            ,'.....'
            ,'.....'],
            ['.....'
            ,'..T..'
            ,'..TT.'
            ,'..T..'
            ,'.....']
        ],
        'I':[
            ['.....'
            ,'.....'
            ,'.IIII'
            ,'.....'
            ,'.....'],
            ['.....'
            ,'..I..'
            ,'..I..'
            ,'..I..'
            ,'..I..']
        ],
    }

    """
        Constructor de la clase Piece:
            @param shape = 'S'| 'Z'| 'L'| 'J'| 'T'| 'I' -- indica que tipo de pieza es y se utiliza para tomar el array de posiciones posibles que puede tomar la pieza
            @param x -- indica la posicion en la fila con la que se va a trackear la pieza (se puede asumir que es el bloque del medio)
            @param y -- indica la posicion en la columna con la que se va a trackear la pieza (se puede asumir que es el bloque del medio)
    """
    def __init__(self, shape, x = 5, y = 0):
        self.shape = shape
        self.x = x
        self.y = y
        self.rotation = 0
        self.template = Piece.templates[shape][abs(self.rotation % len(Piece.templates[self.shape]))]
        self.blocks = self.calculate_blocks()

    def rotate_clock(self):
        self.rotation += 1
        self.template = Piece.templates[self.shape][abs(self.rotation % len(Piece.templates[self.shape]))]
        self.blocks = self.calculate_blocks()

    def rotate_unclock(self):
        self.rotation -= 1
        self.template = Piece.templates[self.shape][abs(self.rotation % len(Piece.templates[self.shape]))]
        self.blocks = self.calculate_blocks()

    def calculate_blocks(self):
        lista = []
        
        for y, y_string in enumerate(self.template, start = 0):
            for x, x_char in enumerate(y_string, start = 0):
                if(x_char != '.'):
                    lista.append(Block(self.x + x - 1, self.y + y - 1))
        
        self.blocks = lista
        return lista

    def check_state(self, positions):
        accupied_positions = []
        for _ in positions:
            for x, y, symbol in _:
                if(symbol != '.'):
                    accupied_positions.append((x, y))
        for block in self.calculate_blocks():
            if((block.x, block.y) in accupied_positions):
                return False
            elif( block.y >= len(positions) or block.y <= -1 or block.x >= len(positions[0]) or block.x <= -1):
                return False
        return True
        
                
        


        