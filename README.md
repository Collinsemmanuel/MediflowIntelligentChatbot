# MediFlowAI
A Medical Assistant Chat UI powered by MedLlama2 via Ollama, LangChain and Chainlit

### Open Source in Action 🚀
- [MedLlama2](https://ollama.com/library/medllama2) as Medical Language Model via [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/) as a Framework for LLM
- [Chainlit](https://docs.chainlit.io/langchain) for deploying

## System Requirements
Python 3.10 or later

## Steps to Run MediFlowAI
1. Create conda environment:
   ```
   conda create -n mediflowai python=3.10
   conda activate mediflowai
   ```

2. Install Ollama and pull the medllama2 model:
   ```
   # Install Ollama (Mac/Linux)
   curl -fsSL https://ollama.com/install.sh | sh

   # Pull medllama2 model
   ollama pull medllama2
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   chainlit run mediflow_ai.py
   ```

## Disclaimer
This is test project and is presented in my youtube video to learn new stuffs using the available open source projects and model. It is not meant to be used in production as it's not production ready. You can modify the code and use for your usecases ✌️
