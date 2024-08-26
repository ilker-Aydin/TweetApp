from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required #giriş yapmayan kullanıcının goremiycegi seyler için
from django.contrib.auth.forms import UserCreationForm #kullanıcı olstrmak için sınıf temelli yapıcaz bunu import etmemiz gerekio video 256 dan detyalara bakablrsn 
from django.views.generic import CreateView #bu class formlrını kullanabilmek için gorunum olusturmayıdda import ettikS

# Create your views here.
def listtweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dictionary={"tweets":all_tweets}
    return render(request,'tweetapp/listtweet.html',context=tweet_dictionary)
@login_required(login_url="/login")#bunu yapınca burayı sadece giriş yapan kullanıcılar kullanabiliyo ve giriş yapmayan kullanıcılar bunu yapmaya calısıtgında login sayfasına yonlendirmesi için paranytez içindekileri yazdık
def addtweet(request):
    if request.POST:
        #nickname=(request.POST["nick name"])#bu sayede html e açtgmz formda kullanıcının girdigi nickname ve messageyi alabiliyoruz,258.videodan sonra buna ihtiyacmz kalmıo kullanıcı zaten giriş yapmış olcak cunku
        message=(request.POST["message"])
        models.Tweet.objects.create(username=request.user,message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request,'tweetapp/addtweet.html')

def addtweetbyform(request):
    if request.method=="POST":
        form=AddTweetForm(request.POST)#forms un guzelliklerinden direkt requestPOST vererek yani bana gelen istegi vererek hazır bir dolu şekilde olusturabiliyorum
        if form.is_valid():#bu eger form gecerliyse demek
            nickname=form.cleaned_data["nickname_input"]
            message=form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error in form")
            return render(request,'tweetapp/addtweetbyform.html',context={"form":form})
    else:
        form=AddTweetForm()#htmlinde bunun oldugunu belirtebilmek için bunu yapmamız ve contexte belirtmemiz gerekir
        return render(request,'tweetapp/addtweetbyform.html',context={"form":form})

def addtweetbymodelform(request):
     if request.method=="POST":
        form=AddTweetModelForm(request.POST)#forms un guzelliklerinden direkt requestPOST vererek yani bana gelen istegi vererek hazır bir dolu şekilde olusturabiliyorum
        if form.is_valid():#bu eger form gecerliyse demek
            nickname=form.cleaned_data["nickname"]
            message=form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error in form")
            return render(request,'tweetapp/addtweetbymodelform.html',context={"form":form})
     else:
        form=AddTweetModelForm()#htmlinde bunun oldugunu belirtebilmek için bunu yapmamız ve contexte belirtmemiz gerekir
        return render(request, 'tweetapp/addtweetbymodelform.html',context={"form":form})
@login_required
def DeleteTweet(request,id):
    tweet=models.Tweet.objects.get(pk=id)
    #aslnda artk burda sileblrz tweeti ama ben daha guvenli olması için tekrar kontrol edicem
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect(reverse('tweetapp:listtweet'))#şimdi bunu urls.py ye tanımlıcaz

class SignUpView(CreateView):
    form_class=UserCreationForm #hangi formu kullanıcagımızı belirtiyoruz
    success_url=reverse_lazy("login")#eger firiş başarılı olursa nereye yonlendircegimzi giriyoruz#her reverse yaptgmzda bzm için hesaplanıo ama kullanıcı bunu bir kez kullanıcak o yuzden biraz gereksiz cok kullanılmaz bu yuzden revrse_lazy import edp onu kullanıız u sayede sadece buraya ulaşıldıgında hesaplanır surekli boosu bosuna hesaplanmaz bu yzuden reverse yerine reverse_lazy kullandık
    template_name="registration/signup.html"#html mizi veriyoruz

