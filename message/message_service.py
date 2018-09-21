from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = "3462154729@qq.com"
password = "asd123456"


def sendEmailMessage(email, message):
    print("send to email>> ", email, ":", message)
    messageObj = MIMEText(message, "plain", "utf-8")
    messageObj['From'] = sender
    messageObj['To'] = email
    messageObj['Subject'] = Header('A email from kubo', 'utf-8')
    try:
        smtpObj = smtplib.SMTP('smpt.qq.com')
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, [email], messageObj.as_string())
        print("send mail success")
        return True
    except smtplib.SMTPException as ex:
        print("send mail failed")
        print(ex)
        return False

class MessageServiceHandler(object):

    def sendMobileMessage(self, mobile, message):
        print("send to mobile>> ",mobile,":",message)
        return True
    def sendEmailMessage(self, email, message):
        print("send to email>> ", email, ":", message)
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['From'] = sender
        messageObj['To'] = email
        messageObj['Subject'] = Header('A email from kubo', 'utf-8')
        try:
            smtpObj = smtplib.SMTP('smpt.qq.com')
            smtpObj.login(sender, password)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print("send mail success")
            return True
        except smtplib.SMTPException as ex:
            print("send mail failed")
            print(ex)
            return False

if __name__ == "__main__":
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift start")
    server.serve()
    print("python thrift stop")
