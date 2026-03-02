mport os
import time

def get_current_timestamp():
    """获取当前时间戳"""
    return int(time.time())

def format_response(message):
    """格式化机器人回复"""
    return f"【海外商务小助手】{message}"

def validate_account_id(account_id):
    """验证账号ID格式"""
    if not account_id or not isinstance(account_id, str):
        return False
    return len(account_id) > 0
