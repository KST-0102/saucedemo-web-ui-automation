# SauceDemo Web UI Test Automation

## 1. 프로젝트 개요

SauceDemo 웹사이트를 대상으로 Python, Playwright, pytest를 활용한 UI 테스트 자동화 프로젝트입니다.

로그인부터 상품 정렬, 장바구니, 주문 과정까지 주요 사용자 시나리오를 자동화하고, 테스트 결과를 검증했습니다.

## 2. 기술 스택

- **Language:** Python 3.14
- **Test Framework:** pytest
- **Automation Tool:** Playwright
- **Test Report:** pytest-html
- **Version Control:** Git / GitHub

## 3. 테스트 범위

| 기능 | 주요 테스트 내용 |
|---|---|
| Login | 정상 로그인, 잘못된 로그인 정보, 빈 입력값 |
| Product Sorting | 상품명 및 가격 정렬 |
| Cart | 상품 추가 및 장바구니 확인 |
| Checkout | 주문 정보 입력 및 주문 완료 흐름 |

총 20개의 테스트 함수를 작성했으며, 이 중 19개는 기능 검증 테스트이고 1개는 정렬 옵션 확인을 위한 학습·점검용 테스트입니다.

## 4. 프로젝트 구조

```text
qa-web-automation/
├── conftest.py
├── test_login.py
├── test_sort.py
├── test_cart.py
├── test_checkout.py
├── reports/
│   └── report.html
└── .gitignore
```

## 5. 테스트 실행 방법

### 1) 프로젝트 복제

```bash
git clone https://github.com/KST-0102/saucedemo-web-ui-automation.git
cd saucedemo-web-ui-automation
```

### 2) 가상환경 생성 및 활성화

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3) 라이브러리 설치

```bash
pip install pytest pytest-playwright pytest-html
playwright install chromium
```

### 4) 테스트 실행

```bash
pytest -v -s --log-cli-level=INFO
```

### 5) HTML 리포트 생성

```bash
pytest -v -s --log-cli-level=INFO --html=reports/report.html --self-contained-html
```

## 6. 테스트 결과

- 총 테스트 함수: 20개
- 기능 검증 테스트: 19개
- 학습·점검용 테스트: 1개
- 최종 실행 결과: 20 passed

상세 실행 결과는 `reports/report.html`에서 확인할 수 있습니다.

## 7. 주요 학습 내용

- Playwright를 활용한 웹 UI 테스트 자동화
- pytest Fixture를 활용한 테스트 환경 및 로그인 상태 재사용
- 테스트 시나리오별 검증 로직 작성
- Python logging을 활용한 테스트 실행 로그 기록
- Decimal을 활용한 금액 계산 및 비교
- pytest-html을 활용한 테스트 결과 리포트 생성
- Git과 GitHub를 활용한 소스 코드 버전 관리