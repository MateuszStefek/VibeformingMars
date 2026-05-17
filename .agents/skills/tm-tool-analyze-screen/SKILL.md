# tm-tool-analyze-screen

This skill allows Gemini CLI to interactively capture and analyze your screen.

## Instructions
- When the user asks to "capture the screen", "see this", or "analyze the screenshot":
  1. ALWAYS run the script `.agents/skills/tm-tool-analyze-screen/capture.sh` using the `run_shell_command` tool (wait for exit).
  2. The script will return the absolute path to the captured image.
  3. ALWAYS read that file path using the `read_file` tool.
  4. Use the visual information from the image to answer the user's request.
- This skill handles both the "Eyes" (capture) and the "Brain" (analysis) in one sequence.

## Usage
"Capture the screen and tell me which corporation is better for these cards."
"Analyze my current hand."
"Look at this error message."
