import os
import logging
from sklearn.metrics import r2_score
from simple_linear_regr_utils import generate_data
from utils import load_model, save_model, read_metrics, write_metrics
from simple_linear_regr import SimpleLinearRegression

# Configure logging to save messages to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # Optional: Also print log messages to console
    ]
)

model_path = os.path.join('artifacts', 'model.pkl')
metrics_path = os.path.join('artifacts', 'metrics.txt')

if __name__ == "__main__":
    try:
        X_train, y_train, X_test, y_test = generate_data()
        model = SimpleLinearRegression()
        try:
            logging.info('loading existing model successfully')
            model = load_model(model_path)
        except Exception as e:
            logging.info('loading existing model unsuccessfully')
            pass
        logging.info('Training ....')
        model.fit(X_train,y_train)
        logging.info('Training completed')
        predicted = model.predict(X_test)
        r2_new = r2_score(y_test, predicted)
        r2_best = read_metrics(metrics_path)
        if r2_new > r2_best:
            # save model
            save_model(model_path, model)
            logging.info(f'New model was better. It was saved. Old r2: {r2_best:.4f}; new r2: {r2_new:.4f}')
            write_metrics(metrics_path, r2_new)
        else:
            logging.info(f'New model was not better. It was not saved. Old r2: {r2_best:.4f}; new r2: {r2_new:.4f}')
    except Exception as e:
        logging.error(f'Training process failed: {e}')


        
