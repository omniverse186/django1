from django.db import models

# 질문
#질문 제목 생성일
class Question(models.Model):
    name = models.CharField('질문제목',max_length=100)
    # DateField : 날짜(년,월,일)을 저장하는 공간
    # DateTimeField : 닐짜+시간을 저장하는 공간
    date = models.DateTimeField('생성일')
    def __str__(self) : 
        return self.name
    class Meta: #모델 클래스에 정의된 변수, 테이블이름 등을 처리할 때 사용하는 클래스
        #ordering : 해당 모델 클래스에 정의된 변수 중에서 정렬에 사용할 변수 이름을 저장하는 변수
        #변수 이름만 쓴 경우 - > 오름차순              -변수 이름 -> 내림찬순
        ordering = ['-date']
# 답변
#어떤 질문에 연결되었는지 답변내용 투표수
class Choice(models.Model) :
    # ForignKey(연결한 다른 클래스) 
    # : ForeignKey 객체를 만든 모델 클래스의 객체들이 연결한 모델 클래스의 객체와 1:n 로 설정
    # Choice.q.name ->해당하는 Choice객체와 연결된 Question 객체의 name변수 값을 추출
    # on_delete : 연결된 모델클래스의 객체가 삭제 될 땨 어떻게 처리할지 저장하는 변수
    # on delete = model.PROTECT : 연결된 모든 클래스의 객체가 삭제 되지 않도록 막아줌
    # models.CASCADE : 연결된 모드클래스의 객체가 삭제되면 같이 삭제된다
    # models.set_NULL : 연결된 모델클래스의 객체가 삭제되면 아무것도 연결되지 않은 상태로 유지
    # models.SET(연결할객체 ) : 연결된 객체가 삭제 되면 매개변수 넣은 객체와 연결
    # models.set : 연결된 객체가 삭제되면 기본 설정된 객체와 연결
    #q = models.ForeignKey(Question)
    q = models.ForeignKey(Question, on_delete = models.CASCADE)
    name = models.CharField('답변항목', max_length=50)
    #IntegerField : 정수 값을 저장하는 공간
    #default : 모델클래스의 객체 생성시 해당 저장공간에 기본값 설정
    votes = models.IntegerField('투표 수', default = 0)
    def __str__(self):
        return self.q.name+ '/' + self.name