# 하나의 파일을 실행하는 예시 입니다.
import os

os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = (
    "1"  # Transformers uses .isin for a simple op, which is not supported on MPS
)

import time

from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter

# from marker.logger import configure_logging
from marker.models import create_model_dict
from marker.output import save_output

from src.config import cfg_engine

# configure_logging()


def main(fpath: str, **kwargs):
    start = time.time()
    config_parser = ConfigParser(kwargs)

    converter = PdfConverter(
        config=config_parser.generate_config_dict(),
        artifact_dict=create_model_dict(),
        processor_list=config_parser.get_processors(),
        renderer=config_parser.get_renderer(),
    )
    rendered = converter(fpath)
    out_folder = config_parser.get_output_folder(fpath)
    save_output(rendered, out_folder, config_parser.get_base_filename(fpath))

    print(f"Saved markdown to {out_folder}")
    print(f"Total time: {time.strftime('%H:%M:%S', time.time() - start)}")


if __name__ == "__main__":
    fpath = "./data/skms/SKMS.pdf"
    config = cfg_engine.marker
    main(fpath, **config)

# fpath
