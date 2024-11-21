from django.shortcuts import render  # render 함수 임포트

# Create your views here.  # Django가 기본으로 제공하는 주석: 뷰 함수를 여기에 작성하라는 의미

# index 함수: 특정 URL에 대해 처리할 로직 정의
def index(request):  
    # 요청(request)이 들어오면 'board/index.html' 템플릿을 렌더링하여 응답으로 반환
    return render(request, 'board/index.html')  
