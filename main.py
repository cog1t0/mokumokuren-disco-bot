import discord
from discord.ext import commands
from openai import OpenAI
from constant import TOKEN, OPENAI_API_KEY  # OPENAI_API_KEYもconstant.pyからインポート
from prompt.test import MESSAGES

extensions = (
)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.all(),
        )

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(f'extensions.{extension}')

    # メンションを受けた際の処理を追加
    async def on_message(self, message):
        if message.author.bot:  # ボット自体のメッセージは無視
            return
        if self.user.mentioned_in(message):  # Botへのメンションが含まれている場合
            content = message.content.replace(f'<@!{self.user.id}>', '')  # メンションを削除
            if content.startswith('test:'):  # メッセージの先頭が'test:'で始まる場合        
                messages_to_ai = [
                    {"role": "system", "content":MESSAGES}
                ]
                messages_to_ai.append({"role": "user", "content": content.split('>')[1].lstrip()})
            else:
                messages_to_ai = [
                    {"role": "system", "content": "あなたは技術的な質問に、端的にわかりやすく回答するAIアシスタントです."}
                ]
                messages_to_ai.append({"role": "user", "content": content.split('>')[1].lstrip()})

            # OpenAIのAPIキーを設定
            client = OpenAI(
                # This is the default and can be omitted
                api_key=OPENAI_API_KEY,
            )
            # OpenAI APIを呼び出して応答を生成
            chat_completion = client.chat.completions.create(
                messages=messages_to_ai,
                model="gpt-3.5-turbo",
            )

            await message.channel.send(chat_completion.choices[0].message.content)  # 応答を送信

if __name__ == '__main__':
    MyBot().run(TOKEN)
