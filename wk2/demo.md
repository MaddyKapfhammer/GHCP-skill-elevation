# GitHub Copilot Demo: Log File Analyzer (Advanced Python)

Welcome to the live demo for Session 2 of **Elevating Your Skills with GitHub Copilot**. This walkthrough showcases how Copilot can be used at multiple stages of a complex, non-web-based project: a Log File Analyzer written in Python.

## Overview: What Are We Building?

We are working on a **Log File Analyzer** — a tool that parses large system log files, identifies patterns or anomalies (e.g., frequent errors, slow responses), and generates human-readable reports.

This tool might be used by SREs or developers for automated health analysis of logs.

## Requirements

- Python 3.9+
- GitHub Copilot enabled in VS Code
- A large sample log file (`sample.log`) placed in the same folder (can be dummy or generated)
- Use Copilot Chat and inline suggestions

## Step-by-Step Instructions

### 1. Understand the Codebase
Open `log_analyzer.py` and skim the code. Briefly walk through the class structure:
- `LogEntry`: A dataclass to represent each log line
- `LogParser`: Handles parsing of log files
- `LogAnalyzer`: Computes metrics like most common errors or slowest endpoints
- `ReportGenerator`: Formats the results into readable summaries

Ask Copilot to explain a function like `parse_line()` or `compute_error_stats()`  
Prompt:  
```
// Ask GitHub Copilot in chat:
"What does the function `parse_line` do? Summarize in plain English."
````

### 2. Add New Feature: "Top 5 Slowest Requests"

We'll ask Copilot to generate a method in `LogAnalyzer` that returns the top 5 slowest requests in the logs.
Prompt:
```
"Write a method to return the 5 slowest response times from the logs"
````

Discussion: Did GitHub Copilot infer the correct sorting logic? Is it reading from `LogEntry.response_time`?

### 3. Improve Code: Add Type Annotations

Many of the methods lack full typing. We’ll use Copilot to add these.

Prompt:

```
// Ask Copilot Chat:  
"Add type hints to all public methods in LogAnalyzer"
```

Review: How accurate were the suggestions? Did any types seem incorrect or too generic?

### 4. Write Tests with Copilot

Use GitHub Copilot to create a new file: `test_log_analyzer.py`. We’ll prompt GitHub Copilot to write unit tests.
Prompt:

```python
# Write tests for LogAnalyzer's compute_error_stats and get_slowest_requests methods
```

Tip: Check if GitHub Copilot assumes realistic input/output or if you need to refine prompts.

### 5. Refactor: Simplify Redundant Logic

Pick a function with nested loops or repeated logic. Use Copilot to refactor it into smaller, testable units.
Prompt:

```
// Ask Copilot Chat:  
"Refactor `compute_response_stats` to make the logic clearer and extract reusable parts"
```

## Wrap-Up Discussion

* Where did Copilot succeed?
* Where did it struggle or misinterpret the context?
* What strategies improved the quality of completions?

## Optional Extension

Add support for JSON log formats by prompting Copilot:
Prompt:

```python
Extend the LogParser class to support parsing logs in JSON format
```

## Key Takeaways

* Copilot is not just for writing new code—it enhances **reading**, **refactoring**, and **testing**.
* The **quality of prompts** and your **contextual setup** matter more as code complexity increases.
* Use it to speed up **feature iteration**, **error analysis**, and **code cleanup**.
