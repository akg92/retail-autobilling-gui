pip install -r requirements.txt --user
cd ../
#retinanet build
git clone https://github.com/akg92/retail-product-auto-billing
cd retail-product-auto-billing/retinanet
pip install . --user
python setup.py build_ext --inplace
#pwd
## tensorcf install
cd ../tf-faster-rcnn
cd lib
pwd
make clean
make
cd ..

mkdir -p data/imagenet_weights
cd data/imagenet_weights
wget -v http://download.tensorflow.org/models/resnet_v1_101_2016_08_28.tar.gz
tar -xzvf resnet_v1_101_2016_08_28.tar.gz
mv resnet_v1_101.ckpt res101.ckpt
cd ../..

##
cd ../../retail-autobilling-gui
