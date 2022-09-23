from typing import Iterable
import random

from music.adapters.repository import AbstractRepository
from music.domainmodel import *


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.name for genre in genres]
    print("Genres Names = ", genre_names)
    return genre_names


# # ============================================
# # Functions to convert dicts to model entities
# # ============================================

# def article_to_dict(article: Article):
#     article_dict = {
#         'date': article.date,
#         'title': article.title,
#         'image_hyperlink': article.image_hyperlink
#     }
#     return article_dict


# def articles_to_dict(articles: Iterable[Article]):
#     return [article_to_dict(article) for article in articles]