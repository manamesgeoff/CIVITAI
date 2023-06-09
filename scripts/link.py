import gradio as gr

import civitai.link as link

from modules import shared, script_callbacks

def connect_to_civitai(demo: gr.Blocks, app):
    key = shared.opts.data.get("civitai_link_key", None)
    # If key is empty or not set, don't connect to Civitai Link
    if not key: return

    link.log('Connecting to Civitai Link Server')
    link.socketio_connect()
    link.join_room(key)

script_callbacks.on_app_started(connect_to_civitai)

