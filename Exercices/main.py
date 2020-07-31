import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def model_describe(function):
    def called_function():
        called_function = function()
        called_function.summary()
        return called_function
    return called_function

@model_describe
def train_sequential_model_chain_method():
    inputs = keras.Input(shape=(4,), dtype="float32")
    hidden = keras.layers.Dense(5, activation="relu")(inputs)
    hidden = keras.layers.Dense(10, activation="relu")(hidden)
    hidden = keras.layers.Dense(5, activation="relu")(hidden)
    hidden = keras.layers.Dense(6, activation="relu")(hidden)
    outputs = keras.layers.Dense(4)(hidden)
    return keras.Model(inputs=inputs, outputs=outputs, name="example_model")

@model_describe
def train_sequential_model_add_method():
    model = keras.Sequential(name="sequential_example_model")
    model.add(keras.layers.Input(shape=(4,), dtype="float32"))
    model.add(keras.layers.Dense(5, activation="relu"))
    model.add(keras.layers.Dense(4))
    return model

if __name__ == '__main__':
    print('Begin...')

ds_source = load_iris()

X_train, X_test, y_train, y_test = train_test_split(ds_source.data, ds_source.target, test_size=0.2, random_state=0)

models = [train_sequential_model_add_method(), train_sequential_model_chain_method()]

for model in models:

    model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        optimizer=keras.optimizers.SGD(),
        metrics=["accuracy"],
    )

    history = model.fit(X_train, y_train, batch_size=60, epochs=40, validation_split=0.2)
    test_scores = model.evaluate(X_test, y_test, verbose=2)

    print("Test loss:", test_scores[0])
    print("Test accuracy:", test_scores[1])

print('...End')
