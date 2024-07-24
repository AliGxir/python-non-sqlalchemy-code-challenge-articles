class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("title must be in string format")
        elif hasattr(self, "_title"):
            raise ValueError("title cannot be reset")
        elif len(title) not in range(5, 51):
            raise ValueError("title must be in between 5-50 char")
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be from Author class")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be from Magazine class")
        self._magazine = magazine


class Author:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("names must be in string format")
        elif hasattr(self, "_name"):
            raise ValueError("name cannot be reset")
        elif not len(name) > 0:
            raise ValueError("name must be longer than 0 char")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        topics = list(
            {
                article.magazine.category
                for article in Article.all
                if article.author is self}
        )
        if len(topics) == 0:
            return None
        return topics


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be in string format")
        elif len(name) not in range(2, 17):
            raise ValueError("name must be between 2-16 char")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("category must be in string format")
        elif not len(category) > 0:
            raise ValueError("category must be between 2-16 char")
        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if len(titles) == 0:
            return None
        return titles

    def contributing_authors(self):
        contributors = []
        authors = [article.author for article in self.articles()]
        for author in set(authors):
            if authors.count(author) > 2:
                contributors.append(author)
        if len(contributors) == 0:
            return None
        return contributors

    def top_publisher():
        all_publisher = [magazine for magazine in Magazine.all]
        if len(Article.all) == 0:
            return None
        return max(all_publisher, key=lambda magazine: len(magazine.articles()))
        # max_count = 0
        # max_publisher = None
        # for magazine in Magazine.all:
        #     if len(magazine.articles()) > max_count:
        #         max_count = len(magazine.articles())
        #         max_publisher = magazine
        # return max_publisher
