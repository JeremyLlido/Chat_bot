
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from transformers import pipeline

# Initialize the text-generation model
llm = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Telegram bot token
API_TOKEN = "7288077717:AAE0O3-NnQnYzSsccrHtA1v8WqOtJ0iUhvM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command by sending a greeting message."""
    await update.message.reply_text("Hi! I'm Jeremy_Bot, your AI assistant. How can I help you?")

async def process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming user messages and generates responses."""
    user_message = update.message.text.strip()  # Clean up user input
    await update.message.reply_text("...")  # Acknowledge receipt of the message

    # Generate a response using the language model
    response = llm(
        user_message,
        max_length=200,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
    )

    # Extract the generated text
    generated_text = response[0]['generated_text']
    print(f"Debug: Generated response: {generated_text}")  # Log the model's output for debugging

    # Send the generated text back to the user
    await update.message.reply_text(generated_text)

def main() -> None:
    """Sets up and starts the Telegram bot."""
    # Create the application instance
    application = Application.builder().token(API_TOKEN).build()

    # Register handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))

    # Start polling to receive updates
    application.run_polling()

if __name__ == "__main__":
    main()
