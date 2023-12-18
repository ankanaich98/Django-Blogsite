from django.shortcuts import render,redirect
from .models import PostModel,PostSection
from .forms import PostModelForm,PostUpdateForm,CommentForm,PostApproveForm,PostSectionForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.forms import inlineformset_factory

# Create your views here.
# Creating a new post is here


@login_required
def index(request):
    # posts = PostModel.objects.all()
    posts = PostModel.objects.filter(is_approved=True)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


@login_required
@user_passes_test(lambda user: user.is_authenticated and user.profilemodel.role == 'ADMIN')
def approvePost(request):
    posts = PostModel.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/approve_post.html', context)

# @login_required
# def index(request):
#     posts = PostModel.objects.all()
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             return redirect('blog-index')
#     else:
#         form = PostModelForm
#     form = PostModelForm()
#     context = {
#         'posts':posts,
#         'form':form
#     }
#     return render(request, 'blog/index.html',context)

@login_required
def newPost(request):
    # post = PostModel.objects.get(pk=post_id)
    template_name = 'blog/new_post.html'

    SectionFormSet= inlineformset_factory(PostModel,PostSection,fields = ('content','image',),extra=1,can_delete=False)

    if request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)
        post_instance = form.save(commit=False)
        formset = SectionFormSet(request.POST, request.FILES,instance=post_instance)
        if formset.is_valid() and form.is_valid():
            post_instance.author = request.user
            post_instance.save()
            # post_instance = form.save(commit=False)
            # post_instance.author = request.user
            # post_instance.save()

            # instances = formset.save(commit=False)
            # for instance in instances:
            #     instance.post_model = post_instance
            #     # print('saving')
            #     # print(formset)
            #     instance.save()
            formset.save()
            messages.success(request, 'Your post is awaiting approval.')
            return redirect('blog-index')
        elif form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.author = request.user
            post_instance.save()
            messages.success(request, 'Your post is awaiting approval.')
            return redirect('blog-index')
    form = PostModelForm()
    formset = SectionFormSet(instance=None)
    return render(request, template_name, {
        'formset': formset,
        'form': form,
    })

#main

# @login_required
# def newPost(request):
#     if request.method == 'POST':
#         form = PostModelForm(request.POST,request.FILES)
#         s_form = PostSectionForm(request.POST,request.FILES)
#         if form.is_valid() and s_form.is_valid:
#             post_instance = form.save(commit=False)
#             post_instance.author = request.user
#             post_instance.save()


#             # instances = formset.save(commit=False)
#             # for instance in instances:
#             #     instance.post_model = post_instance
#             #     instance.save()
#             section_instance = s_form.save(commit=False)
#             section_instance.post_model = post_instance  # Associate with the PostModel instance
#             section_instance.save()
#             messages.success(request, 'Your post is awaiting approval.')
#             return redirect('blog-index')
#     else:
#         form = PostModelForm()
#         s_form = PostSectionForm()
#     context = {'form': form,
#             #    'formset': formset
#                's_form':s_form
#                }

#     return render(request, 'blog/new_post.html', context)

@login_required
def my_posts(request):
 # Retrieve posts associated with the logged-in user
    posts = PostModel.objects.filter(author=request.user)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/user_posts.html', context)




@login_required
@user_passes_test(lambda user: user.is_authenticated and user.profilemodel.role == 'ADMIN')
def approve_post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    PostSectionFormSet = inlineformset_factory(PostModel, PostSection, fields=('content', 'image',), extra=0,can_delete=False)
    formset = PostSectionFormSet(instance=post)
    if request.method == 'POST':
        form = PostApproveForm(request.POST, instance=post)
        if form.is_valid():
            messages.success(request,'Post status has been updated.')
            form.save()
            return redirect('approve-post')
    else:
        form = PostApproveForm(instance=post)
    context = {
        'post':post,
        'form':form,
        'formset':formset
    }
    return render(request, 'blog/approve_post_details.html',context)
    
    # if request.method == 'POST':
    #     pa_form = PostApproveForm(request.POST, instance=post)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('approve-post-detail', pk = post.id)
    # else:
    #     form = PostApproveForm(instance=post)
    # context = {
    #     'post':post,
    #     'form':form,
    # }
    # return render(request, 'blog/approve_post.html',context)



@login_required
def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    PostSectionFormSet = inlineformset_factory(PostModel, PostSection, fields=('content', 'image',), extra=0,can_delete=False)
    formset = PostSectionFormSet(instance=post)

    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect ('blog-post-detail',pk=post.id)
    else:
        c_form = CommentForm()


    context = {
        'post':post,
        'c_form':c_form,
        'formset':formset
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def post_edit(request,pk):
    post = PostModel.objects.get(id=pk) 
    PostSectionFormSet = inlineformset_factory(PostModel, PostSection, fields=('content', 'image',), extra=0,can_delete=False)
    
    if request.method == 'POST':
        formset = PostSectionFormSet(request.POST,request.FILES or None,instance=post)
       
        form = PostUpdateForm(request.POST,request.FILES or None, instance=post)
        if form.is_valid() and formset.is_valid() :
            messages.success(request,'Post edit successful.')
            form.save()
            formset.save()
            
            return redirect('blog-post-detail', pk =post.id)   
        # else:
        #     print(formset.errors)
        #     messages.success(request,'Post edit not done.')  
        #     return redirect('blog-post-detail', pk =post.id)   
    else:
        
        form = PostUpdateForm(instance=post)
        formset = PostSectionFormSet(instance=post)
    context = {
        'post':post,
        'form':form,
        'formset':formset
    }
    return render(request, 'blog/post_edit.html',context)

@login_required
def post_delete(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        messages.success(request,'Post deleted successfully.')
        post.delete()
        return redirect('my-posts')
    context = {
        'post': post,
    }
    return render(request, 'blog/post_delete.html',context)


