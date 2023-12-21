# Litemono

## Setting
### 공통 설치 항목

```bash
$ conda create -n monodepth2 python=3.6.6 anaconda
$ pip3 install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
$ pip install tensorboardX==1.4
$ conda install opencv=3.3.1   # just needed for evaluation
```

- torchvision.ops 에러로 인해 0.9.x 이상이어야함 (0.2.1보다 높아야함…)

### Litemono 추가 설치 항목

```bash
$ pip install timm thop
$ pip install git+https://github.com/saadnaeem-dev/pytorch-linear-warmup-cosine-annealing-warm-restarts-weight-decay
```

## Dataset
- 데이터셋 구조
  - 폴더명과 파일 이름을 다음과 같이 수정해주었음
    ```bash
    |-data/
    |  |--infra/
    |  |  |--s_1/
    |  |  |  |--0000000000.jpg
    |  |  |--s_2/
    |  |  |  |--0000000000.jpg
    |  |  |...
    |  |  |--s_198/
    |  |  |  |--0000000000.jpg
    |  |--rgb/
    |  |  |--s_1/
    |  |  |  |--0000000000.jpg
    |  |  |--s_2/
    |  |  |  |--0000000000.jpg
    |  |  |...
    |  |  |--s_125/
    |  |  |  |--0000000000.jpg

## Training
```
$ CUDA_VISIBLE_DEVICES=0 python train.py --batch_size 14 --num_epochs 20 --model_name {train_model_name} --data_path=../data --dataset=infra
