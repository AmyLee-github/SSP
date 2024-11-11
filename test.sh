python -W ignore test.py \
--name='4pf_6_cam_h3_squeeze_test' \
--n_heads=3 \
--load='/hexp/ly/PF_CAM/snapshot/sortnet/Net_epoch_best_4pf_6_cam_h3_squeeze.pth' \
| tee "/hexp/ly/PF_CAM/log/print_out/test_4pf_6_cam_h3_squeeze.txt"