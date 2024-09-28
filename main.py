from abc import ABC


class NotificationSender(ABC):
    def send(self, recipient: str, message: str) -> None:
        pass


class EmailNotificationService(NotificationSender):
    def send(self, email: str, message: str) -> None:
        print(f"Sending email to {email}: {message}")


class SmsNotificationService:
    """Класс из старой бизнес-логики."""

    def send_sms(self, phone_number: str, message: str) -> None:
        print(f"Sending SMS to {phone_number}: {message}")


class SmsAdapter(NotificationSender):
    def __init__(self, sms_service: SmsNotificationService):
        self.sms_service = sms_service

    def send(self, recipient: str, message: str) -> None:
        self.sms_service.send_sms(recipient, message)


def notify_user(notification_sender: NotificationSender, recipient: str, message: str):
    notification_sender.send(recipient, message)


if __name__ == "__main__":
    # Старый сервис email
    email_service = EmailNotificationService()

    sms_service = SmsNotificationService()
    sms_adapter = SmsAdapter(sms_service)

    # Уведомление по email
    notify_user(email_service, "user@example.com", "Hello via Email!")

    # Уведомление по SMS
    notify_user(sms_adapter, "+1234567890", "Hello via SMS!")
