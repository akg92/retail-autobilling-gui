pip install -f requirements.txt --user
cd ../
#retinanet build
git clone https://github.com/akg92/retail-product-auto-billing
cd retail-product-auto-billing/retinanet
pip install . --user
python setup.py build_ext --inplace
## tensorcf install
cd ../tf-faster-rcnn
cd lib
make clean
make
cd ..
bash ./data/scripts/fetch_faster_rcnn_models.sh
##
cd ../../retail-autobilling-gui