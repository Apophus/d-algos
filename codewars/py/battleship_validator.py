def validate_battlefield(field):
    # write your magic here
	return True


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


class BattleShip:

    def __init__(self, field):
        """
        Is initialized with a 2x2 array what we call the field
        """
        
        self.field = field

    def ship_count(self):
        """
        Comes up with the total ships i.e battleship, destroyers and submarines
        """
        ...

    def battleship_count(self):
        """
        Count the number of battleships available on the board
        """
        ...
    def cruiser_count(self):
        """
        Count cruisers in the field
        """
        ...
    
    def destroyer_count(self):
        """
        Count destroyers in the field
        """
        ...

    def submarine_count(self):
        """
        Count submarines in the field
        """
        ...

    def parse_rows(self, number):

        """
        Go through the rows of the battleship
         identifying the vessels based on numbersof cells

        :param: number : int - number of cells a vessel should occupy
        """
        for i in self.field:
            ...
        ...

    def parse_columns(self):
        ...

    