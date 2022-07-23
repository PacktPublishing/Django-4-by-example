from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Course

def subdomain_course_middleware(get_response):
    """
    Subdomains for courses
    """
    def middleware(request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':
            # get course for the given subdomain
            course = get_object_or_404(Course, slug=host_parts[0])
            course_url = reverse('course_detail',
                                 args=[course.slug])
            # redirect current request to the course_detail view
            url = '{}://{}{}'.format(request.scheme,
                                     '.'.join(host_parts[1:]),
                                     course_url)
            return redirect(url)
        response = get_response(request)
        return response
    return middleware
