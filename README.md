# IoT 백엔드 개발자 포트폴리오

## Phase 1 — 백엔드 기초 : REST API 호출 & JSON 파싱

### 개요
외부 REST API(wttr.in)를 호출해 JSON 파싱 → 모듈화까지 구현

### 구현 내용
- `mission1_json_parsing.py` : 서울 날씨 API 호출 후 딕셔너리 반환 모듈
- `assignment1.py` : 위 모듈 import 후 온도 조건 분기 출력

### 학습 포인트
- REST API 호출 → JSON 파싱 → 중첩 구조에서 값 추출
- 함수 모듈화 + `if __name__ == "__main__"` 패턴
- Git 워크플로우 (커밋, merge 충돌 해결, .gitignore 관리)

### 기술 스택
Python 3.12 / requests / wttr.in API