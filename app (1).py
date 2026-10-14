import gradio as gr
import random

def new_game():
    return "🐍 Welcome to Snake Game! Press Start to begin.", 0

def start_game():
    return "🎮 Game started! This is a starter screen. Add your original game logic here.", 0

with gr.Blocks(title="Snake Game") as demo:
    gr.Markdown("# 🐍 Snake Game")
    gr.Markdown("A simple game page for your exhibition.")
    status = gr.Textbox(label="Game Status", value="Ready to play")
    score = gr.Number(label="Score", value=0, interactive=False)
    start = gr.Button("Start Game")
    reset = gr.Button("Reset")

    start.click(start_game, outputs=[status, score])
    reset.click(new_game, outputs=[status, score])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
