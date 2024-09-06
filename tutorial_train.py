from share import *

import pytorch_lightning as pl
from torch.utils.data import DataLoader
from tutorial_dataset import MyDataset
from cldm.logger import ImageLogger
from cldm.model import create_model, load_state_dict
from pytorch_lightning.callbacks import ModelCheckpoint

# Configs
resume_path = './models/control_sd15_ini.ckpt'
resume_checkpoint = 'resume_checkpoint/control_sd15_epoch=19-step=6279.ckpt'
batch_size = 4
logger_freq = 1000
learning_rate = 1e-5
sd_locked = True
only_mid_control = False


checkpoint_callback = ModelCheckpoint(
    dirpath = './resume_checkpoint', 
    filename = 'control_sd15_{epoch}-{step}', 
    save_top_k = -1, 
    every_n_epochs = 20
)


# First use cpu to load models. Pytorch Lightning will automatically move it to GPUs.
model = create_model('./models/cldm_v15.yaml').cpu()
model.load_state_dict(load_state_dict(resume_path, location='cpu'))
model.learning_rate = learning_rate
model.sd_locked = sd_locked
model.only_mid_control = only_mid_control

# Misc
dataset = MyDataset()
dataloader = DataLoader(dataset, num_workers=0, batch_size=batch_size, shuffle=True)
logger = ImageLogger(batch_frequency=logger_freq)
#resume_from_checkpoint=resume_checkpoint
trainer = pl.Trainer(gpus=[4], precision=32, callbacks=[logger, checkpoint_callback], resume_from_checkpoint = resume_checkpoint)

# Train!
trainer.fit(model, dataloader)
