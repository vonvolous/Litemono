from __future__ import absolute_import, division, print_function

from options import LiteMonoOptions
from trainer import Trainer

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

options = LiteMonoOptions()
opts = options.parse()


if __name__ == "__main__":
    trainer = Trainer(opts)
    trainer.train()
