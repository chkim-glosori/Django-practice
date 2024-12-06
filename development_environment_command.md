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
cd {project_directory}
python manage.py migrate
```
정확히 이해하지는 못했지만, 데이터베이스를 이용해서 테이블, 필드, 인덱스, 제약 조건을 생성하고 관리할 수 있는 기능을 추가해주는 명령어라고 한다.

## 6. 서버 실행
```bash
cd {project_directory}
python manage.py runserver
```

## 7. 애플리케이션 생성하기 (project 의 root directory 에서 진행)
```bash
python manage.py startapp {application_name}
```