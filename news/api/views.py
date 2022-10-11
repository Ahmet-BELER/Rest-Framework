
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article , Author
from .serializers import ArticleSerializers,AuthorSerializer
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class AuthorListCreateView(APIView):
    def get(self,request):
        author = Author.objects.all()
        serializer=AuthorSerializer(author, many=True ,context={'request': request})
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ArticleListCreateView(APIView):
    def get(self,request):
        article = Article.objects.filter(active=True)
        serializer=ArticleSerializers(article, many=True )
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer=ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class ArticleDetailAPIView(APIView):
    
    def get_object(self,id):
        article_instance = get_object_or_404(Article,id=id)
        return article_instance
    
    def get(self,request, id):
        article=self.get_object(id=id)  
        serializer =ArticleSerializers(article)
        return Response(serializer.data)
        
    def put(self,request, id):
        article=self.get_object(id=id)   
        serializer =ArticleSerializers(article , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        article=self.get_object(id=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
