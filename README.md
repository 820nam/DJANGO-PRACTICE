Django Function-Based View 게시판
Django의 함수형 뷰(Function-Based Views, FBV)를 활용한 간단한 게시판 프로젝트입니다.

프로젝트 구조
앱 구성

board 앱: 게시판 기능을 담당.
템플릿 구조

base.html: 공통 레이아웃.
index.html: 메인 페이지.
list.html: 게시글 목록 페이지.
read.html: 게시글 상세 보기 페이지.
데이터베이스

SQLite 사용.
기능
1. 게시글 목록 보기 (list)
작성된 게시글을 테이블 형식으로 출력.
제목을 클릭하면 해당 게시글의 상세 보기로 이동.
2. 게시글 상세 보기 (read)
선택한 게시글의 상세 정보를 출력.
출력 정보:
등록일, 조회수, 제목, 내용 등.
목록으로 돌아가기 버튼 제공.
3. 메인 페이지 (index)
게시판 기능의 진입점.
게시글 목록 및 등록 링크 제공.
URL 패턴
URL	설명	연결 뷰 함수
/	메인 페이지	index
/list/	게시글 목록 보기	list
/read/<int:id>/	게시글 상세 보기	read
코드
views.py 주요 코드
list 뷰
게시글 목록을 출력하는 뷰:

python
코드 복사
from django.shortcuts import render
from .models import Board

def list(request):
    board_list = Board.objects.all()  # 모든 게시글 가져오기
    context = {
        'board_list': board_list
    }
    return render(request, 'board/list.html', context)
read 뷰
게시글 상세 정보를 출력하는 뷰:

python
코드 복사
from django.shortcuts import render, get_object_or_404
from .models import Board

def read(request, board_id):
    board = get_object_or_404(Board, id=board_id)  # 특정 게시글 가져오기
    context = {
        'board': board
    }
    return render(request, 'board/read.html', context)
템플릿
list.html
게시글 목록을 출력하는 템플릿:

html
코드 복사
<table border="1">
    <tr>
        <th>번호</th>
        <th>제목</th>
        <th>작성자</th>
        <th>조회수</th>
    </tr>
    {% for board in board_list %}
    <tr>
        <td>{{ board.id }}</td>
        <td><a href="{% url 'board:read' board.id %}">{{ board.title }}</a></td>
        <td>{{ board.writer }}</td>
        <td>{{ board.readcount }}</td>
    </tr>
    {% endfor %}
</table>
read.html
게시글 상세 정보를 출력하는 템플릿:

html
코드 복사
<table border="1">
    <tr>
        <th>등록일</th>
        <td>{{ board.regdate }}</td>
    </tr>
    <tr>
        <th>조회수</th>
        <td>{{ board.readcount }}</td>
    </tr>
    <tr>
        <th>제목</th>
        <td>{{ board.title }}</td>
    </tr>
    <tr>
        <th>내용</th>
        <td>{{ board.content }}</td>
    </tr>
</table>
<a href="{% url 'board:list' %}"><button>목록으로</button></a>
모델
models.py
게시판 데이터를 정의하는 Board 모델:

python
코드 복사
from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True)
    readcount = models.IntegerField(default=0)

    def __str__(self):
        return self.title
사용 방법
1. 프로젝트 시작
bash
코드 복사
python manage.py runserver
2. 브라우저 접속
메인 페이지: http://127.0.0.1:8000/
게시글 목록 보기: http://127.0.0.1:8000/list/
게시글 상세 보기: http://127.0.0.1:8000/read/<게시글ID>/
주요 라이브러리
Django: 4.x
SQLite: 기본 데이터베이스로 사용.
기타
이 프로젝트는 Django 함수형 뷰를 학습 및 연습하는 목적으로 작성되었습니다.
확장하려면 등록(create) 또는 수정(update) 기능을 추가해보세요!
