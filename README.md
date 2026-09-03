# Prompt Engineering Learning Project

A comprehensive collection of **22 prompt engineering techniques** for learning and experimentation with large language models.

## 📚 Overview

This repository is a personal learning project exploring prompt engineering techniques, from foundational concepts to advanced strategies. Each technique is implemented as a Jupyter notebook with practical examples using OpenAI's API and LangChain.

## 🎯 Prompt Engineering Techniques

| # | Category | Technique |
|---|----------|-----------|
| 1 | 🎓 **Fundamental Concepts** | [Introduction to Prompt Engineering](all_prompt_engineering_techniques/intro-prompt-engineering-lesson.ipynb) |
| 2 | 🎓 **Fundamental Concepts** | [Basic Prompt Structures](all_prompt_engineering_techniques/basic-prompt-structures.ipynb) |
| 3 | 🎓 **Fundamental Concepts** | [Prompt Templates and Variables](all_prompt_engineering_techniques/prompt-templates-variables-jinja2.ipynb) |
| 4 | 🔧 **Core Techniques** | [Zero-Shot Prompting](all_prompt_engineering_techniques/zero-shot-prompting.ipynb) |
| 5 | 🔧 **Core Techniques** | [Few-Shot Learning](all_prompt_engineering_techniques/few-shot-learning.ipynb) |
| 6 | 🔧 **Core Techniques** | [Chain of Thought (CoT)](all_prompt_engineering_techniques/cot-prompting.ipynb) |
| 7 | 🎯 **Advanced Strategies** | [Self-Consistency](all_prompt_engineering_techniques/self-consistency.ipynb) |
| 8 | 🎯 **Advanced Strategies** | [Constrained Generation](all_prompt_engineering_techniques/constrained-guided-generation.ipynb) |
| 9 | 🎯 **Advanced Strategies** | [Role Prompting](all_prompt_engineering_techniques/role-prompting.ipynb) |
| 10 | 🚀 **Advanced Implementations** | [Task Decomposition](all_prompt_engineering_techniques/task-decomposition-prompts.ipynb) |
| 11 | 🚀 **Advanced Implementations** | [Prompt Chaining](all_prompt_engineering_techniques/prompt-chaining-sequencing.ipynb) |
| 12 | 🚀 **Advanced Implementations** | [Instruction Engineering](all_prompt_engineering_techniques/instruction-engineering-notebook.ipynb) |
| 13 | ⚡ **Optimization** | [Prompt Optimization](all_prompt_engineering_techniques/prompt-optimization-techniques.ipynb) |
| 14 | ⚡ **Optimization** | [Handling Ambiguity](all_prompt_engineering_techniques/ambiguity-clarity.ipynb) |
| 15 | ⚡ **Optimization** | [Length Management](all_prompt_engineering_techniques/prompt-length-complexity-management.ipynb) |
| 16 | 🛠️ **Specialized Applications** | [Negative Prompting](all_prompt_engineering_techniques/negative-prompting.ipynb) |
| 17 | 🛠️ **Specialized Applications** | [Prompt Formatting](all_prompt_engineering_techniques/prompt-formatting-structure.ipynb) |
| 18 | 🛠️ **Specialized Applications** | [Task-Specific Prompts](all_prompt_engineering_techniques/specific-task-prompts.ipynb) |
| 19 | 🌍 **Advanced Applications** | [Multilingual Prompting](all_prompt_engineering_techniques/multilingual-prompting.ipynb) |
| 20 | 🌍 **Advanced Applications** | [Ethical Considerations](all_prompt_engineering_techniques/ethical-prompt-engineering.ipynb) |
| 21 | 🌍 **Advanced Applications** | [Prompt Security](all_prompt_engineering_techniques/prompt-security-and-safety.ipynb) |
| 22 | 🌍 **Advanced Applications** | [Effectiveness Evaluation](all_prompt_engineering_techniques/evaluating-prompt-effectiveness.ipynb) |

## Getting Started

### Prerequisites
- Python 3.10+ (or use the provided venv setup)
- OpenAI API key

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/cibiyannatw/prompt-engineering.git
   cd prompt-engineering
   ```

2. Create a virtual environment:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

5. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

6. Open any notebook from `all_prompt_engineering_techniques/` and start learning!

## 📖 Key Features

- 🎓 22 hands-on tutorial notebooks
- 🧠 Techniques from beginner to advanced levels
- 💻 Practical implementations with OpenAI and LangChain
- 🔄 Interactive learning with reproducible examples
- 📝 Well-documented code with explanations

## 🛠️ Technologies Used

- **LLM Framework**: OpenAI GPT models
- **Libraries**: LangChain, Python
- **Notebooks**: Jupyter
- **Templating**: Jinja2

## Project Structure

```
.
├── all_prompt_engineering_techniques/  # 22 technique notebooks
├── requirements.txt                    # Python dependencies
├── README.md                          # This file
└── .env                               # API keys (add this file)
```

## Notes for Learning

- Each notebook is self-contained and can be explored independently
- Experiments with different prompts and parameters to understand how they affect model behavior
- Keep track of what works and what doesn't in your learning journey
- Consider running notebooks multiple times as LLM outputs can vary

## License

This project is for personal learning purposes.

---

**Happy learning!** 🚀
