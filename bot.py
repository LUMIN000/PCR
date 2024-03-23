import disnake, asyncio
from disnake.ext import commands
import json
import random
import sqlite3
from datetime import datetime, timedelta

intents = disnake.Intents.default()
intents.message_content = True  # 메시지 내용 인텐트 활성화
bot = commands.Bot(command_prefix="!", intents=intents)

token = "" # 봇토큰

def load_config():
    with open('config.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_config(data):
    with open('config.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

class Setting(disnake.ui.Modal):
    def __init__(self):

        components = [
        disnake.ui.TextInput(
            label="비밀번호",
            placeholder="",
            required=True,
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=20,
            custom_id="pw",
        ),
        disnake.ui.TextInput(
            label="토큰",
            placeholder="",
            required=True,
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=130,
            custom_id="token",
        ),
        disnake.ui.TextInput(
            label="상태",
            placeholder="",
            required=True,
            value = "PLAYING",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=10,
            custom_id="type",
        ),
        disnake.ui.TextInput(
            label="접두사",
            placeholder="",
            required=True,
            value = "!",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=4,
            custom_id="prefix",
        )
        
        ]
        super().__init__(
            title=f"RPC 기본 설정",
            custom_id="setting1",
            components=components,
            timeout=10000
        )

class Photo(disnake.ui.Modal):
    def __init__(self):

        components = [
        disnake.ui.TextInput(
            label="비밀번호",
            placeholder="",
            required=True,
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=20,
            custom_id="pw",
        ),
        disnake.ui.TextInput(
            label="큰사진",
            placeholder="",
            required=True,
            value = "https://media.discordapp.net/attachments/1170317205427200010/1204504567077929110/cloud.png",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=300,
            custom_id="largeimage",
        ),
        disnake.ui.TextInput(
            label="작은사진",
            placeholder="",
            required=False,
            value = "https://media.discordapp.net/attachments/1170317205427200010/1204504567077929110/cloud.png",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=300,
            custom_id="smallimage",
        ),
        disnake.ui.TextInput(
            label="큰사진 글자",
            placeholder="",
            required=True,
            value = "Cloud AN RPC Example 1",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=50,
            custom_id="largete",
        ),
        disnake.ui.TextInput(
            label="작은사진 글자",
            placeholder="",
            required=False,
            value = "Cloud AN RPC Example 2",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=50,
            custom_id="smallte",
        )
        
        ]
        super().__init__(
            title=f"RPC 사진 설정",
            custom_id="photo1",
            components=components,
            timeout=10000
        )

class Button(disnake.ui.Modal):
    def __init__(self):

        components = [
        disnake.ui.TextInput(
            label="비밀번호",
            placeholder="",
            required=True,
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=20,
            custom_id="pw",
        ),
        disnake.ui.TextInput(
            label="상단버튼 (이름)",
            placeholder="",
            required=False,
            value = "서버링크",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=300,
            custom_id="button1",
        ),
        disnake.ui.TextInput(
            label="하단버튼 (이름)",
            placeholder="",
            required=False,
            value = "자판기",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=300,
            custom_id="button2",
        ),
        disnake.ui.TextInput(
            label="상단버튼 (링크)",
            placeholder="",
            required=False,
            value = "https://starvend.xyz/",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=2000,
            custom_id="button1link",
        ),
        disnake.ui.TextInput(
            label="하단버튼 (링크)",
            placeholder="",
            required=False,
            value = "https://starvend.xyz/discord",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=2000,
            custom_id="button2link",
        )
        
        ]
        super().__init__(
            title=f"RPC 버튼 설정",
            custom_id="button1",
            components=components,
            timeout=10000
        )

class Ment(disnake.ui.Modal):
    def __init__(self):

        components = [
        disnake.ui.TextInput(
            label="비밀번호",
            placeholder="",
            required=True,
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=20,
            custom_id="pw",
        ),
        disnake.ui.TextInput(
            label="상단멘트",
            placeholder="",
            required=False,
            value = "기모띠한 스타",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=300,
            custom_id="details",
        ),
        disnake.ui.TextInput(
            label="하단멘트",
            placeholder="",
            required=False,
            value = "섹시한 스타",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=300,
            custom_id="state",
        ),
        disnake.ui.TextInput(
            label="상태메시지 + 제목",
            placeholder="",
            required=False,
            value = "귀여운 스타입니다.",
            style=disnake.TextInputStyle.short,
            min_length=1,
            max_length=20,
            custom_id="name",
        )
        
        ]
        super().__init__(
            title=f"RPC 멘트 설정",
            custom_id="ment1",
            components=components,
            timeout=10000
        )

@bot.command()
async def 생성(ctx, date: int):
    if not ctx.author.id == int(434100608857800744):
        return
    license_key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))

    conn = sqlite3.connect('license.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO licenses VALUES (?, ?)', (license_key, date))
    conn.commit()
    conn.close()

    await ctx.send(f'랜덤 라이센스: {license_key}\n날짜: {date}')

@bot.command()
async def 등록(ctx, license: str):
    conn = sqlite3.connect('license.db')
    cursor = conn.cursor()

    # 라이센스 조회 및 date 값을 가져옴
    cursor.execute('SELECT licenses, date FROM licenses WHERE licenses=?', (license,))
    result = cursor.fetchone()

    if result:
        licenses, date = result
        current_date = datetime.now()

        # date를 정수로 변환하고 현재 날짜에 더해서 만료 날짜 계산
        expiration_date = (current_date + timedelta(days=int(date))).strftime('%Y-%m-%d')

        # 라이센스 삭제
        cursor.execute('DELETE FROM licenses WHERE licenses=?', (license,))
        conn.commit()
        conn.close()

        try:
            with open('config.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        new_entry = {
            "id": str(ctx.author.id),
            "pw": license,
            "token": "",
            "prefix": "",
            "embed": False,
            "day": expiration_date,
            "type": "",
            "details": "",
            "state": "",
            "name": "",
            "largeimage": "",
            "smallimage": "",
            "largete": "",
            "smallte": "",
            "button1": "",
            "button2": "",
            "button1link": "",
            "button2link": ""
        }


        data['tokens'].append(new_entry)

        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        await ctx.send(f'라이센스가 등록되었습니다. 만료 날짜: {expiration_date}')
    else:
        conn.close()
        await ctx.send('없는 라이센스입니다.')

@bot.slash_command(name='패널', description='테스트 명령어')
async def 패널(interaction: disnake.ApplicationCommandInteraction):
    select = disnake.ui.Select(
        custom_id="testselect",
        placeholder="설정하려는 옵션을 선택해주세요.",
        options=[
            disnake.SelectOption(label="기본설정", description="RPC 기본설정 입니다.", emoji="🔧", value="setting"),
            disnake.SelectOption(label="멘트설정", description="RPC에 뜨는 멘트관련 설정입니다.", emoji="🔧", value="ment"),
            disnake.SelectOption(label="사진설정", description="RPC에 뜨는 사진관련 설정입니다.", emoji="🔧", value="photo"),
            disnake.SelectOption(label="버튼설정", description="RPC에 뜨는 버튼관련 설정입니다.", emoji="🔧", value="button"),
        ],
    )

    view = disnake.ui.View()
    view.add_item(select)
    await interaction.response.send_message(embed=disnake.Embed(title="패널", description="쉽다.", color=0x2B2D31), ephemeral=True, view=view)

@bot.event
async def on_interaction(interaction: disnake.MessageInteraction):
    if interaction.type == disnake.InteractionType.component:
        if interaction.data.custom_id == "testselect":
            selected = interaction.data.values[0]
            
            if selected == 'setting':
                await interaction.response.send_modal(Setting())
                try:
                    modal_inter: disnake.ModalInteraction = await bot.wait_for(
                        "modal_submit",
                        check=lambda i: i.custom_id == "setting1" and i.author.id == interaction.author.id,
                        timeout=10000,
                    )

                except asyncio.TimeoutError:
                    return
                
                config = load_config()
                user_id = str(interaction.user.id)
                pw = modal_inter.text_values["pw"]


                for user_config in config['tokens']:
                    if user_config.get("id") == user_id and user_config.get("pw") == pw:
                        user_config['token'] = modal_inter.text_values["token"]
                        user_config['type'] = modal_inter.text_values["type"]
                        user_config['prefix'] = modal_inter.text_values["prefix"]
                        save_config(config)
                        await modal_inter.send("설정이 업데이트되었습니다.", ephemeral=True)
                        return

                await modal_inter.send("ID 또는 비밀번호가 일치하지 않습니다.", ephemeral=True)

            if selected == 'ment':
                await interaction.response.send_modal(Ment())
                try:
                    modal_inter: disnake.ModalInteraction = await bot.wait_for(
                        "modal_submit",
                        check=lambda i: i.custom_id == "ment1" and i.author.id == interaction.author.id,
                        timeout=10000,
                    )

                except asyncio.TimeoutError:
                    return
                
                config = load_config()
                user_id = str(interaction.user.id)
                pw = modal_inter.text_values["pw"]

                for user_config in config['tokens']:
                    if user_config.get("id") == user_id and user_config.get("pw") == pw:
                        user_config['details'] = modal_inter.text_values["details"]
                        user_config['state'] = modal_inter.text_values["state"]
                        user_config['name'] = modal_inter.text_values["name"]
                        save_config(config)
                        await modal_inter.send("설정이 업데이트되었습니다.", ephemeral=True)
                        return

                await modal_inter.send("ID 또는 비밀번호가 일치하지 않습니다.", ephemeral=True)

            if selected == 'photo':
                await interaction.response.send_modal(Photo())
                try:
                    modal_inter: disnake.ModalInteraction = await bot.wait_for(
                        "modal_submit",
                        check=lambda i: i.custom_id == "photo1" and i.author.id == interaction.author.id,
                        timeout=10000,
                    )

                except asyncio.TimeoutError:
                    return
                
                config = load_config()
                user_id = str(interaction.user.id)
                pw = modal_inter.text_values["pw"]

                for user_config in config['tokens']:
                    if user_config.get("id") == user_id and user_config.get("pw") == pw:
                        user_config['largeimage'] = modal_inter.text_values["largeimage"]
                        user_config['smallimage'] = modal_inter.text_values["smallimage"]
                        user_config['largete'] = modal_inter.text_values["largete"]
                        user_config['smallte'] = modal_inter.text_values["smallte"]
                        save_config(config)
                        await modal_inter.send("설정이 업데이트되었습니다.", ephemeral=True)
                        return

                await modal_inter.send("ID 또는 비밀번호가 일치하지 않습니다.", ephemeral=True)

            if selected == 'button':
                await interaction.response.send_modal(Button())
                try:
                    modal_inter: disnake.ModalInteraction = await bot.wait_for(
                        "modal_submit",
                        check=lambda i: i.custom_id == "button1" and i.author.id == interaction.author.id,
                        timeout=10000,
                    )

                except asyncio.TimeoutError:
                    return
                
                config = load_config()
                user_id = str(interaction.user.id)
                pw = modal_inter.text_values["pw"]

                for user_config in config['tokens']:
                    if user_config.get("id") == user_id and user_config.get("pw") == pw:
                        user_config['button1'] = modal_inter.text_values["button1"]
                        user_config['button2'] = modal_inter.text_values["button2"]
                        user_config['button1link'] = modal_inter.text_values["button1link"]
                        user_config['button2link'] = modal_inter.text_values["button2link"]
                        save_config(config)
                        await modal_inter.send("설정이 업데이트되었습니다.", ephemeral=True)
                        return

                await modal_inter.send("ID 또는 비밀번호가 일치하지 않습니다.", ephemeral=True)


bot.run(token)
