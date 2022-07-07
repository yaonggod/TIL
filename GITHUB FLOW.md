# GITHUB FLOW

## 기본 원칙

1. master branch는 반드시 배포 가능한 상태여야 한다.
2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
3. commit message는 매우 중요하며, 명확하게 작성한다.
4. pull request를 통해 협업을 진행한다.
5. 변경사항을 변경하고 싶다면 master branch에 병합한다.

## Feature Branch Workflow

Shared repository model (저장소의 소유권이 있는 경우)

- 원격 저장소에 브랜치 반영 가능, 병합 후 브랜치 삭제

## Forking Workflow

Fork & Pull model (저장소의 소유권이 없는 경우)

1. 남의 GitHub에 들어가서 Fork 버튼 누르기
2. 자신의 원격 저장소에 저장될 이름을 작성하고 create fork
3. fork 받아온 저장소를 본인의 로컬로 clone(code 누르고 본인 저장소 복사)
4. branch 생성 후 작업
5. add, commit, push
6. GitHub에서 Compare & pull request 생성, 내용 작성 후 create pull request