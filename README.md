# marker_tutorial
Marker는 PDF를 빠르고 정확하게 마크다운, JSON, HTML로 변환합니다. 

### 기능
    - 다양한 문서 지원
    - 모든 언어 지원
    - 머리글/바닥글/기타 아티팩트 제거
    - 테이블 및 코드 블록 서식 지정
    - 마크다운과 함께 이미지 추출 및 저장
    - 수식을 LaTeX로 변환
    - 사용자 지정 서식 및 로직으로 쉽게 확장 가능
    - GPU, CPU 또는 MPS에서 작동

## 작동원리
Marker는 딥 러닝 모델의 파이프라인입니다.

- 필요한 경우 텍스트 추출, OCR
- 페이지 레이아웃을 감지하고 읽기 순서를 찾습니다.
- 각 블록을 정리하고 포맷합니다.
- 블록을 결합하고 완전한 텍스트를 후처리합니다.

필요한 경우에만 모델을 사용하여 속도와 정확성을 향상시킵니다.

## Setting
### 0. Requirements
- python ≥ 3.10 (conda 에서 python 3.11 로 진행)
- Mac이나 GPU 머신을 사용하지 않는 경우 먼저 CPU 버전의 토치를 설치해야 할 수도 있습니다. [pytorch](https://pytorch.org/get-started/locally/)
    - MAC 의 경우 자동으로 GPU 연결됌. (`TORCH_DEVICE ="mps”`)

### 1. Install
```
pip install -r requirements.txt
```

### 2. data 폴더 추가
- 변환할 pdf 가 있는 data 폴더를 추가 합니다. 

## Usage
### 1. config 설정
- 주석 처리가 되지 않은 설정값은 기본 설정이므로 필수로 설정해야합니다.
- 주석 처리된 설정값은 추가 설정이므로 필수는 아닙니다.  
```yaml
# config/engine.yaml
marker: 
    debug: False  # [bool] Debug mode.
    in_folder: "./data"  # [str] dir path containing PDFs to convert
    output_dir: "./output"  # [str] Output directory for converted files.
    output_format: "markdown" # [markdown|json|html]
    chunk_idx: 0  # [int] Chunk index to convert, 파일 시작 지정.
    num_chunks: 1  # [int] Number of chunks being processed in parallel. 몇 개의 파일을 변환할 건지 지정.
    max_files: null # [int] Maximum number of PDFs to convert. 최대 몇 개의 파일까지 변환할 건지 지정.
    workers: 5  # [int] Number of worker processes to use.
    skip_existing: False  # [bool] 기존 변환된 파일을 건너뛸 수 있습니다.
    # page_range: "0-1" # [str] Specify which pages to process. Accepts comma-separated page numbers and ranges. Example: "0,5-10,20" will process pages 0, 5 through 10, and page 20.
    # force_ocr: False    # [bool] Force OCR for PDFs.
    # language: "eng"   # [str] Language code for Tesseract OCR. e.g. "ko"
```

### 2. 실행
- 실행 시 `in_folder`(defalut: data) 에 있는 모든 pdf 파일을 변환하여, `output_dir`에 결과를 저장합니다.
```
python src/main.py
```

### 3. Output
- output 폴더에 저장된 변환 결과를 확인합니다.
- 모든 결과에는 metadata dictionary 를 반환합니다.
    - file_name: outputname_meta.json
        ```json
        {
            "table_of_contents": [
            {
                "title": "Introduction",
                "heading_level": 1,
                "page_id": 0,
                "polygon": [...]
            }
            ], // computed PDF table of contents
            "page_stats": [
            {
                "page_id":  0, 
                "text_extraction_method": "pdftext",
                "block_counts": [("Span", 200), ...]
            },
            ...
            ]
        }
        ```


## Troubleshooting
- 깨진 텍스트가 있다면 `force_ocr`을 설정해야 합니다. 이는 문서를 다시 OCR 처리할 것입니다.
- `TORCH_DEVICE`: 추론에 사용할 특정 torch 디바이스를 강제로 설정하려면 이를 사용하세요.
- 메모리 부족 오류가 발생하면 작업자 수를 줄이세요. 또한 긴 PDF 파일을 여러 파일로 분할해 볼 수 있습니다.
- `RuntimeError: MPS backend out of memory` 문제
    - `.zshrc`에서 `export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0` 추가

## 한계점
PDF는 다루기 까다로운 형식이기 때문에 마커(Marker)가 항상 완벽하게 작동하지는 않습니다. 다음은 해결 예정인 몇 가지 알려진 제한 사항입니다:
- 마커는 블록 수식만 변환할 수 있습니다.
- 표는 항상 100% 정확하게 형식화되지 않을 수 있으며, 여러 줄로 된 셀은 때때로 여러 행으로 나뉘는 문제가 있습니다.
- 양식은 최적화된 방식으로 변환되지 않습니다.
- 중첩된 표와 양식이 포함된 매우 복잡한 레이아웃은 제대로 작동하지 않을 수 있습니다.