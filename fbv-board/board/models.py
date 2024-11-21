from django.db import models  # Django의 데이터베이스 모델 모듈 임포트
from django.utils import timezone  # 시간 관련 유틸리티를 위해 임포트

# 게시판 모델 정의
class Board(models.Model):
    title = models.CharField(max_length=50)  # 제목: 최대 50자 제한
    writer = models.CharField(max_length=30)  # 작성자: 최대 30자 제한
    content = models.TextField()  # 본문: 글자 수 제한 없음
    regdate = models.DateTimeField(auto_now=timezone.now)  # 작성 시간: 자동으로 현재 시간 저장
    readcount = models.IntegerField(default=0)  # 조회수: 기본값 0

    # 객체를 문자열로 표현할 때 사용 (예: 제목, 작성자, 조회수를 표시)
    def __str__(self):
        return '%s. %s(%d)' % (self.title, self.writer, self.readcount)
    
    # 조회수를 증가시키는 메서드
    def incrementReadCount(self):
        self.readcount += 1  # 조회수 1 증가
        self.save()  # 변경 사항 저장