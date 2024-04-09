from django.shortcuts import render

# Create your views here.
def movies(request):
    head_text = '영화 블로그 프로젝트 메인 페이지'
    body_text = '영화 블로그 내용을 관리합니다.'
    context = {
        'head_text': head_text,
        'body_text': body_text
    }
    return render(request, 'movies/movies.html', context)

def create_movie(request):
    context = {
    }
    return render(request, 'movies/create_movie.html', context)