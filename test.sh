python -W ignore test.py \
# --blur_prob=0 --jpg_prob=0 --val_batchsize=64 --patch_size=32 \
--load='/hexp/ly/PF_CAM/snapshot/sortnet/Net_epoch_best_pf_cam.pth' \
| tee "/hexp/ly/PF_CAM/log/print_out/test_pf_cam.txt"