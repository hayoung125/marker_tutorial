# marker_tutorial

## Install
```
pip install -r requirements.txt
```

## Usage
1. config 설정
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
2. 실행
    - 실행 시 `in_folder`(defalut: data) 에 있는 모든 pdf 파일을 변환하여, `output_dir`에 결과를 저장합니다.
    ```
    python src/main.py
    ```

## Troubleshooting
- 깨진 텍스트가 있다면 `force_ocr`을 설정해야 합니다. 이는 문서를 다시 OCR 처리할 것입니다.
- `TORCH_DEVICE`: 추론에 사용할 특정 torch 디바이스를 강제로 설정하려면 이를 사용하세요.
- 메모리 부족 오류가 발생하면 작업자 수를 줄이세요. 또한 긴 PDF 파일을 여러 파일로 분할해 볼 수 있습니다.
- `RuntimeError: MPS backend out of memory` 문제
    - `.zshrc`에서 `export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0` 추가