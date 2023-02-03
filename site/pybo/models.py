from django.db import models

# Create your models here.

class Member(models.Model): # 회원테이블
    mem_id = models.CharField(max_length=15, primary_key=True) # 회원ID
    name = models.CharField(max_length=20) # 이름
    phone = models.CharField(max_length=13) # 연락처
    email = models.EmailField() # 이메일
    address = models.TextField() # 주소
    pw = models.CharField(max_length=15) # 비밀번호
    pw_1 = models.CharField(max_length=15) # 비밀번호 확인s


class Thema(models.Model): # 테마테이블
    t_no = models.CharField(max_length=20, primary_key=True) # 테마번호
    t_name = models.CharField(max_length=20) # 테마이름


class Path(models.Model): # 구간테이블
    p_no = models.CharField(max_length=20, primary_key=True)  # 구간번호
    t_no = models.ForeignKey(Thema, on_delete=models.CASCADE, db_column='t_no')  # FK 테마번호

class Chat(models.Model): # 채팅
    ch_no = models.CharField(max_length=30, primary_key=True) # 채팅방번호
    ch_name = models.TextField() # 채팅장명
    ch_to = models.CharField(max_length=10) # 채팅자수
    mem_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='mem_id') # FK 회원-회원ID
