
class DuplicateOid(Exception):

   def __init__(self, the_oid):
      print("That already exists!")