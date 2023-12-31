from potassium import Potassium, Request, Response
from llama_cpp import Llama
import multiprocessing


app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    # device = 0 if torch.cuda.is_available() else -1
    # model = pipeline('fill-mask', model='bert-base-uncased', device=device)

    cpu_count = multiprocessing.cpu_count()
    # cpu_selected = int(cpu_count*0.5)
    cpu_selected = 16
    print(f"Total CPU: {cpu_count}, running with {cpu_selected} CPUs")
    llm = Llama(model_path="./koala-7B.ggmlv3.q5_1.bin", n_gpu_layers=20000, n_threads=cpu_selected, verbose=False, n_ctx=4096)

    context = {
        "llm": llm
    }

    return context

# @app.handler runs for every call
@app.handler()
def handler(context: dict, request: Request) -> Response:
    prompt = request.json.get("prompt")
    stop = request.json.get("stop")
    till_end = request.json.get("till_end")
    max_tokens = int(request.json.get("max_tokens"))
    echo = int(request.json.get("echo"))
    
    llm = context.get("llm")

    if(till_end):

        finish_reason = 'length'
        output = ""
        _prompt = prompt

        while finish_reason != 'stop':
            _output = llm( _prompt , max_tokens=max_tokens, stop=stop, echo=echo)
            _prompt += _output['choices'][0]['text']
            finish_reason = _output['choices'][0]['finish_reason']
            print(_output['choices'][0]['finish_reason'])
        
        output = _output

    else:
        output = llm( prompt, max_tokens=max_tokens, stop=stop, echo=True)
        output = output['choices'][0]['text']
    
    return Response(
        json = {"output": output}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()