# Hotel-Booking-Application-using-Django-Apps
Django is a Python-based free and open-source web framework that follows the model-template-view (MVT) Architectural Pattern. It is maintained by the Django Software Foundation. It is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development.

- Static &  Media Files Configurations

  Files / Images upload & Display are demonstrated in this way as given below:-

 - For Model Class
 	- image = models.ImageField(upload_to='property/',null=True)

 - Urls Patterns:
   - Just Add these 2 lines in urls.py
   		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
 - For Setting
 	- Copy this codes at last lines in settings.py:
 		STATIC_URL = '/static/'
		STATICFILES_DIRS = [
    			os.path.join(BASE_DIR, "static"),    
		]

		MEDIA_URL = '/media/'
		MEDIA_ROOT = os.path.join(BASE_DIR, "static")  
 
 -  Foreign Key Relationship
   - Variable Name = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

 - Get All data from Database
    - Property.objects.all()

 - Get single data from Database
   - Property.objects.get(id=id)


