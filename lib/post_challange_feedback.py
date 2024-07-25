from collections import Counter
# * Article: no notes ✨
# * Author: minor refactoring 🙌🏻
# * Magazine: refactoring and top_publisher is incorrect

class Article:

    all = []

    def __init__(self, author, magazine, title):  # * PERFECT
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):  # * PERFECT
        return self._title

    @title.setter
    def title(self, title):  # * PERFECT
        if not isinstance(title, str):
            raise TypeError("title must be in string format")
        elif hasattr(self, "_title"):
            raise ValueError("title cannot be reset")
        elif len(title) not in range(5, 51):
            raise ValueError("title must be in between 5-50 char")
        self._title = title

    @property
    def author(self):  # * PERFECT
        return self._author

    @author.setter
    def author(self, author):  # * PERFECT
        if not isinstance(author, Author):
            raise TypeError("author must be from Author class")
        self._author = author

    @property
    def magazine(self):  # * PERFECT
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):  # * PERFECT
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be from Magazine class")
        self._magazine = magazine


class Author:

    def __init__(
        self, name
    ):  # * PERFECT (no need to track all authors as per challenge requirements)
        self.name = name

    @property
    def name(self):  # * PERFECT
        return self._name

    @name.setter
    def name(self, name):  # TODO little refactor
        if not isinstance(name, str):
            raise TypeError("names must be in string format")
        elif hasattr(self, "_name"):
            raise ValueError("name cannot be reset")
        elif (
            not len(name) > 0
        ):  #! could be refactored into: "elif not name" -> empty strings are falsey
            raise ValueError("name must be longer than 0 char")
        self._name = name

    def articles(self):  # * PERFECT
        return [article for article in Article.all if article.author is self]

    def magazines(self):  # * PERFECT
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):  # TODO remove unnecessary variable creation
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        # Returns a unique list of strings with the categories of the magazines the author has contributed to
        # TODO you can combine the variable creation for topics and the conditional below with the walrus
        #! YOUR CODE BELOW
        topics = list(
            {
                article.magazine.category
                for article in Article.all
                if article.author is self
            }
        )
        if len(topics) == 0: #TODO refactor to: if not topics
            return None
        return topics

        #! REFACTOR 1
        # if topics := list(
        #     {
        #         article.magazine.category
        #         for article in Article.all
        #         if article.author is self
        #     }
        # ):
        #     return topics

        #! REFACTOR 2
        #! if we have a direct way to obtain the magazines the author has contributed to
        #! why would we have to go through all the articles again?
        # TODO use a logical connector to simplify the code
        # return [magazine.category for magazine in self.magazines()] or None


class Magazine:
    all = []

    def __init__(self, name, category):  # * PERFECT
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):  # * PERFECT
        return self._name

    @name.setter
    def name(self, name):  # * PERFECT (great job using a range)
        if not isinstance(name, str):
            raise TypeError("name must be in string format")
        elif len(name) not in range(2, 17):
            raise ValueError("name must be between 2-16 char")
        self._name = name

    @property
    def category(self):  # * PERFECT
        return self._category

    @category.setter
    def category(self, category):  # TODO ALMOST PERFECT
        if not isinstance(category, str):
            raise TypeError("category must be in string format")
        elif not len(category) > 0:
            raise ValueError(
                "category must be between 2-16 char"
            )  # TODO watch out when copy/pasting
        self._category = category

    def articles(self):  # * PERFECT
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):  # * PERFECT
        return list({article.author for article in self.articles()})

    def article_titles(self):  # TODO REFACTOR
        # TODO you can combine the variable creation for topics and the conditional below with the walrus
        #! YOUR CODE BELOW
        titles = [article.title for article in self.articles()]
        if len(titles) == 0:
            return None
        return titles
        #! REFACTOR 1
        # if titles := [article.title for article in self.articles()]:
        #     return titles
        #! REFACTOR 2
        # return [article.title for article in self.articles()] or None

    def contributing_authors(self): #TODO REFACTOR
        # TODO you are currently doing 3 loops:
        # * 1. list comprehension on line: 179 -> completes before the other two start
        # * 2. for loop on line: 180 -> for each author in the first loop
        # * 3. count() on line: 181 -> you check again authors
        #! This means that the last two loops are nested -> their total times get multiplied
        #! Let's say the authors list has N authors
        #! since you have to go through it twice -> N * N = N^2
        #! You currently have quadratic time and I think we can do it in Linear Time: N
        contributors = []
        authors = [article.author for article in self.articles()] #TODO leverage the
        for author in set(authors): #! GREAT CHOICE USING A set
            if authors.count(author) > 2:
                contributors.append(author)
        #! REFACTOR THIS SECTION
        if len(contributors) == 0: #TODO usual refactor: if contributors
            return None
        return contributors
        #! INTO
        # return contributors or None

        #! REFACTOR in Linear Time using Counter or manually -> dict{[obj]: count}
        # tally = Counter(article.author for article in self.articles())
        # return [author for author, count in tally.items() if count > 2] or None

    # TODO refactor unnecessary list comprehension
    # @classmethod
    def top_publisher():  #! INCORRECT: should be a class method
        #! YOUR CODE
        all_publisher = [magazine for magazine in Magazine.all] #! unnecessary: Magazine.all creates the same list
        if len(Article.all) == 0:
            return None
        return max(all_publisher, key=lambda magazine: len(magazine.articles()))
        #! REFACTOR 1
        # if Article.all:
        # return (
        #     max(cls.all, key=lambda magazine: magazine.max_helper(), default=None)
        #     if Article.all
        #     else None
        # )
        #! REFACTOR 2
        # top_magazine = max(
        #     cls.all, key=lambda magazine: len(magazine.articles()), default=None
        # )

        # return top_magazine if top_magazine and top_magazine.articles() else None

        # max_count = 0
        # max_publisher = None
        # for magazine in Magazine.all:
        #     if len(magazine.articles()) > max_count:
        #         max_count = len(magazine.articles())
        #         max_publisher = magazine
        # return max_publisher
