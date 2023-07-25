import gspread
import datetime

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scope)

client = gspread.authorize(creds)

sheet = client.open('charity reminder').sheet1
from typing import Final

# pip install python-telegram-bot
from telegram import Update,Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = '5984698544:AAEBFxieQ3vDGk2QZXY31iBSurvxqm19Tcw'
BOT_USERNAME: Final = '@Charity_reminder_bot'
bot = Bot('5984698544:AAEBFxieQ3vDGk2QZXY31iBSurvxqm19Tcw')
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=0

#chat_id = update.message.chat_id
#first_name = update.message.chat.first_name
#last_name = update.message.chat.last_name
#username = update.message.chat.username



# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'سلام {update.message.chat.first_name} خوش اومدی')
    await update.message.reply_text('برای عضویت در گروه خیرین میتوانی از /signup استفاده کنی')
    await update.message.reply_text('لطفا دقت داشته باشید تمام مبالغی که وارد میکنید ارقام به انگلیسی باشند و هیچ اسپیسی بین آنها نباشد و ۳ رقم آخر اعداد را وارد نکنید')
# Lets us use the /help command
async def editshare_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global c
    global d
    if type(sheet.find(str(update.message.chat_id))) == gspread.cell.Cell :
        for a in range (1,len(sheet.col_values(1))+1):
            if sheet.cell(a,5).value == str(update.message.chat_id) :
                await update.message.reply_text(f'سهم فعلی شما {sheet.cell(a,2).value} تومان در ماه است مقدار صحیح را وارد کنید')
                c = update.message.chat_id
                d = a

    else :
        await update.message.reply_text('شما هنوز عضو نیستید برای عضویت میتوانید از /signup استفاده کنید')



async def signup_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global b
    if type(sheet.find(str(update.message.chat_id))) != gspread.cell.Cell :
        await update.message.reply_text(f'سلام {update.message.chat.first_name} عزیز لطفا مبلغی که میخوای ماهیانه کمک کنی رو وارد کن ')
        b = update.message.chat_id
    else :
        for a in range (1,len(sheet.col_values(1))+1):
            if sheet.cell(a,5).value == str(update.message.chat_id) :
                await update.message.reply_text(f'شما در حال حاضر عضو هستید و سهم شما از کمک ماهانه {sheet.cell(a,2).value}تومان است ,اگر این مقدار اشتباه است با استقاده از   /edit آن را تصحیح کنید')

# Lets us use the /custom command
async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if type(sheet.find(str(update.message.chat_id))) != gspread.cell.Cell :
        await update.message.reply_text(f'درحال حاضر شما عضو نیستید برای عضویت از /signup استفاده کنید')

    else :
        for e in range (1,len(sheet.col_values(1))+1):
            if sheet.cell(e,5).value == str(update.message.chat_id) :
                if sheet.cell(e,3).value <= sheet.cell(e,2).value :
                    await update.message.reply_text(f'سلام {update.message.chat.first_name} در حال حاضر شما {sheet.cell(e,3).value} تومان در این ماه کمک کرده اید و باید {int(sheet.cell(e,2).value) - int(sheet.cell(e,3).value)} تومان دیگر کمک کنید اگر مقدار کمکی این ماه شما اشتباه ثبت شده است شما میتوانید با استقاده از  /editcontribution آن را تصحیح کنید \n از زحمات شما متشکریم ❤🌹')
                else :
                    await update.message.reply_text(f'سلام {update.message.chat.first_name} در حال حاضر شما {sheet.cell(e,3).value} تومان کمک کرده اید که {int(sheet.cell(e,3).value) - int(sheet.cell(e,2).value)} تومان دیگر کمک کنید اگر مقدار کمکی این ماه شما اشتباه ثبت شده است شما میتوانید با استقاده از  /editcontribution آن را تصحیح کنید \n از زحمات شما متشکریم ❤🌹')

async def payoff_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global f
    if type(sheet.find(str(update.message.chat_id))) != gspread.cell.Cell :
        await update.message.reply_text(f'شما هنوز عضو نیستید برای عضویت از /signup استفاده کنید')
    else :
            await update.message.reply_text(f'سلام {update.message.chat.first_name}  عزیز لطفا مبلغ پرداختی خود را بدون 3 رقم آخر و با ارقام انگلیسی وارد کنید\n برای مثال اگر 200 هزار تومان پرداخت کردید فقط 200 را وارد کنید و اگر مبلغ بالای 1 میلیون تومان است باید فقط یک عدد 4 رقمی وارد کنید برای مثال 1000 ')
            f = update.message.chat_id

async def editcontribution_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global m
    if type(sheet.find(str(update.message.chat_id))) != gspread.cell.Cell :
        await update.message.reply_text(f'شما هنوز عضو نیستید برای عضویت از /signup استفاده کنید')
    else :
        for l in range (1,len(sheet.col_values(1))+1):
                if sheet.cell(l,5).value == str(update.message.chat_id) :
                    await update.message.reply_text(f'مقدار فعلی کمک این ماه شما {sheet.cell(l,3).value} تومان است مقدار صحیح را وارد کنید')
                    m = update.message.chat_id

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text('/start \n برای شروع کار با ربات هست و کار خاصی انجام نمیدهد \n /signup \n برای عضویت در گروه خیران است که از شما مبلغی که ماهیانه میخواهید کمک کنید را درخواست میکند حتما این عدد را بدون ۳ رقم آخر و بدون اسپیس و با ارقام انگلیسی وارد کنید برای مثلا برای ۲۰۰ هزار تومان فقط 200 را وارد میکنید و اگر مبلغ شما بالای ۱ میلیون تومان است فقط یک عدد ۴ رقمی باید وارد کنید برای مثال برای ۲ میلیون تومان باید 2000 وارد کنید \n/payoff \n برای گزارش شما از مبلغی که کمک کردید است هر دفعه که کمکی کردید اینجا وارد کنید که به شما یاد آوری اشتباه نشود \n/status \n برای گزارش وضعیت پرداخت شما و مقدار باقی مانده سهم شما در ماه است \n /editshare \n برای اصلاح کردن مبلغی که به عنوان سهم کمک ماهیانه خود وارد کردید استفاده می شود \n /editcontribution \n برای اصلاح مبلغ واردی شما به عنوان کمک است اگر مبلغ کمک کرده شما در ماه اشتباه ثبت شده بود میتوانید از اینجا آن را اصلاح کنید فقط نکات در مورد وارد کردن اعداد را رعایت کنید')



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
    if str(int(datetime.date.today().strftime('%d')) + 10) == '23' or str(int(datetime.date.today().strftime('%d')) + 10) == '26' or str(int(datetime.date.today().strftime('%d')) + 10) == '29' or str(int(datetime.date.today().strftime('%d')) + 10) == '30' and p == 0 :
        for q in range (1,len(sheet.col_values(1))+1):
            if int(sheet.cell(q,2).value) - int(sheet.cell(q,3).value) > 0 :
                await bot.send_message(sheet.cell(q,5).value,f'سلام {sheet.cell(q,1).value} عزیز بدین وسیله به شما یادآوری میشود که هرچه زود تر سهم خود را پرداخت کنید برای مشاهده وضعیت پرداخت خود میتوانید از /status استفاده کنید \n از کمک های شما سپاش گزاریم ❤🌹')
        q = 0 
        p = 1
    if str(int(datetime.date.today().strftime('%d')) + 10) != '23' and str(int(datetime.date.today().strftime('%d')) + 10) != '26' and str(int(datetime.date.today().strftime('%d')) + 10) != '29' and str(int(datetime.date.today().strftime('%d')) + 10) == '30' and p != 0 :
        p = 0


    
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text
    if update.message.chat.last_name == None:
        name: str = update.message.chat.first_name
    else:
        name: str = update.message.chat.first_name + ' ' + update.message.chat.last_name
    chatid : str = update.message.chat_id
    username: str = update.message.chat.username
    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()

        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        processed: str = text.lower()


        if b == update.message.chat_id :
          if text.isnumeric() :
            sheet.insert_row([name,text,'0','0',chatid,username],len(sheet.col_values(1))+1)
            response: str = f'سلام {update.message.chat.first_name} سهم شما در کمک ماهانه {text} تومان ثبت شد برای اصلاح آن میتوانید از /editshare استفاده کنید \nاز کمک های شما متشکریم ❤🌹'
          else:
            response: str = f'ورودی شما اشتباه است حتما دقت کنید ارقام به انگلیسی و بدون اسپیس وارد شده باشند سپس دوباره با استفاده از /signup مقدار سهم خود را وارد کنید'

        elif c == update.message.chat_id :
            sheet.update_cell(d,2,text)
            response: str = f'سهم شما با موفقیت به {sheet.cell(d,2).value} تومان در ماه تغییر یافت برای اصلاح دوباره میتوانید از   /edit استفاده کنید'
            c = 0

        elif f == update.message.chat_id :
            for g in range (1,len(sheet.col_values(1))+1):
                if sheet.cell(g,5).value == str(update.message.chat_id) :
                    if text.isnumeric() :
                        sheet.update_cell(g,3,(int(sheet.cell(g,3).value) + int(text)))
                        sheet.update_cell(g,4,(int(sheet.cell(g,4).value) + int(text)))
                        response: str = f'از کمک های شما سپاش گزاریم ❤🌹 \n برای آگاهی از وضعیت پرداختی این ماه خود میتوانید از  /status استفاده کنید'
                        f = 0
                        
                    else:
                        response: str = f'ورودی شما اشتباه است حتما دقت کنید ارقام به انگلیسی و بدون اسپیس وارد شده باشند سپس دوباره با استفاده از /payoff مقدار پرداختی خود را وارد کنید'
                        h = update.message.chat_id
                        f = 0
            g = 0
        elif m == update.message.chat_id :
            l = 0
            for l in range (1,len(sheet.col_values(1))+1):
                if text.isnumeric() :
                    if sheet.cell(l,5).value == str(update.message.chat_id) :
                        sheet.update_cell(l,4,int(sheet.cell(l,4).value) - int(sheet.cell(l,3).value) + int(text))
                        sheet.update_cell(l,3,text)
                        response: str = f'مبلغ کمک شده شما در این ماه با موفقیت به {(sheet.cell(l,3).value)} تعقییر پیدا کرد برای اصلاح دوباره آن میتوانید از /editcontributon استفاده کنید از کمک های شما متشکریم ❤🌹 \n'
                    else:
                        response: str = f'ورودی شما اشتباه است حتما دقت کنید ارقام به انگلیسی و بدون اسپیس وارد شده باشند سپس دوباره با استفاده از /editcontribution مقدار پرداختی خود را وارد کنید'
            l = 0
            m = 0
        elif a == 0 :
            response: str = 'متوجه نمیشوم برای راهنمایی میتوانید از /help استفاده کنید'


    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)
    i = 0

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')





    






# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('editshare', editshare_command))
    app.add_handler(CommandHandler('status', status_command))
    app.add_handler(CommandHandler('signup', signup_command))
    app.add_handler(CommandHandler('payoff', payoff_command))
    app.add_handler(CommandHandler('editcontribution', editcontribution_command))
    app.add_handler(CommandHandler('help', help_command))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # Log all errors
    app.add_error_handler(error)
    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)


