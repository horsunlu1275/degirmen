from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import uploaded_file_form

# Create your views here.
def homePage(req):
      
    if req.method == 'POST':
        form = uploaded_file_form(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = uploaded_file_form()
    return render(req, 'convert_app/homePage.html', {'form': form})

    
    
    
    