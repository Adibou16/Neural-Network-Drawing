import tensorflow as tf

# Loading mnist dataset
mnist = tf.keras.datasets.mnist
(img_train, lbl_train), (img_test, lbl_test) = mnist.load_data()

# Normalizing tensors
img_train = tf.keras.utils.normalize(img_train, axis=1)
img_test = tf.keras.utils.normalize(img_test, axis=1)

# Creating deep learning network
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training the network
model.fit(img_train, lbl_train, epochs=10)

# printing loss and acc
val_loss, val_acc = model.evaluate(img_test, lbl_test)
print(val_loss, val_acc)

# Saving the model
model.save('training_3.model')
