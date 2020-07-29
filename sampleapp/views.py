from django.shortcuts import render,redirect
from django.core.paginator import Paginator

def main(request):
    blog_all = Blogapp.objects.all().order_by('-id') #쿼리셋, 객체목록 가져오기
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_all,2)
    #블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    # blog_all = blog.all()
    return render(request,'main.html',{'posts':posts})
# Create your views here.
def upload(request):
    return render(request,'upload.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('/myprofile/profile/')

def profile(request):
    profile=Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})

