import mesop as me
import mesop.labs as mel

from Llm import llm, prompt_template


@me.page(
    path="/chat",
    title="Talk to Knowledge",
)
def page():
    mel.chat(transform, title="Talk to Knowledge", bot_user="Bot without memory")


def transform(input: str, history: list[mel.ChatMessage]):
    qry = prompt_template.format(question=input)
    response = llm.invoke(qry)
    yield response


