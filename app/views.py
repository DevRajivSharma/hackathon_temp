import cloudinary.uploader
from django.shortcuts import render
from .models import my_user

def index(request):
    message = ''
    if request.method == 'POST' and request.FILES.get('profile_image'):
        data = request.POST
        image = request.FILES['profile_image']

        # Upload to 'media/user_profile/' in Cloudinary
        # upload_result = cloudinary.uploader.upload(image, folder='media/user_profile')

        # Save Cloudinary image URL in DB
        user = my_user.objects.create(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            # profile_image=upload_result['url']
            profile_image=image
        )
        user.save()
        
        message = 'User created successfully!'
        return render(request, 'index.html', {'message': message},{'user': user})
    user = my_user.objects.all()
    user_data = user.values()
    return render(request, 'index.html',{'user': user_data})
