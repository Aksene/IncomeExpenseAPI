from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):
        try:
            email = EmailMessage(
                subject=data['email_subject'], body=data['email_body'],to=[data['to_email']])
            response = email.send()
        except Exception as e:
                    pass