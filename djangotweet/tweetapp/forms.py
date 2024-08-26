#şuan aslında kullanıcıdan girdigi bilgileri alp kaydedip gene gosterebiliyoruz gene bunu yapıcaz ama buda farklı bi yolu djangonun kendi bi ozelligi
from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet
#modelse cok benzer modelsde gosterdgmz gibi charfield gibi seyler vardır daha detaylı neler var gormek için django form fields ı arastırabilirsin
#biraz once html i kendm yazdm burda yazmayacaz bile kendi yazacak html i
class AddTweetForm(forms.Form):
    nickname_input=forms.CharField(label="Nickname",max_length=50)
    message_input=forms.CharField(label="Message",max_length=100,widget=forms.Textarea(attrs={"class":"tweetmessage"}))#widgetda yazacagımız alanınn buuyuuzesi için ve gene bu textareanın ozelliigi textareadad sınıf belirtince css le ustunde oynayabiliriz
#viewste bunu gorebilmek için bi fonksiyon olusturcaz ismi addtweetbyformolsun
'''
if request.method=="POST":
        print(request.POST)
    bize bu veri geldiginde hazır bir form dosyası gibi gelecek
    else:
        return render('tweetapp:addtweetbyform.html') yazıyoruz ve dolayısıyla html olusturmamız gerekio
'''

#bu da farklı bi yontem form için MOdelsForm gordgn gibi önce import ettik sonra:
class AddTweetModelForm(ModelForm):
    class Meta:
        model= Tweet
        fields = ["username","message"]#modelde nickname ve message column olusturuluo bize buraya ordan yazıyoruz
#views.py dede bunu kaydetmemiz gerekio ve tabiki html dosyası bunları yaptım bakabilirsin nası yaptıgıma 
#bunda gordgn gibi charfield fln bi şey girmiyoruz bunda bunu kendisi yapıyo biz sadece hangi fieldların olucagını soyledik
