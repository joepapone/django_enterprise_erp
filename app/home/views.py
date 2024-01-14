from django.shortcuts import render

ABOUT_TEXT = '''
A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 

A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 
A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 
A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 

A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 
A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 


A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 
A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 
A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 



A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. A web based ERP system for best performance and reliability. 
Designed for ease of use to offer your business all the necessary tools it requires for monitoring and control. 
'''

def home(request):
    return render(request, 'home/home.html', {'description': ABOUT_TEXT})
