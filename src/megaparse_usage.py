from megaparse import MegaParse
from megaparse.parser.unstructured_parser import UnstructuredParser

# import nltk
# nltk.download("punkt_tab")

parser = UnstructuredParser()
megaparse = MegaParse(parser)
# response = megaparse.load(
#     "./data/material/word/122 SK China정보분석실Intelligence_中 전문가, 미중 관계 악화로 동아시아 지정학 리스크 증대 우려.pdf"
# )
response = megaparse.load("./data/papers/english/lightrag.pdf")
print(response)
megaparse.save("./output/megaparse/test.md")


# import os
# import dotenv

# from megaparse import MegaParse
# from langchain_openai import ChatOpenAI
# from megaparse.parser.megaparse_vision import MegaParseVision

# dotenv.load_dotenv("./.env")

# model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))  # type: ignore
# parser = MegaParseVision(model=model)
# megaparse = MegaParse(parser)
# response = megaparse.load(
#     "./data/122 SK China정보분석실Intelligence_中 전문가, 미중 관계 악화로 동아시아 지정학 리스크 증대 우려.pdf"
# )
# print(response)
# megaparse.save("./output/megaparse/test.md")
