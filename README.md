# Autonomous CLI Coding Agent

A command-line AI agent built in Python that autonomously navigates a codebase, reads and writes files, executes scripts, and debugs code. It uses the OpenAI SDK via OpenRouter to orchestrate function-calling loops, allowing the LLM to interact directly with the local file system within a secure sandbox.

## Features

* **Autonomous Tool Loop:** Uses an iterative `message.tool_calls` loop to perform multi-step reasoning and actions before returning a final response.
* **Function Calling:**
  * `get_files_info`: Maps directory structures and file sizes.
  * `get_file_content`: Reads source code and text files.
  * `write_file`: Modifies existing code or creates new files.
  * `run_python_file`: Executes Python scripts (e.g., test suites) and captures stdout/stderr.
* **Sandboxed Execution:** Enforces parameter injection at the host level (hardcoding the target directory), ensuring the agent cannot access or modify files outside its designated environment.

## Prerequisites

* Python 3.10+
* [uv](https://docs.astral.sh/uv/) (Python package manager)
* An OpenRouter API Key

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmadyacoub/my_ai_agent
   cd my_ai_agent
   ```

2. **Install dependencies:**

   ```bash
   uv sync
   ```

3. **Configure Environment Variables:**

   Create a `.env` file in the root directory and add your API key:

   ```
   OPENROUTER_API_KEY=your_openrouter_key_here
   ```

## Usage

Run the agent via the CLI, passing your instructions as a prompt. Use the `--verbose` flag to monitor the agent's tool calls and execution results in real-time.

```bash
uv run main.py "Run tests.py and fix any failing tests." --verbose
```

**Example Prompts:**

* `"Fix the bug: 3 + 7 * 2 shouldn't evaluate to 20."`
* `"Explain how the calculator renders results to the console."`
* `"List the contents of the pkg directory and read calculator.py."`

## Architecture

* `main.py`: Initializes the OpenRouter client and manages the iterative tool-calling loop (capped at 20 iterations to prevent infinite loops).
* `prompts.py`: Contains the system instructions that define the agent's strict behavior and debugging workflow.
* `call_function.py`: Maps the LLM's requested JSON tool calls to executable Python functions and injects the secure working directory.
* `functions/`: Contains the standalone Python implementations and JSON schemas for each tool available to the model.