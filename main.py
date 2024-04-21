import discord
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

GOOGLE_API_KEY = os.environ['geminikey']
server_ids = [1099127843885170748]
token = os.environ['token']
client = discord.Client()
bot = discord.Bot(intents=discord.Intents.all())
model = genai.GenerativeModel(model_name="gemini-pro")
genai.configure(api_key=GOOGLE_API_KEY)
chat = model.start_chat(history=[])
genai.GenerationConfig(max_output_tokens=150)

@bot.event
async def on_ready():
  print("Bot is ready!")

@bot.command(description = "use gemini")
async def send_prompt(ctx, prompt: discord.Option(str)):
  gemini_message = chat.send_message(prompt, safety_settings={HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE})
  print(gemini_message.parts)
  print(gemini_message.text)
  await ctx.respond(f'message: {prompt}\n\nresponse: {gemini_message.text}')

bot.run(token)