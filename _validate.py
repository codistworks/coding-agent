import gradio as gr
from app import interface

class TestApp:
    def __init__(self):
        self.interface = interface

    def test_interface(self):
        try:
            self.interface
            print("Interface constructed successfully")
        except Exception as e:
            print(f"Error constructing interface: {e}")

if __name__ == "__main__":
    test_app = TestApp()
    test_app.test_interface()