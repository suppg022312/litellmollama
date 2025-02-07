import os
import sys
import gradio as gr
import traceback
from datetime import datetime
import time
import requests
from typing import List, Dict
import yaml

def load_config() -> Dict:
    """Load configuration from config.yaml"""
    try:
        with open("litellm/proxy_server_config.yaml", "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {"model_list": []}

def format_time(seconds: float) -> str:
    """Format time in seconds to a readable string"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = int(seconds // 60)
    seconds = seconds % 60
    return f"{minutes} minutes {seconds:.2f} seconds"

def save_response_to_file(model: str, response: str, prompt: str) -> str:
    """Save model response to a file and return the filename"""
    # Clean model name for filename
    clean_model = model.replace(':', '_').replace('/', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"test_{clean_model}_{timestamp}.md"
    
    # Add markdown formatting instructions to the prompt
    markdown_template = """# Model Response from {model}
Generated on: {timestamp}

Below is the code solution with proper markdown formatting and copyable code snippets:

{response}

## How to Use
Copy the code snippets above and follow the implementation instructions.
"""
    formatted_content = markdown_template.format(
        model=model,
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        response=response,
        prompt=prompt,
        filename=filename
    )
    
    try:
        with open(filename, 'w') as f:
            f.write(formatted_content)
        return filename
    except Exception as e:
        return f"Error saving file: {str(e)}"

def call_api_endpoint(model: str, prompt: str) -> Dict:
    """Make API call to test the model with the given prompt"""
    try:
        # Get API base URL from config
        config = load_config()
        model_config = next((m for m in config["model_list"] if m["model_name"] == model), None)
        
        if not model_config:
            return {
                "success": False,
                "response": None,
                "error": f"Model {model} not found in config"
            }
        
        api_base = model_config["litellm_params"]["api_base"]
        actual_model = model_config["litellm_params"]["model"]
        
        # Add markdown formatting instructions to the prompt
        enhanced_prompt = f"""Please provide a solution to the following task using proper markdown formatting. 
Include code snippets wrapped in triple backticks with the appropriate language identifier.
Make the code easily copyable and include clear section headers.

Task: {prompt}

Format your response with:
1. Clear markdown headers (##)
2. Code snippets in ```language
3. Brief explanations before and after code blocks
4. Any necessary setup or installation instructions
5. Example usage if applicable
"""
        
        # Construct API request for Ollama
        url = f"{api_base}/api/generate"
        headers = {
            "Content-Type": "application/json"
        }
        
        # Ollama format
        data = {
            "model": actual_model.split('/')[-1],
            "prompt": enhanced_prompt,
            "stream": False
        }
        
        # Make API call
        print(f"Calling API: {url}")
        print(f"Request data: {data}")
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        # Check if response is valid JSON
        try:
            response_json = response.json()
        except json.JSONDecodeError as e:
            return {
                "success": False,
                "response": None,
                "error": f"Invalid JSON response: {str(e)}\nResponse text: {response.text}"
            }
        
        return {
            "success": True,
            "response": response_json,
            "error": None
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "response": None,
            "error": f"API Error: {str(e)}\nURL: {url}\nRequest: {data}"
        }
    except Exception as e:
        return {
            "success": False,
            "response": None,
            "error": f"Unexpected error: {str(e)}"
        }

def get_available_models() -> List[str]:
    """Get list of available models from config"""
    config = load_config()
    return [model["model_name"] for model in config["model_list"]]

def test_against_all_models(task: str, progress=gr.Progress()) -> str:
    """Test the given task against all available models"""
    results = []
    created_files = []
    start_time = datetime.now()
    
    # Header
    results.append(
        f"Starting task execution at {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Task: {task}\n"
    )
    
    # Get available models
    models = get_available_models()
    total_models = len(models)
    
    if not models:
        return "Error: No models found in config.yaml"
    
    results.append(f"Total models to test: {total_models}\n{'='*50}\n")
    
    # Test each model
    for idx, model in enumerate(models, 1):
        try:
            model_start_time = time.time()
            progress(idx/total_models, desc=f"Testing model {idx}/{total_models}: {model}")
            
            results.append(f"\nTesting model ({idx}/{total_models}): {model}")
            results.append(f"Sending request...")
            
            # Call API with timeout
            api_result = call_api_endpoint(model, task)
            execution_time = time.time() - model_start_time
            
            if api_result["success"]:
                response_data = api_result["response"]
                # Extract response text - Ollama format
                response_text = response_data.get("response", "No response content")
                
                # Save response to file
                filename = save_response_to_file(model, response_text)
                created_files.append(filename)
                
                results.extend([
                    "✅ API call successful",
                    f"Execution time: {format_time(execution_time)}",
                    f"Response saved to: {filename}",
                    f"{'='*50}\n"
                ])
            else:
                results.extend([
                    "❌ API call failed",
                    f"Execution time: {format_time(execution_time)}",
                    "Error:",
                    api_result["error"],
                    f"{'='*50}\n"
                ])
            
        except Exception as e:
            results.extend([
                f"❌ Error processing model {model}:",
                str(e),
                traceback.format_exc(),
                f"{'='*50}\n"
            ])
            continue
        
        # Update progress after each model
        progress_text = "\n".join(results)
        yield progress_text
    
    # Add summary
    end_time = datetime.now()
    execution_duration = (end_time - start_time).total_seconds()
    results.extend([
        f"\nExecution Summary:",
        f"Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Finished: {end_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total duration: {format_time(execution_duration)}",
        f"Models tested: {total_models}",
        f"Successful files created: {len(created_files)}",
        "\nCreated files:",
        *[f"- {f}" for f in created_files],
        f"\nTask completed!"
    ])
    
    return "\n".join(results)

# Importing StringIO here since it's used in multiple functions
from io import StringIO

# Create the Gradio interface
with gr.Blocks(title="Model Task Tester") as interface:
    gr.Markdown(
        """
        # Model Task Tester
        Test your task against all configured models
        
        Current models (from config.yaml):
        {}
        """.format("\n".join(f"- {model}" for model in get_available_models()))
    )
    
    with gr.Row():
        task_input = gr.Textbox(
            label="Enter your task",
            placeholder="Describe what you want the models to do...",
            lines=3
        )
    
    test_btn = gr.Button("Run Task Against All Models")
    
    execution_output = gr.Textbox(
        label="Execution Results", 
        interactive=False,
        lines=20
    )
    
    test_btn.click(
        fn=test_against_all_models,
        inputs=[task_input],
        outputs=[execution_output]
    )

if __name__ == "__main__":
    try:
        import yaml
    except ImportError:
        print("Installing PyYAML...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyYAML"])
        import yaml
    
    # Get the actual network IP address
    import socket
    def get_local_ip():
        try:
            # Create a socket that connects to an external server
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "Could not determine IP"
    
    local_ip = get_local_ip()
    print(f"\nTo access from another PC on your network, use: http://{local_ip}:7870\n")
    
    interface.launch(
        server_name="0.0.0.0",
        server_port=7870,
        share=False,
        inbrowser=True,
        show_error=True,
        debug=True
    )
