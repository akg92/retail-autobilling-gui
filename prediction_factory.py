
import sys
sys.path.append('../retail-product-auto-billing/retinanet')
sys.path.append('../retail-product-auto-billing/retinanet/keras_retinanet')

sys.path.append('../retail-product-auto-billing/retinanet/keras_retinanet')
sys.path.append('../retail-product-auto-billing/tf-faster-rcnn/tools')
sys.path.append('../retail-product-auto-billing/tf-faster-rcnn/lib')
sys.path.append('../retail-product-auto-billing/tf-faster-rcnn')

# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
import numpy as np
import os
import json

from test_net import test_single,test_single2,clear

def get_model_dir():
    return os.path.abspath(os.path.dirname(__file__))

class BasePrediction():


    def __init__(self):
        with open('annotation.json') as f:
            json_obj = json.load(f)
            self.categories = json_obj['categories']

    def process_prediction(self,labels):
        result = []
        label_set = set(labels)
        for label in label_set:
            name = self.categories[label]['name']
            count = labels.count(label)
            price = int(label / 10)+1
            result.append([name, count, price, price * count])
        return result

    def reset(self):
        clear()




class Multi(BasePrediction):

    FILE_LOCATION ='model/multi.h5'
    PREDICTION_CONFIDENCE = 0.5
    model = None
    def __init__(self):
        BasePrediction.__init__(self)
        if not self.model:
            self.model = models.load_model(self.FILE_LOCATION, backbone_name='resnet50')

    def predict(self,img_path):
        image = read_image_bgr(img_path)
        image = preprocess_image(image)
        image, scale = resize_image(image)
        print(scale)
        boxes, scores, labels = self.model.predict_on_batch(np.expand_dims(image, axis=0))
        result = []
        result_score = []
        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            if score < self.PREDICTION_CONFIDENCE:
                break
            else:
                result.append(label)
                result_score.append(score)
        return self.process_prediction(result)



class Single(BasePrediction):

    FILE_LOCATION ='res101_faster_rcnn_iter_480000.ckpt'
    PREDICTION_CONFIDENCE = 0.65
    model = False
    model_path = None
    def __init__(self):
        BasePrediction.__init__(self)
        if not self.model:
            self.model_dir = get_model_dir()
            self.model_path = os.path.join(self.model_dir,'model',self.FILE_LOCATION)
            print(self.model_path)
    def compute_class(self,scores):
        print(np.max(scores,axis=1))
        result = []
        for i in range(scores.shape[0]):
            for j in range(scores.shape[1]):
                if scores[i][j]>=0.5:
                    print(scores[i][j])
                    result.append(j)
        return result

    def predict(self,img_path):
        img_path = os.path.abspath(img_path)
        #scores,result = test_single(img_path,self.model_path)
        #classes = self.compute_class(scores)
        #test_1 = test_single2(img_path,self.model_path)
        result = test_single(img_path,self.model_path)
        ## normalize the result
        result = [x-1 for x in result]
        print(result)
        return self.process_prediction(result)
        #print(result)
        # for box, score, label in zip(boxes[0], scores[0], labels[0]):
        #     if score < self.PREDICTION_CONFIDENCE:
        #         break
        #     else:
        #         result.append(label)
        #         result_score.append(score)
        # return self.process_prediction(result)


if __name__ == '__main__':
    obj = Single()
    s_result = obj.predict('test3.jpg')
    obj.reset()
    obj2 = Multi()
    m_result = obj2.predict('test3.jpg')
    print(s_result)
    print(m_result)