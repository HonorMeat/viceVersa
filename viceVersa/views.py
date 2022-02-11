from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'greeting':'Hello!'})
def reverse(request):
    reverse_me = request.GET['reverse_me']
    reversed = reverse_me[::-1]
    words_number = len(reverse_me.split())
    return render(request, 'reverse.html', {'reversed': reversed, 
                                            'reverse_me': reverse_me,
                                            'words_number': words_number, })