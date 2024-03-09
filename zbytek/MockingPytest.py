import smtplib

def send_email(sender, receiver, subject, message):
    smtp_server = smtplib.SMTP('smtp.example.com')
    smtp_server.sendmail(sender, receiver, f'Subject: {subject}\n\n{message}')
    smtp_server.quit()


def test_send_email(mocker):
    smtp_mock = mocker.patch('smtplib.SMTP')

    send_email('sender@example.com', 'receiver@example.com', 'Test Subject', 'Test Message')

    smtp_mock.assert_called_once_with('smtp.example.com')
    smtp_mock.return_value.sendmail.assert_called_once()
    smtp_mock.return_value.quit.assert_called_once()