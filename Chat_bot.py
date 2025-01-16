


    
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from transformers import pipeline

# Load the LLM model (TinyLlama)
llm = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Bot token from BotFather
API_TOKEN = "7288077717:AAE0O3-NnQnYzSsccrHtA1v8WqOtJ0iUhvM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hello! I'm Pepe, your AI assistant. Ask me anything!")

async def process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process the user message."""
    user_message = update.message.text
    await update.message.reply_text("Processing your query...")

    # Preprocess the user message if needed (strip unnecessary spaces)
    user_message = user_message.strip()

    # Generate response with adjusted parameters (max_length, temperature, top_k, top_p)
    response = llm(user_message, max_length=200, do_sample=True, temperature=0.7, top_k=50, top_p=0.9)

    # Get the generated text and print it for debugging
    generated_text = response[0]['generated_text']
    print(f"Model response: {generated_text}")  # Debugging line

    # Send the response back to the user
    await update.message.reply_text(generated_text)

def main() -> None:
    application = Application.builder().token(API_TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()


