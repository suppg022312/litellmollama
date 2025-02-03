import os
import importlib.util
import sys
from pathlib import Path
import gradio as gr
import traceback
import re
import subprocess
import pkg_resources

def install_package(package):
    """Install a Python package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def get_required_imports(code_content):
    """Extract import statements from the code"""
    imports = []
    lines = code_content.split('\n')
    for line in lines:
        if line.startswith('import '):
            imports.extend(line.replace('import ', '').split(','))
        elif line.startswith('from '):
            module = line.split(' import ')[0].replace('from ', '')
            imports.append(module)
    return [imp.strip().split('.')[0] for imp in imports]

def ensure_dependencies(code_content):
    """Check and install required packages"""
    required_imports = get_required_imports(code_content)
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    missing_packages = []
    installation_status = []

    for package in required_imports:
        if package not in ['os', 'sys', 'pathlib', 're', 'time', 'datetime', 'json', 'math']:
            if package not in installed_packages:
                missing_packages.append(package)
                status = install_package(package)
                installation_status.append(f"Installing {package}: {'Success' if status else 'Failed'}")

    return installation_status

def list_generated_files():
    """List all generated project files in the current directory"""
    files = [f for f in os.listdir('.') if f.startswith('project_') and f.endswith('.py')]
    return sorted(files, reverse=True)  # Most recent first

def extract_python_code(content):
    """Extract Python code from between triple backticks"""
    # Try to find Python code blocks
    python_blocks = re.findall(r'```(?:python)?\n(.*?)```', content, re.DOTALL)
    
    if python_blocks:
        # Return the first Python code block found
        return python_blocks[0].strip()
    else:
        # If no code blocks found, try to extract just the Python code
        # Remove any markdown-style text before the first Python-like line
        lines = content.split('\n')
        code_lines = []
        started = False
        
        for line in lines:
            # Look for typical Python code indicators
            if not started and (line.startswith('import ') or 
                              line.startswith('from ') or 
                              line.startswith('def ') or 
                              line.startswith('class ') or
                              line.startswith('#')):
                started = True
            
            if started:
                code_lines.append(line)
        
        if code_lines:
            return '\n'.join(code_lines).strip()
        
        # If still no code found, return the original content
        return content.strip()

def load_code_content(file_path):
    """Load and return the content of a Python file"""
    with open(file_path, 'r') as f:
        content = f.read()
        return extract_python_code(content)

def execute_code(code_content, output_capture):
    """Execute the code and capture its output"""
    try:
        # Install any missing dependencies
        installation_status = ensure_dependencies(code_content)
        if installation_status:
            print("\nDependency Installation Results:")
            for status in installation_status:
                print(status)
            print()

        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        sys.stdout = output_capture
        
        # Execute the code in a new namespace
        namespace = {}
        exec(code_content, namespace)
        
        status = "Code executed successfully!"
        if installation_status:
            status += f"\n\nInstalled dependencies:\n" + "\n".join(installation_status)
        
        return status, ""
    except Exception as e:
        return "Error during execution!", f"Error: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
    finally:
        # Restore stdout
        sys.stdout = old_stdout

def test_code(selected_file):
    if not selected_file:
        return "Please select a file to test", "", ""
    
    # Load the code content
    code_content = load_code_content(selected_file)
    
    # Prepare output capture
    from io import StringIO
    output_capture = StringIO()
    
    # Execute the code
    status, error = execute_code(code_content, output_capture)
    
    # Get captured output
    output = output_capture.getvalue()
    output_capture.close()
    
    return (
        f"Status: {status}",
        f"Code Content:\n```python\n{code_content}\n```",
        f"Output:\n{output}\nErrors:\n{error}"
    )

# Create the Gradio interface
with gr.Blocks(title="Generated Code Tester") as interface:
    gr.Markdown("# Generated Code Tester\nTest the code generated by different models")
    
    with gr.Row():
        file_dropdown = gr.Dropdown(
            choices=list_generated_files(),
            label="Select a file to test",
            interactive=True
        )
    
    test_btn = gr.Button("Test Code")
    
    status_output = gr.Textbox(label="Status", interactive=False)
    code_display = gr.Markdown(label="Code Content")
    execution_output = gr.Textbox(
        label="Execution Output", 
        interactive=False,
        lines=10
    )
    
    test_btn.click(
        fn=test_code,
        inputs=[file_dropdown],
        outputs=[status_output, code_display, execution_output]
    )

if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=7862,  # Different port from the main app
        inbrowser=True,
        show_error=True,
        debug=True,
        share=False
    )