"""
模拟邮件系统
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class MailAdminClient():  # 邮件管理后台
    def create_user(self):  # 创建用户
        return MailUser()

    def delete_user(self,user):  # 删除用户
        # do some cleanup
        pass


@dataclass
class Email():
    subject: str  # 邮件主题
    body: str  # 邮件内容


@dataclass
class MailUser():  # 邮件使用人
    # 收件箱
    inbox : List[Email] = field(default_factory=list)

    def send_email(self, email, other):
        """
        发送邮件
        :param email: 邮件（邮件主题，邮件内容）
        :param other: 收件人
        :return: None
        """
        other.inbox.append(email)

    def clean_mailbox(self):
        """
        清理邮箱
        :return: None
        """
        self.inbox.clear()
