from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.conf import settings  # Add this import

# Create your views here.

def vishnu(request):
    return HttpResponse('<h2>Hello vishnu</h2>')



def login_page(request):
     template = loader.get_template('login_entry_page.html')
     return HttpResponse(template.render())
# def login_page1(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if 'last_activity' not in request.session:
#             # Session has expired or doesn't exist
#                  return redirect('login')  # Redirect to login page
#             last_activity = request.session['last_activity']
#             now = timezone.now()
#             session_timeout = settings.SESSION_COOKIE_AGE

#             if (now - last_activity).seconds > session_timeout:
#                 # Session has expired due to inactivity
#                 del request.session['last_activity']
#                 return redirect('login')  # Redirect to login page
#             else:
#                 # Update last activity timestamp
#                 request.session['last_activity'] = now
#             # return HttpResponse('<h2>Hello vishnu</h2>')
#             # login(request, user)
#             # return redirect('/admin/login/?next=/admin/ ')  # Redirect to admin page
#         else:
#             # return HttpResponse('<h2>Hello vishnu1</h2>')
#             return render(request, 'login_entry_page.html', {'error_message': 'Invalid credentials'})
#     else:
#         # return HttpResponse('<h2>Hello vishnu2</h2>')
#         return render(request, 'login_entry_page.html')

# def login_page1(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#              # Check session expiration
#             if 'last_activity' not in request.session:
#                 # Session has expired or doesn't exist
#                 # return redirect('login')  # Redirect to login page
#                 return HttpResponse('<h2>Hello vishnu</h2>')

#             last_activity = request.session['last_activity']
#             now = timezone.now()
#             session_timeout = settings.SESSION_COOKIE_AGE

#             if (now - last_activity).seconds > session_timeout:
#                 # Session has expired due to inactivity
#                 del request.session['last_activity']
#                 # return redirect('login')  # Redirect to login page
#                 return HttpResponse('<h2>Hello vishnu</h2>')
#             else:
#                 # Update last activity timestamp
#                 request.session['last_activity'] = now



#             # Authentication successful
#             # pass  # Add any additional logic for successful authentication here
            
#         else:
#             # Authentication failed
#             return render(request, 'login_entry_page.html', {'error_message': 'Invalid credentials'})

   

#     # Render the login page
#     return render(request, 'login_entry_page.html')


def login_page1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check session expiration
            if 'last_activity' not in request.session:
                # Session has expired or doesn't exist
                return redirect('login')  # Redirect to login page

            last_activity = request.session['last_activity']
            now = timezone.now()
            session_timeout = settings.SESSION_COOKIE_AGE

            if (now - last_activity).seconds > session_timeout:
                # Session has expired due to inactivity
                del request.session['last_activity']
                return redirect('login')  # Redirect to login page
            else:
                # Update last activity timestamp
                request.session['last_activity'] = now

            # Authentication successful, redirect to a success page
            return redirect('success')  # Redirect to success page
        else:
            # Authentication failed, render login page with error message
            return render(request, 'login_entry_page.html', {'error_message': 'Invalid credentials'})

    # Render the login page
    return render(request, 'login_entry_page.html')