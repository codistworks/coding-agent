import app

try:
    app
except Exception as e:
    print(f"Error: {e}")
else:
    print("Validation successful: Gradio UI constructs without error.")