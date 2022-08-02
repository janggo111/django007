from django.shortcuts import render, redirect
from .models import Topic, Choice
from django.utils import timezone

# Create your views here.
def index(request):
    t = Topic.objects.all()
    context = {
        "tset" : t
    }
    return render(request, 'vote/index.html', context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, 'vote/detail.html', context)

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        bs = request.POST.getlist("bsub")
        bp = request.FILES.getlist("bpic")
        bc = request.POST.getlist("bcon")
        t = Topic(subject=s, maker=request.user, content=c, pubdate=timezone.now())
        t.save()
        for n, p, q in zip(bs, bp, bc):
            Choice(topic=t, name=n, pic=p, con=q).save()
        return redirect("vote:index")
    return render(request, 'vote/create.html')

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get('cho')
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect('vote:detail', tpk)

def cancel(request, tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(u)
    u.choice_set.get(topic=t).choicer.remove(u)
    return redirect('vote:detail', tpk)

def delete(request, tpk):
    t = Topic.objects.get(id=tpk)
    if t.maker == request.user:
        t.delete()
    else:
        pass
    return redirect("vote:index")