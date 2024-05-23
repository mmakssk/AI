import tensorflow as tf
from tensorflow.keras.datasets import cifar10
import numpy as np
import matplotlib.pyplot as plt

# Нормалізація набору даних
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

test_ac = []
train_ac = []

class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, hidden_size3, output_size):
        # Створення початкових ваг і зсувів
        self.W1 = np.random.randn(input_size, hidden_size1) / np.sqrt(input_size)
        self.b1 = np.zeros((1, hidden_size1))
        self.W2 = np.random.randn(hidden_size1, hidden_size2) / np.sqrt(hidden_size1)
        self.b2 = np.zeros((1, hidden_size2))
        self.W3 = np.random.randn(hidden_size2, hidden_size3) / np.sqrt(hidden_size2)
        self.b3 = np.zeros((1, hidden_size3))
        self.W4 = np.random.randn(hidden_size3, output_size) / np.sqrt(hidden_size3)
        self.b4 = np.zeros((1, output_size))

    # Пряме поширення
    def forward_propagation(self, X):
        X = X.reshape(X.shape[0], -1)
        # Розрахунок Прямого поширення
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = np.maximum(0, self.z1) # активація ReLU
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = np.maximum(0, self.z2)
        self.z3 = np.dot(self.a2, self.W3) + self.b3
        self.a3 = np.maximum(0, self.z3)
        self.z4 = np.dot(self.a3, self.W4) + self.b4
        self.z4 -= np.max(self.z4, axis=1, keepdims=True)
        self.a4 = np.exp(self.z4) / np.sum(np.exp(self.z4), axis=1, keepdims=True) # softmax
        return self.a4

    # Зворотнє поширення
    def backward_propagation(self, X, y):
        m = X.shape[0]
        # Розрахунок градієнтів
        delta4 = self.a4 - y
        self.dW4 = np.dot(self.a3.T, delta4) / m
        self.db4 = np.sum(delta4, axis=0, keepdims=True) / m
        delta3 = np.dot(delta4, self.W4.T) * np.where(self.a3 > 0, 1, 0)
        self.dW3 = np.dot(self.a2.T, delta3) / m
        self.db3 = np.sum(delta3, axis=0, keepdims=True) / m
        delta2 = np.dot(delta3, self.W3.T) * np.where(self.a2 > 0, 1, 0)
        self.dW2 = np.dot(self.a1.T, delta2) / m
        self.db2 = np.sum(delta2, axis=0, keepdims=True) / m
        delta1 = np.dot(delta2, self.W2.T) * np.where(self.a1 > 0, 1, 0)
        self.dW1 = np.dot(X.reshape(X.shape[0], -1).T, delta1) / m
        self.db1 = np.sum(delta1, axis=0, keepdims=True) / m

    # Оновлення параметрів
    def update_param(self, learning_rate):
        self.W1 -= learning_rate * self.dW1
        self.b1 -= learning_rate * self.db1
        self.W2 -= learning_rate * self.dW2
        self.b2 -= learning_rate * self.db2
        self.W3 -= learning_rate * self.dW3
        self.b3 -= learning_rate * self.db3
        self.W4 -= learning_rate * self.dW4
        self.b4 -= learning_rate * self.db4

    # Розрахунок втрат і точності
    def evaluate(self, X, y):
        predictions = self.forward_propagation(X)
        loss = -np.sum(y * np.log(predictions)) / len(y)
        accuracy = np.mean(np.argmax(predictions, axis=1) == np.argmax(y, axis=1))
        return loss, accuracy

    # Тренування
    def train(self, X, y, epochs, learning_rate, batch_size=64):
        for epoch in range(epochs):
            loss = 0
            accuracy = 0
            for i in range(0, X.shape[0], batch_size):
                batch_X = X[i:i + batch_size]
                batch_y = y[i:i + batch_size]
                self.forward_propagation(batch_X)
                self.backward_propagation(batch_X, batch_y)
                self.update_param(learning_rate)
            loss, accuracy = self.evaluate(X, y)
            _, test_accuracy = self.evaluate(x_test, y_test)
            train_ac.append(accuracy)
            test_ac.append(test_accuracy)
            if (epoch + 1) % 5 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.3f}, Accuracy: {accuracy:.3f}")

epochs = 10

model = NeuralNetwork(3072, 1024,  256, 64, 10)
model.train(x_train, y_train, epochs=epochs, learning_rate=0.01)

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy*100)

"""
fig, plot_one = plt.subplots()
plot_one.plot(range(epochs), train_ac, color="green")
plot_one.plot(range(epochs), test_ac, color="red")
plt.show()

"""
predictions = model.forward_propagation(x_test)

y_pred = np.argmax(predictions, axis=1)
y_true = np.argmax(y_test, axis=1)

confusion = np.zeros((10,10))

for i in range(len(y_pred)):
    confusion[y_true[i], y_pred[i]] += 1

confusion = confusion.astype('float32') / np.sum(confusion, axis=1, keepdims=True)

plt.figure(figsize=(6,6))
plt.imshow(confusion, cmap='Blues')

plt.xticks(range(10,10))
plt.yticks(range(10,10))
plt.xlabel('Predict')
plt.ylabel('True')
plt.title("Confusion Matrix")
plt.show()

