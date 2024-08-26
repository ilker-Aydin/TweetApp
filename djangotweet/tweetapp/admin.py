from django.contrib import admin
from tweetapp.models import Tweet

#buna customazationdan baktk.
class TweetAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Nickname Group',{"fields":["nickname"]}),
        ('Message Group',{"fields":["message"]})
    ]#diyelmki bir suru gup var bii finansallar biri cografiler bur sekilde gruplara ayırabiliyoruz 
#fields = ['nickname','message']#buraya adminde hangilerini gormek istedigimizi yazıyoruz

admin.site.register(Tweet,TweetAdmin)


#admin sayfasında isim ve şifre olsturmak için pythonmanage.py createsuperuser yaparz terminale.olstrduktan sonra sitemizde admin sayfasından giriş yapablrz
# Register your models here.
#admin.site.register(Tweet) normade bunu yapmamız yeterli biz ozelleştirdik#bunu yaptıgımızda tweetleri admin tarafında gormeye başlarım
#ozelleştrmk istersen ggoogleye djangoadmin cutomasation yaz 

