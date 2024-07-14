# FastAPI-FileAPI
## API
- 파일 업로드 목록 API
    - 업로드 IP로 이력 관리
- 파일 업로드 API
    - 로컬 디렉터리에 sha256 이름으로 저장
    - MariaDB 사용 업로드 이력 관리
- 파일 다운로드 API
    - 로컬 디렉터리에 업로드된 단일 파일 다운로드
    - 여러 파일 zip 압축 다운로드

## 구현 기능
- 404 핸들러 처리 적용
- 공통 DTO 사용 일관된 API 응답 관리
- MariaDB 활용 업로드 이력 관리
- Multipart 이용 대용량 파일 업로드
