"""
# step1：执行sending_user 创建发件用户
# step2: 执行receiving_user 创建收件用户
# step3: 执行test_email_received 用例
# step4: 执行receiving_user删除接受用户
# step5: 执行sending_user删除发送用户
"""
from btest.D3.mail import Email


def test_email_received(sending_user, receiving_user):
    print('\n--test_email_received执行测试-------\n')

    # 构造邮件
    email = Email(subject="Hey!", body="How's it going?")
    # 发送者发送邮件给接受者
    sending_user.send_email(email, receiving_user)

    # 断言 邮件是否在接收人的邮箱中
    assert email in receiving_user.inbox

# 说明：
# 同级别的夹具环境初始化是顺序、环境清理是逆序。
# 夹具yield 前面代码是按照参数顺序执行。环境初始化是顺序。
# 夹具yield 后面代码是按照参数逆序执行。环境清理是逆序。
