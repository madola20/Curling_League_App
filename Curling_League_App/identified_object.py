from copy import deepcopy


class IdentifiedObject:
    oid = 0

    def __init__(self, oid):
       """Constructor for IdentifiedObject class
       Args:
           _oid: the object id number
       """
       self.oid = oid

    def get_oid(self):
        """Getter method
        Args:
            self: the oid passed value passed in from constructor method

        Returns:
            a copy of the oid
        """
        return deepcopy(self.oid)

    def __eq__(self, other):
        #return self.oid == other.oid
        if self is other:
            return True
        if hasattr(other, "oid"):
            return self.oid == other.oid
        else: return False




    def __hash__(self):
        return hash(self.oid)

