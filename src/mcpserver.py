from fastapi import FastAPI
from pydantic import BaseModel
from jinja2 import Template
import os

app = FastAPI()

PROMPT_DIR = "prompts"


# request body
class PromptRequest(BaseModel):
    name: str
    code: str



def load_template(name: str):
    path = os.path.join(PROMPT_DIR, f"{name}.jinja")
    print(path)
    if not os.path.exists(path):
        raise Exception(f"Prompt {name} not found")

    with open(path, "r") as f:
        return f.read()


@app.post("/prompt")
def render_prompt(req: PromptRequest):
    template_str = load_template(req.name)
    print(template_str)
    template = Template(template_str)

    rendered = template.render(code="abc")

    return {
        "prompt": rendered
    }