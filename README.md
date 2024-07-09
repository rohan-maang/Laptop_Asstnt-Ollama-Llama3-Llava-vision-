# Virtual Assistant

This project is a voice-controlled assistant inspired by the character Wednesday Addams. It can transcribe speech, respond with dark humor, take screenshots, and interact with the clipboard.

## Features

- **Voice Activation**: Wake word ("Wednesday") to activate the assistant.
- **Voice Commands**: Recognizes commands to take screenshots, read clipboard content, and respond with predefined instructions.
- **Dark Humor**: Responds with a dark, Wednesday Addams-like tone.
- **Screenshot Capture**: Takes screenshots and processes them for analysis.
- **Clipboard Interaction**: Reads and processes clipboard content.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Required Libraries

You can install the required libraries using `pip`:

```bash
pip install speechrecognition pyautogui pyperclip ollama

## Step-by-Step Installation

	1.	Clone the Repository:

  ```bash
git clone https://github.com/your_username/Virtual_Assistant.git
cd Virtual_Assistant

2.	Install the Dependencies:

  ```bash
pip install -r requirements.txt

## Usage

Running the Assistant

	1.	Ensure your microphone is connected and working.
	2.	Run the assistant.py script.
	3.	Speak the wake word (“Wednesday”) to activate the assistant.
	4.	Give voice commands to interact with the assistant.

Voice Commands

	•	Activate: Say “Wednesday” to activate the assistant.
	•	Sleep: Say “sleep” to deactivate the assistant.
	•	Take Screenshot: Say “take a screenshot” or any phrase indicating a screenshot request.
	•	Clipboard Content: Say “read the clipboard” or any phrase indicating clipboard interaction.

## Example Commands

	•	Taking a Screenshot:
	•	User: “Wednesday, can you take a screenshot?”
	•	Assistant: “Getting the screenshot.”
	•	Reading Clipboard Content:
	•	User: “Wednesday, can you read the clipboard?”
	•	Assistant: “Copying from the clipboard.”

