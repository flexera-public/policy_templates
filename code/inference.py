def model_fn(model_dir): return "dummy"
def input_fn(body, content_type): return body
def predict_fn(data, model): return "ok"
def output_fn(pred, accept): return str(pred)
