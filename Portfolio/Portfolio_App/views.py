from django.shortcuts import render
from Portfolio_App.forms import Response
# Create your views here.
def test(request):
    form = Response()
    submitted = False
    if request.method == 'POST':
        form = Response(request.POST)
        print(request.method)
        if form.is_valid():
            form.save()
            print('Form Validation Success and printing data')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['comment'])
            submitted = True
    my_dict ={'form':form,'submitted':submitted}
    return render(request,'home.html',my_dict)
