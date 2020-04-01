from flask import Flask, request, abort
import random
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('V/CtP/rr9dPW7fT//LVR1BH0hmNVUVTDqd4pI2uZN4+u+tErKZIAR+gTkoiuXFeIEhvQat/pwqM+9UkIHe3RcApbeOI67Py9HRmQ9j0SCvq6lDzYsHurgsxm/KVBb2SNm93E2oJlNJM/4RbqFhclowdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a820ef2a99f799e08fe5548f806e4abe')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "喵~喵~喵"
    if msg in ["hi","HI"]:
        r = "喵嗚~"
    elif msg == "駕照":
        r = "有滿18歲喵~"
    elif msg == "滿了":
        r = "要常帶喵喵出門喔"
    elif msg == "大樂透"
        lottery = []
        lottery = (random.sample(range(1, 49), k=6))
        r = lottery
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()