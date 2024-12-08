from litellm import completion
import gradio as gr
import os

os.environ['GROQ_API_KEY'] = ""

def main_ui():
    def gradio_summarize(input_text):
        response = completion(
          model="groq/llama3-8b-8192",
          messages=[
            {"role": "user", "content": "Summarize this text into one short sentence:/n" + input_text}
        ],
        )
        response_text = response.choices[0].message.content
        return response_text

    with gr.Blocks() as demo:
        gr.Markdown("## Text Summarization App")
        gr.Markdown("Enter text in English to generate a summary using LLM.")

        with gr.Row():
            input_box = gr.Textbox(label="Input Text", lines=10, placeholder="Enter your text here...")
            output_box = gr.Textbox(label="Summary", lines=10, interactive=False)

        submit_button = gr.Button("Summarize")

        submit_button.click(gradio_summarize, inputs=input_box, outputs=output_box)

    demo.launch()

if __name__ == "__main__":
    main_ui()
