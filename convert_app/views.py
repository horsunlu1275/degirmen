from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import uploaded_file_form

# Create your views here.
def homePage(req):
    if req.method == 'POST':
        form = uploaded_file_form(req.POST, req.FILES)
        if form.is_valid():
            form.clean_file()
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.save()
            file_name = form.cleaned_data['file_name']
            file_extension = form.cleaned_data['file_extension']
            conversion_options = {
                'txt': ['pdf', 'docx'],
                'pdf': ['txt', 'docx'],
                'docx': ['txt', 'pdf']
                # Buraya istediğiniz diğer dönüştürme seçeneklerini ekleyebilirsiniz
            }
            options = conversion_options.get(file_extension, [])
            return render(req, 'convert_app/homePage.html', {'form': form, 'file_name': file_name, 'file_extension': file_extension, 'conversion_options': options})
    else:
        form = uploaded_file_form()
    return render(req, 'convert_app/homePage.html', {'form': form})

    
    
    
    