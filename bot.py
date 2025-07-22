import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ReplyKeyboardMarkup

# Load user data from JSON
def load_user_data():
    with open('users.json') as f:
        return json.load(f)

# Start
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to Tadele Bank Bot!\n\n"
        "Use the commands below:\n"
        "/balance - Check your balance\n"
        "/transactions - View transaction history\n"
        "/statement - Get mini statement\n"
        "/support - Talk to support\n"
        "/atm - Nearest ATM\n"
        "/reset - Reset password help\n"
        "/loan - Loan due date"
    )

# 1️⃣ Check Balance
def check_balance(update: Update, context: CallbackContext):
    users = load_user_data()
    user_id = "1001"  # Simulated user
    user = users.get(user_id)
    if user:
        update.message.reply_text(f"{user['name']}, your balance is: {user['balance']} ETB")
    else:
        update.message.reply_text("User not found.")

# 2️⃣ Transaction History
def transactions(update: Update, context: CallbackContext):
    users = load_user_data()
    user = users.get("1001")
    if user:
        response = f"📊 {user['name']} - Transaction History:\n\n"
        for t in user["transactions"]:
            response += f"{t['date']} - {t['type'].capitalize()} - {t['amount']} ETB\n"
        update.message.reply_text(response)
    else:
        update.message.reply_text("No data found.")

# 3️⃣ Mini Statement
def mini_statement(update: Update, context: CallbackContext):
    users = load_user_data()
    user = users.get("1001")
    if user:
        response = f"🧾 Mini Statement for {user['name']}:\n\n"
        last = user['transactions'][-3:]  # Last 3 transactions
        for t in last:
            response += f"{t['date']} - {t['type']} - {t['amount']} ETB\n"
        update.message.reply_text(response)
    else:
        update.message.reply_text("No statement found.")

# 4️⃣ Customer Support
def support(update: Update, context: CallbackContext):
    update.message.reply_text("🤝 Contact our support team at: +251-911-000000 or support@bank.com")

# 5️⃣ Nearest ATM Info
def atm_info(update: Update, context: CallbackContext):
    update.message.reply_text("🏧 The nearest ATM is at: Addis Ababa, Piassa Branch.\nUse Google Maps for directions.")

# 6️⃣ Password/Pin Reset
def reset_help(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔐 To reset your password or PIN:\n"
        "1. Visit your nearest branch OR\n"
        "2. Call customer service: +251-911-000000"
    )

# 7️⃣ Loan Due Date
def loan_due(update: Update, context: CallbackContext):
    users = load_user_data()
    user = users.get("1001")
    if user and "loan_due" in user:
        update.message.reply_text(f"🗓️ Your next loan payment is due on {user['loan_due']}.")
    else:
        update.message.reply_text("No loan information found.")


def menu(update: Update, context: CallbackContext):
    keyboard = [
        ["/balance", "/statement"],
        ["/transactions", "/loan"],
        ["/support", "/atm", "/reset"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=False)
    update.message.reply_text("🔁 Main Menu:", reply_markup=reply_markup)

# Register in your main()
# dp.add_handler(CommandHandler("menu", menu))

# Main function
def main():
    updater = Updater("7604878367:AAFmstkykaZ6McOyfnEwMkqr7gbc2_4S4V8")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("balance", check_balance))
    dp.add_handler(CommandHandler("transactions", transactions))
    dp.add_handler(CommandHandler("statement", mini_statement))
    dp.add_handler(CommandHandler("support", support))
    dp.add_handler(CommandHandler("atm", atm_info))
    dp.add_handler(CommandHandler("reset", reset_help))
    dp.add_handler(CommandHandler("loan", loan_due))
    dp.add_handler(CommandHandler("menu", menu))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
