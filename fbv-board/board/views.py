from django.shortcuts import render, redirect, reverse # render 함수 임포트: 템플릿을 렌더링하여 HTML로 반환하는 역할

# Create your views here.  # Django가 기본으로 제공하는 주석: 뷰 함수를 여기에 작성하라는 의미

# index 함수: 특정 URL에 대해 처리할 로직 정의
def index(request):  
    # 요청(request)이 들어오면 'board/index.html' 템플릿을 렌더링하여 응답으로 반환
    return render(request, 'board/index.html')  

from .models import Board  # Board 모델 임포트: 데이터베이스에서 게시글 데이터를 가져오기 위해 사용

# list 함수: 게시판 목록을 렌더링하는 뷰
def list(request):
    board_list = Board.objects.all().order_by('-id')  # Board 모델의 모든 객체(게시글) 데이터를 가져옴
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

def regist(request):  # 'regist' 함수 정의. 'request'는 클라이언트 요청을 나타냄.
    if request.method == 'POST':  # 요청 메서드가 POST인지 확인. POST는 데이터 제출에 사용됨.
        title = request.POST['title']  # POST 요청에서 'title' 데이터를 가져옴.
        writer = request.POST.get('writer')  # POST 요청에서 'writer' 데이터를 가져옴(get 메서드를 사용해 KeyError 방지 가능).
        content = request.POST['content']  # POST 요청에서 'content' 데이터를 가져옴.
        
        # Board 모델 객체 생성 및 저장. title, writer, content 값 설정 후 데이터베이스에 저장.
        Board(title=title, writer=writer, content=content).save()
        
        # 데이터 저장 후 'board:list' URL로 리다이렉트. 'reverse'는 URL 네임스페이스를 사용해 URL 문자열을 생성함.
        return redirect(reverse('board:list'))
    else:  # 요청 메서드가 POST가 아닌 경우
        # 'board/regist.html' 템플릿을 렌더링하여 응답으로 반환.
        return render(request, 'board/regist.html')


def edit(request, id):  # 사용자가 게시글을 수정하기 위해 요청을 보낼 때 호출되는 함수
    board = Board.objects.get(pk=id)  # 주어진 id를 기반으로 Board 객체를 데이터베이스에서 가져옴
    if request.method == 'POST':  # 요청 메서드가 POST인 경우 (즉, 폼 데이터 제출)
        board.title = request.POST['title']  # POST 데이터에서 제목(title)을 가져와 board 객체에 할당
        board.writer = request.POST.get('writer')  # 작성자(writer) 데이터를 가져와 board 객체에 할당
        board.content = request.POST['content']  # 내용(content)을 가져와 board 객체에 할당
        board.save()  # 변경된 board 객체를 데이터베이스에 저장
        return redirect(reverse('board:read', args=(id,)))  # 수정된 게시글 보기 페이지로 리다이렉트
    else:  # 요청 메서드가 GET인 경우 (즉, 폼 페이지를 처음 요청할 때)
        return render(request, 'board/edit.html', {'board': board})  # 수정 폼 페이지를 렌더링하며 기존 데이터를 전달


def remove(request, id):  # 사용자가 게시글을 수정하기 위해 요청을 보낼 때 호출되는 함수
    board = Board.objects.get(pk=id)  # 주어진 id를 기반으로 Board 객체를 데이터베이스에서 가져옴
    if request.method == 'POST':  # 요청 메서드가 POST인 경우 (즉, 폼 데이터 제출)
        board.delete()
        return redirect(reverse('board:list'))  # 수정된 게시글 보기 페이지로 리다이렉트
    else:  # 요청 메서드가 GET인 경우 (즉, 폼 페이지를 처음 요청할 때)
        return render(request, 'board/remove.html', {'board': board})  # 수정 폼 페이지를 렌더링하며 기존 데이터를 전달
