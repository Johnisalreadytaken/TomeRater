class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books ={}


    def get_email(self):
        return self.email


    def change_email(self, address):
        self.email = address
        print("Email updated successfully!")


    def __repr__(self):
        return "User {name}, email: {email}, books read: {books_read}".format(
            name = self.name, 
            email = self.email, 
            books_read = len(self.books))
    

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False


    def read_book(self, book, rating=None):
        self.books[book] = rating


    def get_average_rating(self):
        sum_rating = 0.0
        count_non_none = 0.0
        for rating in self.books.values():
            if rating != None:
                sum_rating += rating
                count_non_none += 1
        avg_rating = sum_rating/count_non_none
        return avg_rating


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn  = isbn
        self.ratings = []


    def get_title(self):
        return self.title


    def get_isbn(self):
        return self.isbn


    def set_isbn(self, isbn):
        self.isbn = isbn
        print("ISBN updated successfully.")


    def add_rating(self, rating):
        if rating in range(0,5):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")


    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False


    def __hash__(self):
        return hash((self.title, self.isbn))


    def get_average_rating(self):
        sum_rating = 0.0
        count_non_none = 0.0
        for rating in self.ratings:
            if rating != None:
                sum_rating += rating
                count_non_none += 1
        avg_rating = sum_rating/count_non_none
        return avg_rating



class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author


    def get_author(self):
        return self.author


    def __repr__(self):
        return "{title} by {author}".format(
            title=self.title, 
            author=self.author)



class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level


    def get_subject(self):
        return self.subject


    def get_level(self):
        return self.level


    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(
            title = self.title,
            level = self.level,
            subject = self.subject)



class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbns_in_use=[]


    def create_book(self, title, isbn):
        if (self.validate_isbn(isbn)):
            self.isbns_in_use.append(isbn)
            return Book(title, isbn)
        else:
            print("duplicated ISBN.")
        

    def create_novel(self, title, author, isbn):
        if (self.validate_isbn(isbn)):
            self.isbns_in_use.append(isbn)
            return Fiction(title, author, isbn)
        else:
            print("duplicated ISBN.")


    def create_non_fiction(self, title, subject, level, isbn):
        if (self.validate_isbn(isbn)):
            self.isbns_in_use.append(isbn)
            return Non_Fiction(title, subject, level, isbn)
        else:
            print("duplicated ISBN.")


    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            user = self.users[email]
            user.read_book(book, rating)

            book.add_rating(rating)
        else:
            print("No user with email {0}".format(email))

        if book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1


    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("User already exists!")
            return

        if not ("@" in email and (".com" in email or ".org" in email or ".edu" in email)):
            print("Invalid email-address!")
            return

        new_user=User(name, email)
        self.users[email] = new_user

        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, new_user.email, None)


    def print_catalog(self):
        for key in self.books:
            print(key)


    def print_users(self):
        for value in self.users:
            print(value)


    def most_read_book(self):
        highest_count = 0
        for book, read_count in self.books.items():
            if highest_count < read_count:
                highest_count = read_count
        return book


    def highest_rated_book(self):
        highest_rated_book = 0

        for book in self.books.keys():
            avg_rating = book.get_average_rating()
            if highest_rated_book < avg_rating:
                highest_rated_book = avg_rating
        return book


    def most_positive_user(self):
        highest_average=0
        most_positive_user=None

        for user in self.users.values():
            average_rating=user.get_average_rating()
            if highest_average < average_rating:
                highest_average = average_rating
                most_positive_user = user
        return user


    def validate_isbn(self, isbn):
        if isbn in self.isbns_in_use:
            return False
        else:
            return True