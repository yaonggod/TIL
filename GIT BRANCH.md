# GIT BRANCH

master 말고 다른 영역(branch)에서 작업 후 병합

1. 브랜치 생성

```bash
git branch (branch name)
```

1. 브랜치 조회

```bash
git branch
```

1. 브랜치 이동

```bash
git checkout (branch name)
```

1. 브랜치 생성 후 이동

```bash
git checkout -b (branch name)
```

브랜치에서 작업 → add → commit 이후

1. 브랜치 병합 (master에서 실행)

```bash
git merge (branch name)
```

1. 브랜치 지우기

```bash
git branch -d (branch name)
```

작업 완료하고 브랜치를 병합하면 브랜치에서 작업한 내용이 master에 합쳐지므로 지워도 작업한 내용은 master에 남아있음

1. 그래프 형태로 log 확인하기

```bash
git log --oneline --graph
```

*상황 1. 혼자 작업(fast-forward)*

```bash
(master) $ git branch feature/home
(master) $ git checkout feature/home

(feature/home) $ touch home.txt
(feature/home) $ git add .
(feature/home) $ git commit -m "Add home.txt"

(feature/home) $ git checkout master

(master) $ git merge feature/home

(master) $ git branch -d feature/home
```

*상황 2. 서로 다른 커밋을 병합하는 과정에서 다른 파일이 수정되어 있는 상황*

```bash

(master) $ git checkout -b feature/about

(feature/about) $ touch about.txt
(feature/about) $ git add .
(feature/about) $ git commit -m "Add about.txt"

(feature/about) $ git checkout master

(master) $ touch master.txt
(master) $ git add . 
(master) $ git commit -m "Add master.txt"

(master) $ git merge feature/about

(master) $ git branch -d feature/about
```

*상황 3. 서로 다른 커밋을 병합하는 과정에서 같은 파일의 동일한 부분이 수정되어 있는 상황*

```bash
(master) $ git checkout -b feature/test

# 두 커밋 모두 README.md 파일을 열어서 수정
(feature/test) $ touch test.txt
(feature/test) $ git add .
(feature/test) $ git commit -m "Update README.md, Add test.txt"

(feature/test) $ git checkout master

(master) $ touch master.txt
(master) $ git add README.md
(master) $ git commit -m "Update README.md"

(master) $ git merge feature/test
```

*merge conflict(충돌)해서 merge에 fail하고 branch가 (master|MERGING)으로 변함*

*→ 충돌 확인 및 해결*

```bash
(master|MERGING) $ git add .
(master|MERGING) $ git commit

(master) $ git branch -d feature/about
```