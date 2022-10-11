from rest_framework import serializers 
from news.models import Article,Author
from datetime import datetime, date
from django.utils.timesince import timesince



class ArticleSerializers(serializers.ModelSerializer):
    time_since_pub= serializers.SerializerMethodField()
    #author= serializers.StringRelatedField()
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['id','create_date','update_date']
        


    def get_time_since_pub(self, object):
        now=datetime.now()
        pub_date = object.release_date
        if object.active == True: 
           time_delta = timesince(pub_date,now)
           return time_delta

        else:
            return "Aktif değil"

    def validate_release_date(self, datevalue):
        today=date.today()
        if datevalue > today:
            raise serializers.ValidationError('Release date cannot be greater than today')
        
        else:
            return datevalue
        
        
class AuthorSerializer(serializers.ModelSerializer):
    
    articles = ArticleSerializers(many=True, read_only=True) 
    #articles= serializers.HyperlinkedRelatedField(
        # many=True,
      #  read_only=True, 
       
       # view_name ="article-detay",
        #)
    class Meta: 
     model = Author
     fields = '__all__'
        
    
            
        
        
        
        
        
        
        
        
#### eski yöntem (serializers.Serializer) 


class ArticleDefaultSerializers(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    header= serializers.CharField()
    explanation = serializers.CharField()
    text= serializers.CharField()
    city= serializers.CharField()
    release_date= serializers.DateField()
    active= serializers.BooleanField()
    create_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    
    def create(self, valiadated_data):
         print(valiadated_data)
         return Article.objects.create(**valiadated_data)
    

    def update(self, instance, valiadated_data):
        instance.author = valiadated_data.get("author",instance.author)
        instance.header = valiadated_data.get("header",instance.header)
        instance.explanation = valiadated_data.get("explanation",instance.explanation)
        instance.text = valiadated_data.get("text",instance.text)
        instance.city = valiadated_data.get("city",instance.city)
        instance.release_date = valiadated_data.get("release_date",instance.release_date) 
        instance.active = valiadated_data.get("active",instance.active) 
        instance.create_date = valiadated_data.get("create_date",instance.create_date) 
        instance.update_date = valiadated_data.get("update_date",instance.update_date) 
        instance.save()
        return instance
    
    def validate(self,data):
        if data['header'] ==  data['explanation'] :
            raise serializers.ValidationError('header and explanation cannot be the same')
        return data
    def validate_explanation(self,value):
        
        if len(value) < 10 :
            raise serializers.ValidationError( f'explanation lengt must be at least 20 characters you input {len(value)} characters')
        return value 