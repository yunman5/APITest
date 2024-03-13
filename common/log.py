from loguru import logger

from config import project_path

# 配置日志文件的输出位置和文件名
logger.add(project_path+"/logs/{time:YYYYMMDD}.log", level="INFO")


# 可以在这里添加其他Loguru配置选项

def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)

# # 示例：记录不同级别的日志
# logger.debug("This is a debug message.")
# log_info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")
# logger.critical("This is a critical message.")
