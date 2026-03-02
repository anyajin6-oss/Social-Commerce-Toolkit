rom config.config import TIKTOK_API_BASE_URL, BOT_NAME, AUTO_REPLY_ENABLED, DEFAULT_RESPONSE, TIKTOK_ACCOUNT_ID
from automation.utils.helper import get_current_timestamp, format_response, validate_account_id

def main():
    print(f"启动 {BOT_NAME}...")
    print(f"API 地址: {TIKTOK_API_BASE_URL}")
    print(f"当前时间戳: {get_current_timestamp()}")

    if validate_account_id(TIKTOK_ACCOUNT_ID):
        print(f"账号 ID 验证通过: {TIKTOK_ACCOUNT_ID}")
    else:
        print("账号 ID 验证失败，请检查配置。")

    if AUTO_REPLY_ENABLED:
        print("自动回复已启用，默认回复示例:")
        print(format_response(DEFAULT_RESPONSE))
    else:
        print("自动回复已禁用。")

if name == "__main__":
    main()
