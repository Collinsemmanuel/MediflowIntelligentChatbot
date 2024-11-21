from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    # Sending an image with the local file path
    elements = [
        cl.Image(name="logo", display="inline", path="mediflow_logo.jpeg")
    ]
    await cl.Message(
        content="👋 Hello! I'm MediFlowAI, your medical assistant. I can help you with medical information and general health queries. Remember, while I can provide information, always consult healthcare professionals for specific medical advice. How can I assist you today?", 
        elements=elements
    ).send()
    
    model = Ollama(model="medllama2")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are MediFlowAI, a medical AI assistant powered by MedLlama2. Follow these guidelines:
                - Provide accurate, evidence-based medical information
                - Use clear, professional, and easy-to-understand language
                - Include relevant medical terminology with explanations
                - Always emphasize the importance of consulting healthcare professionals
                - Do not make definitive diagnoses
                - Be empathetic and professional in responses
                - If unsure, acknowledge limitations and suggest professional consultation
                - Focus on general medical knowledge and health education
                
                Important: Remind users that this is for informational purposes only and not a substitute for professional medical advice."""
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send() 