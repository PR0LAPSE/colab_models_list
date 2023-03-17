import os
import requests
import gradio as gr
from modules import scripts, script_callbacks

def on_ui_tabs():     
    with gr.Blocks() as colab_models_list:
        html_url = "https://raw.githubusercontent.com/PR0LAPSE/colab_models_list/main/scripts/models.html"
        html_text = requests.get(html_url).text
        gr.HTML(f"{html_text}")
    return (colab_models_list, "описание моделей", "colab_models_list"),

script_callbacks.on_ui_tabs(on_ui_tabs)
