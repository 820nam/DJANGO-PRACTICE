from django.shortcuts import render  # render 함수 임포트: 템플릿을 렌더링하여 HTML로 반환하는 역할

# Create your views here.  # Django가 기본으로 제공하는 주석: 뷰 함수를 여기에 작성하라는 의미

# index 함수: 특정 URL에 대해 처리할 로직 정의
def index(request):  
    # 요청(request)이 들어오면 'board/index.html' 템플릿을 렌더링하여 응답으로 반환
    return render(request, 'board/index.html')  

from .models import Board  # Board 모델 임포트: 데이터베이스에서 게시글 데이터를 가져오기 위해 사용

# list 함수: 게시판 목록을 렌더링하는 뷰
def list(request):
    board_list = Board.objects.all()  # Board 모델의 모든 객체(게시글) 데이터를 가져옴
    context = {
        'board_list': board_list,  # 가져온 게시글 데이터를 템플릿에 전달하기 위한 딕셔너리
    }
    return render(
        request,
        'board/list.html',  # 렌더링할 템플릿 파일 경로
        context  # 템플릿에 전달할 데이터
    )
    
    
def read(request, id):
    board = Board.objects.get(pk=id)
    board.incrementReadCount() #조회수 count
    return render(request, 'board/read.html', {'board':board})
