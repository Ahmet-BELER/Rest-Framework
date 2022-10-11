from django.urls import path
from .views  import ArticleListCreateView,ArticleDetailAPIView,AuthorListCreateView


urlpatterns = [
  
    path('author/', AuthorListCreateView.as_view(), name='author_list_create' ),
    path('article/', ArticleListCreateView.as_view(), name='article_list_create' ),
    path('article/<int:id>', ArticleDetailAPIView.as_view(), name='article-detay' ),
]
 