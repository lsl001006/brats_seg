import os
from tqdm import tqdm
from PIL import Image

path_gt = "/home/lsl/Research/brats_seg/UNet2D_BraTs/output/test/GT"
path_pred = "/home/lsl/Research/brats_seg/UNet2D_BraTs/output/test/Pred"
dst = "/home/lsl/Research/brats_seg/UNet2D_BraTs/output/test/Combined"

if not os.path_pred.exists(dst):
    os.mkdir(dst)
gts = sorted(os.listdir(path_gt))
preds = sorted(os.listdir(path_pred))
for gt, pred in tqdm(zip(gts, preds)):
    imgs = [Image.open(os.path_pred.join(path_gt, gt)), Image.open(os.path_pred.join(path_pred, pred))]
    result = Image.new(imgs[0].mode, (320,160))
    for i, im in enumerate(imgs):
        result.paste(im, (i*160, 0))
    result.save(os.path_pred.join(dst, gt))
