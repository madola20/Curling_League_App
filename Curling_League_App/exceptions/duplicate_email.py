class DuplicateEmail(Exception):

    def __init__(self, the_email):
        print("That email already exists!")