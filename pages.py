import customtkinter as ctk

def show_chat(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "🤖 Welcome to Future AI!\n\n")
    chatbox.insert("end", "You're in Chat Mode.\n")


def show_research(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "🔍 Research Mode\n\n")
    chatbox.insert("end", "Soon you'll be able to research anything.\n")


def show_learn(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "📚 Learning Mode\n\n")
    chatbox.insert("end", "Future AI will become your personal teacher.\n")


def show_images(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "🎨 Image Generation\n\n")
    chatbox.insert("end", "Soon you'll create amazing AI images.\n")


def show_brainstorm(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "💡 Brainstorm Mode\n\n")
    chatbox.insert("end", "Let's create business ideas, apps and more.\n")


def show_websites(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "🌐 Website Builder\n\n")
    chatbox.insert("end", "Future AI will build websites here.\n")


def show_settings(chatbox):
    chatbox.delete("1.0", "end")
    chatbox.insert("end", "⚙️ Settings\n\n")
    chatbox.insert("end", "Customize Future AI here.\n")
