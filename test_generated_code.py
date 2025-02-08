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
    """Load available models from the LiteLLM API endpoint"""
    try:
        response = requests.get("http://dockerdev:4000/v1/models")
        response.raise_for_status()
        
        # Transform the API response into the expected format
        models_data = response.json()
        return {
            "model_list": [
                {
                    "model_name": model["id"],
                    "litellm_params": {
                        "model": model["id"],
                        "api_base": "http://dockerdev:4000"
                    }
                }
                for model in models_data["data"]
            ]
        }
    except Exception as e:
        print(f"Error loading models from API: {e}")
        return {"model_list": []}

def format_time(seconds: float) -> str:
    """Format time in seconds to a readable string"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = int(seconds // 60)
    seconds = seconds % 60
    return f"{minutes} minutes {seconds:.2f} seconds"

def create_test_session_folder() -> str:
    """Create a unique folder for this test session"""
    # Generate a unique folder name using timestamp and random words
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create a descriptive folder name using timestamp
    folder_name = f"test_session_{timestamp}"
    
    try:
        # Create the folder
        os.makedirs(folder_name, exist_ok=True)
        
        # Move any existing .md files from previous runs
        for file in os.listdir('.'):
            if file.endswith('.md'):
                try:
                    shutil.move(file, os.path.join(folder_name, file))
                except Exception as e:
                    print(f"Could not move file {file}: {e}")
        
        return folder_name
    except Exception as e:
        print(f"Error creating session folder: {e}")
        return "."  # Return current directory as fallback

def save_response_to_file(model: str, response: str, prompt: str, session_folder: str) -> str:
    """Save model response to a file and return the filename"""
    clean_model = model.replace(':', '_').replace('/', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"test_{clean_model}_{timestamp}.md"
    filepath = os.path.join(session_folder, filename)
    
    # Add copy button HTML/CSS styling
    copy_button_style = """
<style>
.copy-button {
    position: absolute;
    top: 5px;
    right: 5px;
    padding: 5px 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    z-index: 1;
}
.code-container {
    position: relative;
    margin: 10px 0;
}
.copy-button:hover {
    background-color: #45a049;
}
.copy-button:active {
    background-color: #3d8b40;
}
</style>

<script>
function copyCode(buttonElement) {
    const codeBlock = buttonElement.parentElement.querySelector('code');
    const range = document.createRange();
    range.selectNode(codeBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    try {
        document.execCommand('copy');
        buttonElement.textContent = 'Copied!';
        setTimeout(() => {
            buttonElement.textContent = 'Copy';
        }, 2000);
    } catch(e) {
        console.error('Failed to copy text:', e);
        buttonElement.textContent = 'Failed to copy';
    }
    window.getSelection().removeAllRanges();
}
</script>
"""

    # Function to wrap code blocks with copy button
    def add_copy_button(match):
        code_block = match.group(0)
        lang = ""
        if "```" in code_block:
            first_line = code_block.split("\n")[0]
            lang = first_line.replace("```", "").strip()
        
        wrapped_block = f'''<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
{code_block}
</div>'''
        return wrapped_block
    
    # Process the response to add copy buttons to all code blocks
    import re
    processed_response = re.sub(r'```[\s\S]*?```', add_copy_button, response)

    # Extract all code blocks for summary
    code_blocks = re.findall(r'```(?:\w+)?\n([\s\S]*?)```', response)
    
    # Create the complete summary of all necessary code
    code_summary = "\n\n".join(code_blocks)
    
    markdown_content = f"""# Model Response: {model}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{copy_button_style}

## Original Task
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```
{prompt}
```
</div>

## Model Solution
{processed_response}

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: {model}
# Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{code_summary}
```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: {model}
- Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- File: {filename}
"""
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        return filepath
    except Exception as e:
        return f"Error saving file: {str(e)}"

def call_api_endpoint(model: str, prompt: str) -> Dict:
    """Make API call to test the model with the given prompt"""
    try:
        url = "http://dockerdev:4000/v1/chat/completions"
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
        
        print(f"Calling API: {url}")
        print(f"Request data: {data}")
        
        response = requests.post(
            url, 
            headers=headers, 
            json=data, 
            timeout=300  # 5 minute timeout
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "response": {
                "response": response.json()["choices"][0]["message"]["content"]
            },
            "error": None
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "response": None,
            "error": f"Request timed out after 300 seconds for model {model}"
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
            "error": f"Unexpected error: {str(e)}\n{traceback.format_exc()}"
        }

def get_available_models() -> List[str]:
    """Get list of available models from config"""
    config = load_config()
    return [model["model_name"] for model in config["model_list"]]

def create_summary_file(task: str, model_results: List[Dict], execution_time: float, session_folder: str) -> str:
    """Create a summary markdown file of all model results"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"summary_report_{timestamp}.md"
    filepath = os.path.join(session_folder, filename)
    
    summary_content = f"""# Model Testing Summary Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Task
```
{task}
```

## Results Summary
- Total Models Tested: {len(model_results)}
- Total Execution Time: {format_time(execution_time)}
- Success Rate: {sum(1 for r in model_results if r['success'])} / {len(model_results)}

## Detailed Results

| Model | Status | Response Time | Details |
|-------|--------|---------------|----------|
"""
    
    for result in model_results:
        status_icon = "✅" if result['success'] else "❌"
        details = result.get('filename', '') if result['success'] else result.get('error', 'Unknown error')
        response_time = format_time(result['execution_time'])
        
        summary_content += f"| {result['model']} | {status_icon} | {response_time} | {details} |\n"

    summary_content += "\n\n## Failed Models Details\n\n"
    failed_models = [r for r in model_results if not r['success']]
    if failed_models:
        for failure in failed_models:
            summary_content += f"""### {failure['model']}
- Error: {failure.get('error', 'Unknown error')}
- Execution Time: {format_time(failure['execution_time'])}
"""
    else:
        summary_content += "No failed models! 🎉\n"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        return filepath
    except Exception as e:
        return f"Error saving summary file: {str(e)}"

def test_against_all_models(task: str, progress=gr.Progress()) -> str:
    """Test the given task against all available models"""
    # Create a new session folder at the start of each test
    session_folder = create_test_session_folder()
    
    results = []
    created_files = []
    model_results = []
    start_time = datetime.now()
    
    # Add session information to results
    results.append(f"Created new test session folder: {session_folder}")
    results.append(f"Starting task execution at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    results.append(f"Task: {task}\n")
    
    # Get available models
    models = get_available_models()
    total_models = len(models)
    
    if not models:
        return "Error: No models found in config.yaml"
    
    results.append(f"Total models to test: {total_models}\n{'='*50}\n")
    
    # Test each model
    for idx, model in enumerate(models, 1):
        model_result = {
            'model': model,
            'success': False,
            'execution_time': 0
        }
        
        try:
            model_start_time = time.time()
            progress(idx/total_models, desc=f"Testing model {idx}/{total_models}: {model}")
            
            results.append(f"\nTesting model ({idx}/{total_models}): {model}")
            results.append(f"Sending request...")
            
            # Call API with timeout
            api_result = call_api_endpoint(model, task)
            execution_time = time.time() - model_start_time
            model_result['execution_time'] = execution_time
            
            if api_result["success"]:
                response_data = api_result["response"]
                response_text = response_data.get("response", "No response content")
                
                filename = save_response_to_file(
                    model=model,
                    response=response_text,
                    prompt=task,
                    session_folder=session_folder
                )
                
                created_files.append(filename)
                model_result['success'] = True
                model_result['filename'] = filename
                
                results.extend([
                    "✅ API call successful",
                    f"Execution time: {format_time(execution_time)}",
                    f"Response saved to: {filename}",
                    f"{'='*50}\n"
                ])
            else:
                error_msg = api_result["error"]
                model_result['error'] = error_msg
                results.extend([
                    "❌ API call failed",
                    f"Execution time: {format_time(execution_time)}",
                    "Error:",
                    error_msg,
                    f"{'='*50}\n"
                ])
            
        except Exception as e:
            error_msg = f"{str(e)}\n{traceback.format_exc()}"
            model_result['error'] = error_msg
            results.extend([
                f"❌ Error processing model {model}:",
                error_msg,
                f"{'='*50}\n"
            ])
        
        model_results.append(model_result)
        progress_text = "\n".join(results)
        yield progress_text
    
    # Create summary file in the session folder
    end_time = datetime.now()
    execution_duration = (end_time - start_time).total_seconds()
    summary_file = create_summary_file(task, model_results, execution_duration, session_folder)
    
    # Get failed models and their errors
    failed_models = [r for r in model_results if not r['success']]
    
    # Create failure summary
    failure_summary = []
    if failed_models:
        failure_summary.extend([
            "\n\n🔍 FAILED MODELS SUMMARY",
            "=======================",
            f"Total Failures: {len(failed_models)} out of {len(models)}",
            "\nDetailed Error Report:"
        ])
        
        for failure in failed_models:
            error_msg = failure.get('error', 'Unknown error')
            # Clean up error message for better readability
            error_msg = error_msg.split('\nURL:')[0]  # Remove URL and request details
            error_msg = error_msg.replace('API Error: ', '')
            
            failure_summary.extend([
                f"\n🔴 Model: {failure['model']}",
                f"   Time: {format_time(failure['execution_time'])}",
                f"   Error: {error_msg}"
            ])
    else:
        failure_summary = ["\n\n✅ All models completed successfully! No failures to report."]
    
    # Add summary to results
    results.extend([
        f"\nExecution Summary:",
        f"Session folder: {session_folder}",
        f"Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Finished: {end_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total duration: {format_time(execution_duration)}",
        f"Models tested: {len(models)}",
        f"Successful files created: {len(created_files)}",
        f"\nSummary report saved to: {summary_file}",
        "\nCreated files:",
        *[f"- {f}" for f in created_files],
        *failure_summary,  # Add the failure summary
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
        def save_task(task):
            """Save the task to a file"""
            try:
                with open("last_task.json", 'w') as f:
                    json.dump({"last_task": task}, f)
            except Exception as e:
                print(f"Error saving task: {e}")

        def load_task():
            """Load the task from a file"""
            try:
                if os.path.exists("last_task.json"):
                    with open("last_task.json", 'r') as f:
                        data = json.load(f)
                        return data.get("last_task", "")
            except Exception as e:
                print(f"Error loading task: {e}")
            return ""

        task_input = gr.Textbox(
            label="Enter your task",
            placeholder="Describe what you want the models to do...",
            lines=3,
            value=load_task()  # Load the last task on startup
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
    print(f"\nTo access from another PC on your network, use: http://{local_ip}:7879\n")
    
    interface.launch(
        server_name="0.0.0.0",
        server_port=7880,
        share=False,
        inbrowser=True,
        show_error=True,
        debug=True
    )
