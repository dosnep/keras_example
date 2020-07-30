import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

if __name__ == '__main__':
    print('Begin...')

dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=0)

inputs = keras.Input(shape=(4,), dtype="float32")
hidden = keras.layers.Dense(5, activation="relu")(inputs)
outputs = keras.layers.Dense(4)(hidden)
model = keras.Model(inputs=inputs, outputs=outputs, name="example_model")
model.summary()

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=["accuracy"],
)

history = model.fit(X_train, y_train, batch_size=60, epochs=40, validation_split=0.2)

test_scores = model.evaluate(X_test, y_test, verbose=2)

print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])
