from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    # question_text: ���� ������ �����ϴ� �ʵ�. �ִ� ���̴� 200��.
    question_text = models.CharField(max_length=200)
    
    # pub_date: ������ �Խõ� ��¥�� �ð��� �����ϴ� �ʵ�.
    # "date published"�� ����� ���� �� �ִ� �ʵ� �̸�(human-readable name).
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        # __str__ �޼���� ��ü�� ���ڿ��� ǥ���ϴ� ����� �����ϴ� �޼���.
        # Question �𵨿����� question_text �ʵ� ���� ��ȯ�ϵ��� ����.
        # �̸� ���� ������ �������� �п��� ��ü�� ���������� Ȯ��.
        return self.question_text

    def was_published_recently(self):
        # was_published_recently�� ������ �ֱ�(�Ϸ� �̳�)�� �ԽõǾ����� ���θ� Ȯ���ϴ� �޼���.
        # timezone.now(): ���� �ð��� �������� �Լ� (Django���� �ð��� �ν��� ����).
        # datetime.timedelta(days=1): �Ϸ�(1��)�� �ð� ������ ���.
        # pub_date >= (���� �ð� - 1��): ������ �Խõ� ��¥(pub_date)�� �Ϸ� �̳����� Ȯ��.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # question: Choice ���� Question �𵨰� ����Ǵ� �ܷ� Ű.
    # ForeignKey�� ����Ͽ� �ٴ��� ���踦 ����.
    # on_delete=models.CASCADE: ����� Question�� �����Ǹ� �ش� Choice�� �����ǵ��� ����.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    # choice_text: ������ ������ �����ϴ� �ʵ�. �ִ� ���̴� 200��.
    choice_text = models.CharField(max_length=200)
    
    # votes: �������� ���� ��ǥ ���� �����ϴ� �ʵ�. �⺻���� 0.
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        # __str__ �޼���� Choice ��ü�� ���ڿ��� ǥ���ϴ� ����� �����ϴ� �޼���.
        # Choice �𵨿����� choice_text �ʵ� ���� ��ȯ�ϵ��� ����.
        return self.choice_text
