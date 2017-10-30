import itchat, time
from itchat.content import *


# from PIL import Image


def sentChatRoomsMsg(name, content):
    itchat.get_chatrooms(update=True)
    iroom = itchat.search_chatrooms(name)
    for room in iroom:
        if room['NickName'] == name:
            userName = room['UserName']
            break
    itchat.send_msg(content, userName)
    try:
        # img = Image.open("C:/Users/faith/Desktop/wechatPersonal/img/a.jpg")
        itchat.send_image("C:/Users/faith/Desktop/wechatPersonal/img/moneyboy.jpg", userName)  # 自动回复文本等类别的群聊消息
    except IOError:
        print("Error: 没有找到文件或读取文件失败")


# else:
# # 缩小图片
# img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
# # 拼接图片
# toImage.paste(img, (x * eachsize, y * eachsize))
# x += 1
# if x == numline:
#     x = 0
#     y += 1

# isGroupChat=True表示为群聊消息
@itchat.msg_register([TEXT, CARD, PICTURE, SHARING], isGroupChat=True)
def group_reply_text(msg):
    if msg['Type'] == TEXT:
        content = msg['Content']
    elif msg['Type'] == SHARING:
        content = msg['Text']
    username = ''

    # 发送者的昵称
    if 'ActualNickName' in msg:
        username = msg['ActualNickName']
        # if username == "Alan.Yeung":
        #     sentChatRoomsMsg(u'得嗲噶', 'alen 哥牛逼')
        if username == u'崔智理' or username == u'幻影zL' or username == u'Cui智理':
            sentChatRoomsMsg(u'得嗲噶', '智理总有钱仔')
            # sentChatRoomsMsg(u'得嗲噶', 'test msg')
    print(username + ":" + content)

# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text

# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))
#     elif msg.text == "faith":
#         msg.user.send('%s: %s' % (msg.type, msg.text))

# itchat.send('Hello, filehelper', toUserName='filehelper')
itchat.auto_login(hotReload=True)
# itchat.send_image("C:/Users/faith/Desktop/wechatPersonal/img/a.jpg", 'filehelper')
while True:
    sentChatRoomsMsg(u'得嗲噶', '智理总有钱仔')

itchat.run()
