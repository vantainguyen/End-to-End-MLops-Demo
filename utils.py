import dill as pickle 


def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
        return model
    

def save_model(model_path, model):
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)


def read_metrics(metrics_path):
    with open(metrics_path, 'r') as file:
        r2_best = float(file.readline())
        return r2_best
    

def write_metrics(metrics_path, r2_new):
    with open(metrics_path, 'w') as file:
        file.write(str(r2_new))