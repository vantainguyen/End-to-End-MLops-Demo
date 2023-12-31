import numpy as np
import dill as pickle 
from sklearn.metrics import r2_score
from simple_linear_regr_utils import generate_data, evaluate



class SimpleLinearRegression:
    def __init__(self, iterations=15000, lr=0.1):
        self.iterations = iterations # number of iterations the fit method will be called
        self.lr = lr # The learning rate
        self.losses = [] # A list to hold the history of the calculated losses
        self.W, self.b = None, None # the slope and the intercept of the model

    def __loss(self, y, y_hat):
        """

        :param y: the actual output on the training set
        :param y_hat: the predicted output on the training set
        :return:
            loss: the sum of squared error

        """
        # Calculate the loss. use the sum of squared error formula for simplicity
         
        loss = np.square(y - y_hat)

        self.losses.append(loss)
        return loss

    def __init_weights(self, X):
        """

        :param X: The training set
        """
        weights = np.random.normal(size=X.shape[1] + 1)
        self.W = weights[:X.shape[1]].reshape(-1, X.shape[1])
        self.b = weights[-1]

    def __sgd(self, X, y, y_hat):
        """

        :param X: The training set
        :param y: The actual output on the training set
        :param y_hat: The predicted output on the training set
        :return:
            sets updated W and b to the instance Object (self)
        """
        # Calculate dW & db.
        
        dW = 0 
        db = 0
        dW -= 2/len(X) * np.dot(X.T, (y - y_hat))
        db -= 2/len(X) * np.sum(y - y_hat)
        
        #  Update the self.W and self.b using the learning rate and the values for dW and db
        self.W = self.W - self.lr*dW
        self.b = self.b - self.lr*db


    def fit(self, X, y):
        """

        :param X: The training set
        :param y: The true output of the training set
        :return:
        """
        self.__init_weights(X)
        y_hat = self.predict(X)
        loss = self.__loss(y, y_hat)
        print(f"Initial Loss: {loss}")
        for i in range(self.iterations + 1):
            self.__sgd(X, y, y_hat)
            y_hat = self.predict(X)
            loss = self.__loss(y, y_hat)
            if not i % 100:
                print(f"Iteration {i}, Loss: {loss}")

    def predict(self, X):
        """

        :param X: The training dataset
        :return:
            y_hat: the predicted output
        """
        # Calculate the predicted output y_hat. remember the function of a line is defined as y = WX + b
        y_hat = X*self.W + self.b
        return y_hat


if __name__ == "__main__":
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    model.fit(X_train,y_train)
    predicted = model.predict(X_test)
    r2_new = r2_score(y_test, predicted)
    with open('./artifacts/metrics.txt', 'r') as file:
        r2_best = float(file.readline())
    if r2_new > r2_best:
        # save model
        with open('model.pkl', 'wb') as file:
            pickle.dump(model, file)
        print('New model is better. It has been saved')
        with open('./artifacts/metrics.txt', 'w') as file:
            file.write(str(r2_new))
    else:
        print('New model is not better. It was not saved')

    evaluate(model, X_test, y_test, predicted)
