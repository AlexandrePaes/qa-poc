# # faq/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, Page
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQ
from .forms import FAQForm


# def faq_list(request):
#     faq_list = FAQ.objects.all()
#     paginator = Paginator(faq_list, 1)  # Show 1 FAQ per page

#     page = request.GET.get('page')
#     faqs = paginator.get_page(page)
    
#     return render(request, 'faq/faq_list.html', {'faqs': faqs})


# def faq_detail(request, faq_id):
#     faq = get_object_or_404(FAQ, pk=faq_id)
#     return render(request, 'faq/faq_detail.html', {'faq': faq})


# def next_page_number(self):
#         return self.paginator.validate_number(self.number + 1)

######################################################################################

# V5 Create

@api_view(['GET', 'POST'])
def faq_create(request, index):
    question = FAQ.objects.filter().order_by('id')[index - 1]
    print('question:', question)
    print('question_id:', question.id)      
    print('question_answer:', question.answer)
    if request.method == 'POST':
        if question.id == index:
            form = FAQForm(request.POST, instance=question)
            if form.is_valid():
                form.save()                
                print('question_answer2:', type(question))
                print('question_answer2:', question)
        return redirect(f'/create/{index + 1}')
    form = FAQForm(instance=question)
    # print('form:', form)
    return render(request, 'faq/faq_create.html', {'form': form, 'index': index})


#####################################################################################

# V4

# @api_view(['GET', 'POST'])
# def faq_create(request):
#     faq_list = FAQ.objects.all().order_by('id')

#     # Get the current page number
#     page_number = request.GET.get('page', 1)

#     paginator = Paginator(faq_list, 1)  # 1 item per page
#     page_obj = paginator.get_page(page_number)

#     if request.method == 'POST':
#         form = FAQForm(request.POST or None)

#         if form.is_valid():
#             # Save the answer for the current question
#             faq = get_object_or_404(FAQ, pk=page_obj.object_list[0].pk)
#             faq.save()

#             # Redirect to the next question page
#             next_page_number = page_number + 1
#             if next_page_number <= paginator.num_pages:
#                 return redirect(f'/faq/create/?page={next_page_number}')

#     form = FAQForm()
#     return render(request, 'faq/faq_create.html', {'form': form, 'page_obj': page_obj})

########################################################################################

# # V3

# @api_view(['GET', 'POST'])
# def faq_create(request, index):
#     faq_page = FAQ.objects.filter(available=True).order_by('id')[index - 1]
#     context = {'index': index, 'faq_page': faq_page}
#     print('faq_page Type:', type(faq_page))
#     print('faq_page:', faq_page)

#     paginator = Paginator(faq_page, 1)
#     print('paginator Type:', type(paginator))
#     print('paginator:', paginator)

#     page_number = request.GET.get('page', 1)
#     print('page_number Type:', type(page_number))
#     print('page_number:', page_number)

#     page_obj = paginator.get_page(page_number)
#     print('page_obj Type:', type(page_obj))
#     print('page_obj:', page_obj)

#     next_page_number = paginator.get_page(page_number)
#     print('next_page_number Type:', type(next_page_number))
#     print('next_page_number:', next_page_number)    

#     if request.method == 'POST':
#         form = FAQForm(request.POST or None)
#         print('form:', form)
#         if form.is_valid():
#             # Get the FAQ for the current page and update the answer
#             #faq = get_object_or_404(FAQ, pk=page_obj.object_list)
#             faq = faq.save()
#             print("faq:", faq)
#             # faq.save()
#             # faq.answer = form.data['answer']
#             # faq.save()
#                 # Redirect to the next question or FAQ            
#             # if page_obj.has_next():
#             #     # return redirect(f'faq/create/{page_number}')                
#             #     # return redirect(f'/faq/create/?page={faq_page[0::]}')
#             #     next_page_number = page_number + 1
#             #     next_page_number = int(next_page_number)
#             #     print('next_page_number 2:', next_page_number)
#             #     if next_page_number <= paginator.num_pages:
#                     # return redirect(f'/faq/create/?page={next_page_number}/{paginator.page(int(page_number))}')
#             return redirect(f'/faq/create/{index + 1}')
#         return redirect(f'/faq/create/{index}')
#     form = FAQForm({'question': 'answer'})
#     return render(request, 'faq/faq_create.html', {'form': form, 'index': index}, context=context)

########################################################################################

# V2

# @api_view(['GET', 'POST'])
# def faq_create(request):
#     faq_page = FAQ.objects.all().order_by('id')
#     print('faq_page Type:', type(faq_page))
#     print('faq_page:', faq_page)

#     paginator = Paginator(faq_page, 1)
#     print('paginator Type:', type(paginator))
#     print('paginator:', paginator)

#     page_number = request.GET.get('page', 1)
#     print('page_number Type:', type(page_number))
#     print('page_number:', page_number)

#     #page_number = int(page_number)

#     page_obj = paginator.get_page(page_number)
#     print('page_obj Type:', type(page_obj))
#     print('page_obj:', page_obj)

#     next_page_number = paginator.get_page(page_number)
#     print('next_page_number Type:', type(next_page_number))
#     print('next_page_number:', next_page_number)    

#     try:
#         page_obj = paginator.page(page_number)
#     except EmptyPage:
#         # If the requested page is out of range, redirect to the last page
#         return redirect(f'{request.path_info}?page={paginator.num_pages}')

#     if request.method == 'POST':
#         form = FAQForm(request.POST or None)
#         if form.is_valid():
#             question = form.save(commit=False)
#             faq = get_object_or_404(FAQ, pk=page_obj.object_list.first('id'))

#             # Check if the answer index matches the question index
#             question_id = request.POST.get('question_id')
#             if question_id and faq.id == int(question_id):
#                 faq.answer = form.data['answer']
#                 question.save()
            
#             # Redirect to a specific URL after saving the question
#             return HttpResponseRedirect(f'/faq/faq_create.html?page={page_obj.next_page_number()}')  
        
#         return render(request, 'faq/faq_create.html', {'form': form, 'page_obj': page_obj})

#     # Handle GET request
#     return render(request, 'faq/faq_create.html', {'page_obj': page_obj})

###############################################################################

# V1

# @api_view(['GET', 'POST'])
# def faq_create(request):
#     faq_list = FAQ.objects.all().order_by('id')
#     paginator = Paginator(faq_list, 1)  # Show 1 FAQ per page
#     page_number = request.GET.get('page', 1)  # Get the page from the request, default to 1
#     page_obj = paginator.get_page(page_number)
#     next_page_number = paginator.get_page(page_obj)    

#     try:
#         page_obj = paginator.page(page_number)
#     except EmptyPage:
#         # If the requested page is out of range, redirect to the last page
#         return redirect(f'{request.path_info}?page={paginator.num_pages}')

#     if request.method == 'POST':
#         form = FAQForm(request.POST or None)
#         if form.is_valid():
#             # Get the FAQ for the current page and update the answer
#             faq = get_object_or_404(FAQ, pk=page_obj.object_list)

#             # Check if the answer index matches the question index
#             question_id = request.POST.get('question_id')
#             if question_id and faq.id == int(question_id):
#                 faq.answer = form.data['answer']
#                 faq.save()

#                 # Redirect to the next question or FAQ            
#             if page_obj.has_next():
#                 next_page_number = page_obj.next_page_number()
#                 return redirect(f'{request.path_info}?page={next_page_number}')
#             return redirect(f'{request.path_info}?page={page_number}')

#      #else:
#         # Pass the question_id to the form for rendering
#     form = FAQForm({'question_id': page_obj.object_list.first().id})

#     return render(request, 'faq/faq_create.html', {'form': form, 'page_obj': page_obj})
