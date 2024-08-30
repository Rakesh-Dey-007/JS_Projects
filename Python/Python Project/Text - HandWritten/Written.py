import pywhatkit as kit

text = "Hello, World!"
kit.text_to_handwriting(text, "written.png", [0, 0, 138])  # Convert text to handwritten text with blue color
print("END")