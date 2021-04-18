import logging
from datetime import datetime
import pyperclip # 클립보드 집어넣기

# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")


# # level : debug < info < warning < error < critical
# logging.debug("아 이거 누가짠거임?")
# logging.info("자동화 수행 준비")
# logging.warning("실행상의 문제가 발생할수 있음")
# logging.error("error 발생")
# logging.critical("복구불가 심각한 문제가 발생")

filename  = datetime.now().strftime("mylogFile_%y%m%d%H%M%S.log")

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

#로그레벨설정
logger.setLevel(logging.DEBUG)

#스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행")
