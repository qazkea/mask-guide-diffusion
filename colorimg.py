import cv2
import os
import numpy as np
from tqdm import tqdm
#path = "/data1/Code/zhaoxiaowei/LVSCiTLos/results_all_and_pretrain_32topo/AttentUnet/attentunet0.3/ModelLabel2024_05_20_18_04"
#path0 = path + '/best'
#path1 = path + '/best'+"/pred_image"


#target1 = "/data1/Datasets/Seg/vxray/labels" + "/all1"
#target2 = "/data1/Datasets/Seg/vxray/labels" + "/all2"

target1 = './data'

if not os.path.exists(target1):
    os.makedirs(target1)
for imgname in tqdm(os.listdir('/20TB/data/yixue/mask30/0')):
    img = np.zeros([448,448,3],dtype = np.uint8)
    #color = [(255,0,255),(60,255,125),(0,0,255),(125,255,60),
    #         (255,60,125),(255,125,60),(60,125,0),(60,0,125),
    #         (0,60,125),(125,60,0),(125,0,60),(0,125,60),
    #        (30, 30, 255), (30, 255, 30), (255, 30, 30), (30, 255, 255),
    #(255, 30, 255), (255, 255, 30), (30, 30, 30), (255, 255, 255),
    #(0, 128, 128), (128, 0, 128), (128, 128, 0), (64, 64, 64),
#
#
    #         (60,255,0),(60,60,35),(128,60,255),(60,0,255),(0,60,255),(0,155,60),(60,0,125),
#
#
    #         (0,155,60),(255, 255, 255),
    #         (255, 204, 204),(153, 255, 255), (204, 255, 255),
    #         (153, 204, 255), (204, 229, 255),(128,0,128),(153, 204, 255)]
    # mask30
    color = [
        (255, 153, 255), (153, 255, 204), (153, 153, 255), (204, 255, 153),
        (255, 153, 204), (255, 204, 153), (153, 204, 153), (153, 153, 204),
        (153, 204, 255), (204, 153, 153), (204, 153, 204), (153, 255, 153),
        (102, 102, 255), (102, 255, 102), (255, 102, 102), (102, 255, 255),
        (255, 102, 255), (255, 255, 102), (102, 102, 102), (255, 255, 255),
        (102, 204, 204), (204, 102, 204), (204, 204, 102), (128, 128, 128),
        (153, 255, 102), (153, 102, 255), (102, 153, 255), (255, 153, 102),
        (204, 102, 153), (102, 204, 153)
    ]
    for i in range(29,-1,-1):
        #path3 = os.path.join("/data1/Datasets/Seg/Ribseg/labels",str(i),imgname)
        path3 = os.path.join("/20TB/data/yixue/mask30",str(i),imgname)
        #print(path3)
        img1 = cv2.imread(path3,0)
        img1 = cv2.resize(img1,(448,448))
        img1[img1<=125] = 0
        img1[img1>125] = 1
        img[:,:,0] = cv2.bitwise_or(img[:,:,0],color[i][0] * img1)
        img[:,:,1] = cv2.bitwise_or(img[:,:,1],color[i][1] * img1)
        img[:,:,2] = cv2.bitwise_or(img[:,:,2],color[i][2] * img1)
    cv2.imwrite(os.path.join(target1,imgname),img)
    #img1 = cv2.imread(os.path.join('/data1/Code/zhaoxiaowei/LVSCiTLos_ablation/data/zxwtesthard', imgname), 0)
    