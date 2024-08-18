
class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        """
        Overwrites the add magic method. Called to implement the operator '+'. x is the object added to this class
        """
        temp = Distance()  # we'll use the same class object to contain measurement attributes
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __str__(self):
        """
        So we can overwrite the string of the object. Which print
        """
        return f"{self.ft}ft {self.inch}in"


if __name__ == "__main__":
    d1 = Distance(5, 8)  # 5 feet 8 inches
    d2 = Distance(3, 7)  # 3 feet 7 inches

    d3 = d1 + d2 # Add distances
    print(d3)  # Output: 9ft 3in
