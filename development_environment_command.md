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