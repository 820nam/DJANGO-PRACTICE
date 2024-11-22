# Django Function-Based View 게시판

Django의 함수형 뷰(Function-Based Views, FBV)를 활용한 간단한 게시판 프로젝트입니다.

## 프로젝트 구조

### 앱 구성
- `board` 앱: 게시판 기능 담당.

### 템플릿 구조
- `base.html`: 공통 레이아웃.
- `index.html`: 메인 페이지.
- `list.html`: 게시글 목록 페이지.
- `read.html`: 게시글 상세 보기 페이지.

### 데이터베이스
- SQLite 사용.

---

## 기능 설명

### 게시글 목록 보기 (`list`)
- 작성된 게시글을 테이블 형식으로 출력.
- 제목을 클릭하면 해당 게시글의 상세 보기로 이동.

### 게시글 상세 보기 (`read`)
- 선택한 게시글의 상세 정보를 출력.
- **출력 정보**: 등록일, 조회수, 제목, 내용 등.
- 목록으로 돌아가기 버튼 제공.

### 메인 페이지 (`index`)
- 게시판 기능의 진입점.
- 게시글 목록 및 등록 링크 제공.

---

## URL 패턴

| URL                | 설명               | 연결 뷰 함수 |
|--------------------|--------------------|--------------|
| `/`                | 메인 페이지         | `index`      |
| `/list/`           | 게시글 목록 보기     | `list`       |
| `/read/<int:id>/`  | 게시글 상세 보기     | `read`       |

---

## views.py 주요 코드

### 게시글 목록 보기 (`list`)
```python
from django.shortcuts import render
from .models import Board

def list(request):
    board_list = Board.objects.all()  # 모든 게시글 가져오기
    context = {
        'board_list': board_list
    }
    return render(request, 'board/list.html', context)

