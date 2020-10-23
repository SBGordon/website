from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def view(request, page, pk=None, page_number=1):
    if page == 'blog' or page == 'projects':
        lst = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        flist = lst.filter(category = page.capitalize())
        start = 6*(page_number-1)
        end = start + 6
        posts = flist[start:end]
        older = page_number + 1
        newer = page_number - 1
        
        return render(request, 'blog/'+page+'.html', {'posts' : posts, 'newer' : str(page_number - 1), 'older' : str(page_number + 1),'page_number' : page_number})
    
    elif page == "project_detail":
        project = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/project_detail.html', {'project': project})
        
    elif page == "contact":
        return render(request, 'blog/contact.html')

