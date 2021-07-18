import json
import random
import pickle
import numpy as np
from tensorflow.keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()



intents = json.loads(open('intents.json').read())


try:
    model = load_model('pickle/chatbotmodel.h5')
except:
    print("Ok model not exist so we train LIKE ROCKY")
    import train
    model = load_model('pickle/chatbotmodel.h5')

with open('pickle/all_data.pkl', 'rb') as file:
    words, classes, training, labels = pickle.load(file)

def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lem.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    # print(res)
    error_thresh = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > error_thresh]
    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    # print(return_list)
    return return_list


def get_response(msg):
    intents_list = predict_class(msg)

    tag = intents_list[0]['intent']
    prob = float(intents_list[0]['probability'])
    list_of_intents = intents['intents']
    error_thresh = 0.60

    if prob > error_thresh:
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
    # if the error_thresh is not met respond IDK
    else:
        # the first item in intents should be responses to unknown inputs
        result = random.choice(intents['intents'][0]['responses'])
    return result
