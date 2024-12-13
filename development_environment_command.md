# Virtual Environment (UNIX OS 환경 가정)

## 1. 격리된 환경 만들기
```bash
python -m venv {원하는_가상환경의_디렉터리_이름} # 10초 이상 걸린다고 생각하기
```

## 2. 가상 환경 실행하기
```bash
source {가상환경_디렉터리_이름}/bin/activate
```

## 3. pip 를 이용하여 Django install
```bash
pip install Django~=4.1.0 # 2분 이상 걸린다고 생각하기
```

## 4. 프로젝트 만들기 (프로젝트 != 애플리케이션)
```bash
django-admin startproject {하고_싶은_프로젝트_이름}
```

## 5. 데이터베이스 마이그레이션
```bash
# 마이그레이션 생성
# python manage.py makemigrations {application_name}

## 최초의 경우 모든 데이터베이스 마이그레이션하기 (JPA, ddl-auto : create 느낌)
cd {project_directory}
python manage.py migrate

# 특정 모델의 변경 사항을 감지하여 마이그레이션 파일을 생성.
python manage.py makemigrations {특정 Entity 이름}
```
models.py 의 내용을 보고, 테이블과 일치시키는 명령어이다. 필드, 인덱스, 제약 조건 등을 생성하고 관리할 수 있다.

## 6. 서버 실행
```bash
cd {project_directory}
python manage.py runserver
```

## 7. 애플리케이션 생성하기 (project 의 root directory 에서 진행)
```bash
python manage.py startapp {application_name}
```

## 8. 애플리케이션 활성화하기
장고가 애플리케이션을 추적하고 해당 모델에 대해 데이터베이스 테이블을 생성할 수 있또록 하려면 프로젝트에서 blog 애플리케이션을 활성화해야 한다. settings.py 파일에서 INSTALLED_APPS 리스트를 편집하자.

## 9. Super User 생성하기
관리 사이트를 관리할 사용자를 생성할 수 있다.
```bash
python manage.py createsuperuser
```
이후 적절히 Username, email, password 를 설정한다.