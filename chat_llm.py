import mesop as me
import mesop.labs as mel
from mesop.server import server

from Llm import llm, prompt_template


@me.page(
    path="/chat",
    title="Wizardry Whisperer",
)
def page():
    mel.chat(transform, title="Wizardry Whisperer", bot_user="The Wizard")


def transform(input: str, history: list[mel.ChatMessage]):
    qry = prompt_template.format(question=input)
    response = llm.invoke(qry)
    yield response


'''
if __name__ == '__main__':
    server.run()
'''
