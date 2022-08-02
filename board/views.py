from django.shortcuts import render, redirect
from .models import Board, Reply
from django.utils import timezone # 현재시간구하는데 특화
from django.core.paginator import Paginator  # 대문자기 때문에 class 이다

# Create your views here.
def index(request):
    pg = request.GET.get("page", 1)
    cate = request.GET.get("cate", "")
    kw = request.GET.get("kw", "")


    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()
        elif cate == "con":
            b = Board.objects.filter(content__contains=kw)
        else:
            b = Board.objects.none()
    else:
        b = Board.objects.all()

    b = b.order_by("-pubdate")  # 앞에 -가 있으면 시간 최신순

    pag = Paginator(b, 2)
    obj = pag.get_page(pg)
    
    context = {
        "bset" : obj,
        "kw" : kw,
        "cate" : cate
    }
    return render(request, 'board/index.html', context)



def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()  # 역참조 지시자
    context = {
        "b" : b,
        "rset" : r
    }
    return render(request, 'board/detail.html', context)



def creply(request, bpk):
    b = Board.objects.get(id=bpk)
    c = request.POST.get("com")
    Reply(board=b, replyer=request.user, comment=c).save()
    return redirect("board:detail", bpk)



def dreply(request, bpk, rpk):
    r = Reply.objects.get(id=rpk)
    if request.user == r.replyer:
        r.delete()
    else:
        pass # 20일차 메세지
    return redirect("board:detail", bpk)




def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        pass # 20일차에 해킹한사람 협박하자!(해킹 막고 경고메세지만 보여줘도 해킹률 줄어듬)
    return redirect("board:index")




def update(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        if request.method == "POST":
            s = request.POST.get("usub")
            c = request.POST.get("ucon")
            t = timezone.now()
            b.subject = s
            b.content = c
            b.pubdate = t
            b.save()
            return redirect("board:detail", bpk)
        context = {
            "b" : b
        }
        return render(request, 'board/update.html', context)
    else:
        return redirect('board:index')




def create(request):
    if request.method == "POST":
        s = request.POST.get("usub")
        c = request.POST.get("ucon")
        t = timezone.now()
        Board(subject=s, writer=request.user, content=c, pubdate=t).save()
        return redirect("board:index")
    return render(request, 'board/create.html')