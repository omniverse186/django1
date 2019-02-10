from django.db import models
#글쓴이를 외래키로 지정하기 위해 import
from django.contrib.auth.models import User

# 카테고리
# 카테고리 이름
class PostType(models.Model):
    name = models.CharField('카테고리', max_length = 20)
    def __str__(self):
        return self.name
# 글 정보
# 제목, 글쓴이 - 외래키, 글내용, 작성일, 카테고리-외래키
class Post(models.Model):
    category = models.ForeignKey(PostType, on_delete = models.CASCADE)
    headline = models.CharField('제목', max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    #TextField : 글자 수 제한이 없는 문자열 저장공간
    #default 외에 XXXField에서 사용할 수 있는 공통 매개변수
    #null(기본 값 False) : True값을 저장한 경우, 데이터베이스에 객체 저장 시 해당 변수 값이 비어있어도 생성ok
    #blank(기본값 False) : True 값을 저장한 경우, 폼객체를 통한 사용자 입력공간(<input>) 제공시, 
    #해당 변수의 입력 공간을 빈칸으로 허용
    content = models.TextField('내용', null = True , blank = True)
    #auto_now_add(DateTimeField, DateField에서만 사용 가능)
    #객체 생성시, 서버기준의 날짜/시간이 자동으로 저장되도록 서렂ㅇ하는 매개변수
    pub_date = models.DateTimeField('작성일',auto_now_add=True)
    class Meta:
        #pub_date변수에 저장된 값을 내림차순으로 정렬
        ordering = ['-pub_date']
# 글에 포함된 이미지 정보
# 글-외래키, 이미지 파일
#ImageFiled : 이미지 파일을 저장하는 공간
#ImageField를 사용하려면 Pillow모듈이 설치되어 있어야 함
#pip install Pillow
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #upload_to : 실제 파일이 저장되는 경로를 지정하는 매개변수
    #서버 기준의 날짜 데이터를 포함 시킬 수 있음
    #%Y : 객체저장될때 서버기준의 연도
    #%m : 달
    #%d : 일
    image = models.ImageField('이미지 파일', upload_to = 'images/%Y/%m/%d')
# 글에 포함된 첨부파일 정보
# 글-외래키, 파일
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #filefield -> 파일을 저장하는 공간
    file = models.FileField('첨부 파일',
                            upload_to='files/%Y/%m/%d')
