# Litemono

## How to train
  * conda setting
    - conda create -n monovit python=3.7 anaconda
    - conda activate monovit
    - pip3 install torch==1.8.0 torchvision==0.9.0 torchaudio===0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
    - pip install dominate==2.4.0 Pillow==6.1.0 visdom==0.1.8
    - pip install tensorboardX==1.4 opencv-python  matplotlib scikit-image
    - pip3 install mmcv-full==1.3.0 mmsegmentation==0.11.0
    - pip install timm einops IPython

  * dependency installation
    - pip install git+https://github.com/saadnaeem-dev/pytorch-linear-warmup-cosine-annealing-warm-restarts-weight-decay
  * train
    - python train.py --model_name kaist_kitti_litemono --data_path=../data --dataset=infra --num_epochs 20 --batch_size 8
