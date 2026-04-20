import tkinter as tk
import random
from datetime import datetime

name = ""

# ---------- Chatbot Logic ----------
def bot_reply(user_input):
    global name
    user = user_input.lower()

    if "hello" in user or "hi" in user:
        return "Hello! 👋 What is your name?"

    elif "my name is" in user:
        name = user.replace("my name is", "").strip()
        return f"Nice to meet you, {name}!"

    elif "my name" in user:
        return f"Your name is {name}" if name else "I don't know your name yet."

    elif "how are you" in user:
        return random.choice([
            "I'm doing great!",
            "All good 😄",
            "Feeling awesome!"
        ])

    elif "time" in user:
        return "Current time: " + datetime.now().strftime("%H:%M:%S")

    elif "study" in user:
        return "Stay consistent and revise daily 👍"

    elif "code" in user or "coding" in user:
        return "Practice daily and build projects 🚀"

    elif "joke" in user:
        return random.choice([
            "Why do programmers hate bugs? Because they bug them!",
            "I would tell you a joke, but it's still compiling 😄"
        ])

    elif "motivate" in user:
        return "You can do it! Small steps every day 💪"

    elif "news" in user:
        return random.choice([
            "Recent news: AI technology is growing rapidly worldwide.",
            "Global focus is on climate change and renewable energy.",
            "Tech companies are investing heavily in AI and automation."
        ])

    elif "bye" in user:
        return "Goodbye! 👋"

    else:
        return "I'm still learning 🤖"

# ---------- Send Message ----------
def send_message(event=None):
    user_msg = entry.get().strip()
    if user_msg == "":
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_msg}\n")

    reply = bot_reply(user_msg)
    chat_box.insert(tk.END, f"Bot: {reply}\n\n")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

    entry.delete(0, tk.END)

# ---------- GUI ----------
root = tk.Tk()
root.title("Advanced Mini GPT Chatbot")
root.geometry("520x600")
root.configure(bg="#1e1e1e")

# Chat area
chat_box = tk.Text(root, bg="#2b2b2b", fg="white", font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state=tk.DISABLED)

# Bottom frame (fix typing issue)
bottom_frame = tk.Frame(root, bg="#1e1e1e")
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(bottom_frame, bg="#3c3f41", fg="white", font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10))
entry.focus()

send_btn = tk.Button(bottom_frame, text="Send", command=send_message, bg="#4CAF50", fg="white")
send_btn.pack(side=tk.RIGHT)

# Enter key support
entry.bind("<Return>", send_message)

# Run app
root.mainloop()
