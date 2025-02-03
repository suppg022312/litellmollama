import gradio as gr
import requests
import yaml
from pathlib import Path

# Read and sort models from proxy config
proxy_config_path = Path("litellm/proxy_server_config.yaml")
with open(proxy_config_path) as f:
    config = yaml.safe_load(f)
    
models = sorted([model["model_name"] for model in config["model_list"]])

def query_model(prompt, selected_model, progress=gr.Progress(), history=gr.State([])):  # Initialize with empty list
    headers = {
        "Content-Type": "application/json",
        # No authorization needed
    }
    
    data = {
        "model": selected_model,
        "messages": [
            {"role": "system", "content": "You are a helpful coding assistant"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "stream": False
    }
    
    try:
        progress(0, desc="Sending request to model...")
        response = requests.post(
            "http://dockerdev:4000/v1/chat/completions",  # Correct proxy endpoint
            headers=headers,
            json=data
        )
        response.raise_for_status()
        
        # Generate filename with timestamp, model name and response time
        from datetime import datetime
        import time
        start_time = time.time()
        # Calculate response time in milliseconds
        response_time = int((time.time() - start_time) * 1000)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_model_name = selected_model.replace("/", "_").replace(":", "-")
        filename = f"project_{safe_model_name}_{timestamp}_timetaken{response_time}ms.py"
        
        # Save response to file
        code_content = response.json()['choices'][0]['message']['content']
        with open(filename, "w") as f:
            f.write(code_content)
            
        # Add new entry to history (time, model, truncated prompt)
        from datetime import datetime
        new_entry = [[
            datetime.now().strftime("%H:%M:%S"), 
            selected_model,
            (prompt[:47] + "...") if len(prompt) > 50 else prompt
        ]]
        updated_history = history.value + new_entry  # Access .value for State object
        history.value = updated_history  # Update State value
        
        return [
            f"```markdown\n{code_content}\n```",
            f"✅ File saved as: {filename} (Response time: {response_time}ms)",
            updated_history
        ]
    except Exception as e:
        return [f"Error: {str(e)}", "", history]  # Maintain 3 return values even on error

css = """
.gradio-container { max-width: 900px !important; }
.progress-bar { background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 100%) !important; }
button#component-8 { background: #4CAF50 !important; color: white !important; border: none !important; }
.markdown-body { padding: 15px; border-radius: 5px; background: #f8f9fa; border: 1px solid #dee2e6; }
"""

with gr.Blocks(css=css, theme=gr.themes.Default()) as interface:
    gr.Markdown("# LLM Proxy Tester\nTest different models through the LiteLLM proxy")
    
    with gr.Row():
        # Left column for history
        with gr.Column(scale=1):
            history = gr.DataFrame(
                headers=["Time", "Model", "Prompt"],
                label="History",
                interactive=False,
                row_count=(3, "dynamic"),
                col_count=(3, "fixed")
            )
            
        # Right column for inputs/outputs
        with gr.Column(scale=3):
            with gr.Row():
                prompt = gr.Textbox(lines=3, label="Prompt", placeholder="Enter your coding request...")
                model_select = gr.Dropdown(models, label="Model", value=models[0] if models else "")
            
            submit_btn = gr.Button("Submit", variant="primary")
            
            response = gr.Markdown(label="Model Response", elem_classes=["markdown-body"])
            status = gr.Textbox(label="Status", interactive=False, visible=False, elem_classes=["status-box"])

    submit_btn.click(
        fn=query_model,
        inputs=[prompt, model_select],
        outputs=[response, status, history]
    )
    
    status.change(
        lambda x: gr.Textbox(value=x, visible=bool(x)), 
        inputs=[status], 
        outputs=[status]
    )
    
    gr.HTML("""
    <style>
        .status-box {
            margin-top: 15px;
            padding: 10px;
            border-radius: 5px;
            background: #e8f5e9;
            color: #1b5e20;
            border: 1px solid #a5d6a7;
        }
    </style>
    """)

if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=7861,
        inbrowser=True,
        show_error=True,
        debug=True,
        share=False,  # Explicitly disable public sharing
        prevent_thread_lock=True  # Keep the interface responsive
    )
