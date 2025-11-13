import tensorflow as tf

model = tf.keras.models.load_model("emotion_model.h5", compile=False)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001))  # Use `learning_rate` instead of `lr`
model.save("fixed_emotion_model.h5")
