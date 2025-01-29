from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'home.html')  # Render home.html

def start_interview(request):
    return render(request, 'start_interview.html')

def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        fs = FileSystemStorage(location='media/videos/')
        filename = fs.save(video.name, video)
        return JsonResponse({'message': 'Upload successful', 'file': filename})
    return JsonResponse({'error': 'Invalid request'}, status=400)
