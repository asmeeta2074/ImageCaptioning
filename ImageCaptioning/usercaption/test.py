import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.inception_v3 import InceptionV3
from keras.models import Model
from keras.applications.inception_v3 import preprocess_input
import numpy as np
wordtoix = np.load('wordtoix.npy',allow_pickle=True).item()
ixtoword = np.load('ixtoword.npy',allow_pickle=True).item()
max_length=74
def caption(photo):
    model = load_model('batch_changed_model_19.h5')
    in_text = 'startseq'
    for i in range(max_length):
        sequence = [wordtoix[w] for w in in_text.split() if w in wordtoix]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo,sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = ixtoword[yhat]
        in_text += ' ' + word
        if word == 'endseq':
            break
    final = in_text.split()
    final = final[1:-1]
    final = ' '.join(final)
    return final
# extract features from each photo in the directory
def extract_features(filename):
    model = InceptionV3(weights='imagenet')
    model = Model(model.input, model.layers[-2].output)
    image = load_img(filename, target_size=(299, 299))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
	# reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	# prepare the image for the Inception model
    image = preprocess_input(image)
	# get features
    feature = model.predict(image, verbose=0)
    return feature
pic = ('IMG_1186.jpg')
x=plt.imread(pic)
plt.imshow(x)
plt.show()
encoded = extract_features(pic)
print(caption(encoded))