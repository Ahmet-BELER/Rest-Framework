from django.urls import path
from .views  import ArticleListCreateView,ArticleDetailAPIView,AuthorListCreateView,AuthorDetailView,CommentsCreateView


urlpatterns = [
  
    path('author/', AuthorListCreateView.as_view(), name='author_list_create' ),
    path('author/<int:id>', AuthorDetailView.as_view(), name='author_detail' ),
    path('article/', ArticleListCreateView.as_view(), name='article_list_create' ),
    path('article/<int:id>', ArticleDetailAPIView.as_view(), name='article-detay' ),
    path('comment/', CommentsCreateView.as_view(), name='comments_list' ),
]
 