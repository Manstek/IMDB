def send_notif_telegram(name: str, last_name: str, email: str) -> None:
    """Функция отправки уведомления в телеграмм (надо дореализовать)."""
    msg = f'Пользователь заполнил форму: {name}, {last_name}, {email}'
    print(msg)
