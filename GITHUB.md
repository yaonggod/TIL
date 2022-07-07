# GITHUB

원격 저장소(GitHub)에 로컬 저장소의 커밋을 push함

GitHub 로그인 → 우측 상단 + → New Repository → Repository name, description을 기입하고 public 설정 후 create → 터미널 실행 후 가이드대로 실행하기

```bash
git remote add origin url
- 로컬 저장소에 원격 저장소 정보 저장

git remote -v
- 원격 저장소 정보 출력

git push origin(원격 저장소) master
- 원격 저장소로 커밋을 올림
```

> push할 때는 인증 필수

```bash
git pull origin(원격 저장소) master
- 원격 저장소 커밋 가져오기

git clone url
- 원격 저장소 복제

git remote rm origin(원격 저장소)
- 원격 저장소 삭제
```

아예 새로운 프로젝트를 시작할 때, 저장소를 받아옴, init 과정이 필요 없음 → clone

그 프로젝트를 갱신하고 싶을 때, 변경된 커밋을 받아옴 → pull

> 남의 프로젝트는 초대 없이 함부로 커밋 금지

- push 실패 시 : 로컬과 원격 저장소의 커밋 이력이 다를 때

​	→ pull → 로컬에서 커밋 병합 → push

- 버전 관리를 하지 않는 파일/디렉토리는 .gitignore로 관리

​	! 이미 커밋된 파일은 반드시 삭제를 해야 .gitignore로 적용됨