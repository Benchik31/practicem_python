import config

def resolve_and_check_path(user_input_path: str) -> config.Path:
    target_path = (config.ROOT_DIR / user_input_path).resolve()
    if not str(target_path).startswith(str(config.ROOT_DIR)):
        raise PermissionError("Доступ к пути за пределами рабочей директории запрещен.")
    return target_path