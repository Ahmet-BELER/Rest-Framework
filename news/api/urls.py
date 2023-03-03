from django.urls import path
from .views  import ArticleListCreateView,ArticleDetailAPIView,AuthorListCreateView,AuthorDetailView,CommentsCreateView,CommentsDetailView


urlpatterns = [
  
    path('author/', AuthorListCreateView.as_view(), name='author_list_create' ),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail' ),
    path('article/', ArticleListCreateView.as_view(), name='article_list_create' ),
    path('article/<int:id>', ArticleDetailAPIView.as_view(), name='article-detay' ),
    path('comment/', CommentsCreateView.as_view(), name='comments_list' ),
    path('comment/<int:pk>', CommentsDetailView.as_view(), name='comment_detail' ),
]
 