from django.db import models
from django.contrib.auth.models import User #kullanıcının ismini fln alabilmek için

# Create your models here.
class Tweet(models.Model):
    #nickname=models.CharField(max_length=50) artık kullanıcılar giriş yaparak tweet attıgı için buna ihtiuyacım yok 258.video
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)#burda user modelinden farklı odelle ilişki kurabilmek için foregn key kullandık User ı kullanıcagımızı soyledik bi gun bu kullanıcıyı sşilersem tweetlerininde silinmesi için ondeletecascate verdik ve null verdik ve migrationları yapcaz
    message=models.CharField(max_length=100)

    def __str__(self):
        #return f"Tweet nick : {self.nickname},Tweet message:{self.message}"
        return f"Tweet user : {self.username},Tweet message:{self.message}"



