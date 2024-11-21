from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    # question_text: 질문 내용을 저장하는 필드. 최대 길이는 200자.
    question_text = models.CharField(max_length=200)
    
    # pub_date: 질문이 게시된 날짜와 시간을 저장하는 필드.
    # "date published"는 사람이 읽을 수 있는 필드 이름(human-readable name).
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        # __str__ 메서드는 객체를 문자열로 표현하는 방법을 정의하는 메서드.
        # Question 모델에서는 question_text 필드 값을 반환하도록 구현.
        # 이를 통해 관리자 페이지나 셸에서 객체를 직관적으로 확인.
        return self.question_text

    def was_published_recently(self):
        # was_published_recently는 질문이 최근(하루 이내)에 게시되었는지 여부를 확인하는 메서드.
        # timezone.now(): 현재 시간을 가져오는 함수 (Django에서 시간대 인식을 포함).
        # datetime.timedelta(days=1): 하루(1일)의 시간 간격을 계산.
        # pub_date >= (현재 시간 - 1일): 질문이 게시된 날짜(pub_date)가 하루 이내인지 확인.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # question: Choice 모델이 Question 모델과 연결되는 외래 키.
    # ForeignKey를 사용하여 다대일 관계를 정의.
    # on_delete=models.CASCADE: 연결된 Question이 삭제되면 해당 Choice도 삭제되도록 설정.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    # choice_text: 선택지 내용을 저장하는 필드. 최대 길이는 200자.
    choice_text = models.CharField(max_length=200)
    
    # votes: 선택지가 받은 투표 수를 저장하는 필드. 기본값은 0.
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        # __str__ 메서드는 Choice 객체를 문자열로 표현하는 방법을 정의하는 메서드.
        # Choice 모델에서는 choice_text 필드 값을 반환하도록 구현.
        return self.choice_text
