# API as Tool - Routing with LLMs

This repository contains an implementation of routing with LLMs using tools and APIs. It demonstrates how to dynamically classify and handle user queries by invoking specific functions or APIs based on the context.

## Structure

- **chat_app.py**: Contains the implementation for a chat-based API.
- **chat_app.yaml**: OpenAPI specification for the chat-based API.
- **other_app.py**: Contains the implementation for another application with user and document management functionality.
- **other_app.yaml**: OpenAPI specification for the other application.
- **code.ipynb**: Notebook for handling dynamic classification and function/tool invocation.
- **routing.ipynb**: Notebook for managing the routing logic with LLMs.

## Environment Configuration

The `.env` file should contain the following:

```plaintext
OPENAI_API_KEY=<your_openai_api_key>
```
"# Routing-with-LLMs" 
