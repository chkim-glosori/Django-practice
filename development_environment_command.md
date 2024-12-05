# Virtual Environment (UNIX OS 환경 가정)

## 1. 격리된 환경 만들기
```bash
python -m venv {원하는_가상환경의_디렉터리_이름}
```

## 2. 가상 환경 실행하기
```bash
source {가상환경_디렉터리_이름}/bin/activate
```

## 3. pip 를 이용하여 Django install
```bash
pip install Django~=4.1.0
```

## 4. 프로젝트 만들기
```bash
django-admin startproject {하고_싶은_프로젝트_이름}
```

## 5. 데이터베이스 마이그레이션
```bash
cd mysite
python manage.py migrate
```
정확히 이해하지는 못했지만, 데이터베이스를 이용해서 테이블, 필드, 인덱스, 제약 조건을 생성하고 관리할 수 있는 기능을 추가해주는 명령어라고 한다.