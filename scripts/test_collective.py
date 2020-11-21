import sys
sys.path.append(".")
from test_net import *

cfg=Config('collective')
cfg.test_seqs=[9, 64]

cfg.stage1_model_path='result/stage1_mn_epoch84_90.26%.pth'  #PATH OF THE BASE MODEL
cfg.stage2_model_path='result/stage2_mn_epoch16_84.47%.pth'   #PATH OF THE BASE MODEL
cfg.device_list="0,1"
cfg.training_stage=3

cfg.train_backbone=False
cfg.test_before_train=True
cfg.image_size=480, 720
cfg.out_size=57,87
cfg.num_boxes=13
cfg.num_actions=8
cfg.num_activities=7
cfg.num_frames=10
cfg.num_graph=4
cfg.tau_sqrt=True

cfg.batch_size=16
cfg.test_batch_size=1
cfg.train_learning_rate=1e-4
cfg.train_dropout_prob=0.2
cfg.weight_decay=1e-2
cfg.lr_plan={}
cfg.max_epoch=50

cfg.exp_note='Collective_test'
test_net(cfg)