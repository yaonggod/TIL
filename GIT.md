# GIT

분산 버전 관리 시스템

작업을 하고 → 변경된 파일을 모아 → 버전으로 남긴다

modified → staged → committed

```bash
git init 
- git이 활성화되지 않은 폴더에서 git 활성화

git add .
git add 파일
git rm 파일
git restore 파일 - 변경 사항 취소
git commit -m “커밋 메시지”
- 버전 기록
git status
- 커밋된 파일과 커밋되어야 할 파일을 보여줌
git log (--oneline)
- 커밋 확인

참고 : 시작할 때 git config --global user.name “yaonggod” // git config --global user.email “내 이메일”
이름 확인 : git config user.name

기타 커맨드 창에서 유용한 명령어들
-mkdir 디렉토리명 - 디렉토리 만들기
-cd 디렉토리명/../~ - 디렉토리로 이동하기
-ls - 현재 디렉토리 들여다보기
-touch 파일명 - 파일 생성
-pwd - 현재 디렉토리 출력
-rm 파일명 - 파일 삭제하기
-rm -r 디렉토리 - 디렉토리 삭제하기
```

