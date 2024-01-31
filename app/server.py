from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langserve import add_routes
from langchain_community.llms import CTransformers

app = FastAPI(
    title="Xana Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces with Mistral-7B-Instruct-v0.2",
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
model = CTransformers(model=r'models\mistralai\Mistral-7B-Instruct-v0.2-GGUF\mistral-7b-instruct-v0.2.Q5_K_M.gguf', callbacks=[StreamingStdOutCallbackHandler()])
prompt = ChatPromptTemplate.from_template("{prompt}")
add_routes(app, prompt | model, path="/xana")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
