# Hướng dẫn cài đặt CenterNet

## Cài đặt môi trường
0. Môi trường thử nghiệm
CUDA >= 9.0
GPU: NVIDIA-Tesla K80

1. Cài đặt COCOAPI
```
COCOAPI = 'cocoapi'
!git clone https://github.com/cocodataset/cocoapi.git 'cocoapi'
cd $COCOAPI/PythonAPI
make
python setup.py install --user
```

2. Cài đặt CenterNet
```
CenterNet_ROOT = 'CenterNet'
git clone https://github.com/xuan-vy-nguyen/CenterNet.git 'CenterNet'
cd $CenterNet_ROOT
pip install -r requirements.txt
cd $CenterNet_ROOT/src/lib/external
python setup.py build_ext --inplace
```

3. Cài đặt DCN2
```
cd $CenterNet_ROOT/src/lib/models/networks
rm -rf DCNv2
git clone https://github.com/CharlesShang/DCNv2
cd DCNv2
python setup.py build develop
```

##Dataset
1. Download dữ liệu
