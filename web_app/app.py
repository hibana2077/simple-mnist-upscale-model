'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-01-22 21:50:25
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-01-22 22:22:44
FilePath: /simple-mnist-upscale-model/web_app/app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import streamlit as st
import os
os.environ['KERAS_BACKEND'] = 'torch'
import keras

# load data
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# load model
from keras.models import load_model
model = load_model('../model/mnist_upscale_2.keras')

# noise rate input
noise_rate = st.sidebar.slider('Noise Rate', 0.0, 1.0, 0.5, 0.1)

# add noise
import numpy as np
x_test_noisy = x_test + noise_rate * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)

# predict
y_pred = model.predict(x_test_noisy)

# show result
import plotly.express as px

img_idx = st.sidebar.slider('Image Index', 0, len(y_pred)-1, 1, 1)

st.write('### Original Image')
fig = px.imshow(x_test[img_idx])
fig.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig)

st.write('### Noisy Image')
fig = px.imshow(x_test_noisy[img_idx])
fig.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig)

st.write('### Denoised Image')
fig = px.imshow(y_pred[img_idx])
fig.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig)

st.write('[![Github](https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hibana2077/simple-mnist-upscale-model)')