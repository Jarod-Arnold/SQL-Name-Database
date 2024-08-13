class Name:
    """
    This method initializes the Name object with the name, year, name count, and gender variables.
    """
    def __init__(self, name, year, name_count, gender):
        self.name = name
        self.year = year
        self.name_count = name_count
        self.gender = gender

    @staticmethod
    def from_tuple(record):
        """
        Creates a Name object from a tuple
        """
        return Name(record[0], record[1], record[2], record[3]) # returns the specified indexes (year, name, gender, name count)
