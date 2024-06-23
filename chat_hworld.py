# from : https://google.github.io/mesop/

import random
import time

import mesop as me
import mesop.labs as mel


@me.page(
    path="/chat",
    title="Mesop Demo Chat",
)
def page():
    mel.chat(transform, title="Demo Chat", bot_user="Hello World Bot")


def transform(input: str, history: list[mel.ChatMessage]):
    joke = random.sample(LINES, random.randint(3, len(LINES) - 1))[0]
    time.sleep(0.3)
    yield joke


LINES = [
    "Why do Python programmers prefer dark mode? Because light typing is harder on the eyes!",
    "What's a programmer's favorite type of music? Code beats – it’s all in the loops and rhythms!",
    "How does a Python programmer celebrate their birthday? They get another 'self' to party with!",
    "Why don't Python programmers like to take vacations? Because they can't find any break statements that work for "
    "them!",
    "What did the Python programmer say to his date at dinner? Let me just debug this conversation real quick.",
    "How do you know a programmer is lying about their code being clean and simple? They’ll start talking in loops "
    "and conditionals.",
    "Why was the Python programmer late for work? His interpreter ran out of memory!",
    "What's a programmer's favorite type of weather? Rainy – it gives them an excuse to stay indoors and code more!",
    "How do you know someone is a Python programmer? They always have a 'if __name__ == '__main__':' joke up their "
    "sleeve.",
    "Why did the Python programmer get locked out of his house? He forgot the password to his own keypad!",
    "What do you call an angry Python programmer? A snake in a loop – it’s always coiling back on itself!",
    "How does a Python programmer celebrate their first successful compile? They throw a 'Syntax' party!",
    "Why did the Python programmer get kicked out of bed at night? Because his code was too complex to sleep through!",
    "What do you call a programmer who only likes one language? A mono-lingual coder – they're all about that single "
    "syntax life!",
    "Why did the Python program fail its driving test? It couldn’t parallel process any instructions!",
    "How does a Python programmer celebrate their first successful deployment? They raise a 'print()' toast!",
    "What do you call a programmer who only likes to work at night? A nocturnal coder – they're always in the dark "
    "until morning light!",
]
