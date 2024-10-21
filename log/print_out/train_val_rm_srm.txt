# Options
----------------- Options ---------------
                 CropSize: 224                           
                      aug: True                          
                batchsize: 64                            
                blur_prob: 0.0                           
                 blur_sig: [0, 1]                        
                  choices: [0, 0, 0, 0, 1, 0, 0, 0]      
                    epoch: 30                            
                   gpu_id: 0                             
               image_root: /hxp/dataset/genImage         
                  isPatch: True                          
                  isTrain: True                          	[default: None]
                    isVal: False                         	[default: None]
               jpg_method: ['pil', 'cv2']                
                 jpg_prob: 0.0                           
                 jpg_qual: [90, 100]                     
                     load: None                          
                 log_name: log3.log                      
                       lr: 1e-4                          	[default: 0.0001]
                     name: experiment_name               
               patch_size: 32                            	[default: 32]
                rz_interp: bilinear                      
                save_path: ./snapshot/sortnet/           
                trainsize: 256                           
            val_batchsize: 64                            
             val_interval: 1                             
----------------- End -------------------
load data...
train on: imagenet_ai_0419_sdv4
val on: imagenet_ai_0508_adm
val on: imagenet_ai_0419_biggan
val on: imagenet_glide
val on: imagenet_midjourney
val on: imagenet_ai_0419_sdv4
val on: imagenet_ai_0424_sdv5
val on: imagenet_ai_0419_vqdm
val on: imagenet_ai_0424_wukong
USE GPU 0
Start train
2024-09-02 03:12:18.639032 Epoch [001/030], Step [0001/2668], Total_loss: 0.6162
2024-09-02 03:15:13.989041 Epoch [001/030], Step [0200/2668], Total_loss: 0.1669
2024-09-02 03:18:13.800292 Epoch [001/030], Step [0400/2668], Total_loss: 0.0309
2024-09-02 03:21:03.158114 Epoch [001/030], Step [0600/2668], Total_loss: 0.0316
2024-09-02 03:23:52.613442 Epoch [001/030], Step [0800/2668], Total_loss: 0.0322
2024-09-02 03:26:44.877384 Epoch [001/030], Step [1000/2668], Total_loss: 0.0686
2024-09-02 03:29:45.374175 Epoch [001/030], Step [1200/2668], Total_loss: 0.0098
2024-09-02 03:32:40.196537 Epoch [001/030], Step [1400/2668], Total_loss: 0.0066
2024-09-02 03:35:32.146019 Epoch [001/030], Step [1600/2668], Total_loss: 0.0057
2024-09-02 03:38:26.534862 Epoch [001/030], Step [1800/2668], Total_loss: 0.0033
2024-09-02 03:41:10.126611 Epoch [001/030], Step [2000/2668], Total_loss: 0.0065
2024-09-02 03:43:21.554996 Epoch [001/030], Step [2200/2668], Total_loss: 0.0147
2024-09-02 03:45:23.980946 Epoch [001/030], Step [2400/2668], Total_loss: 0.0059
2024-09-02 03:47:20.454933 Epoch [001/030], Step [2600/2668], Total_loss: 0.0128
2024-09-02 03:48:01.010386 Epoch [001/030], Step [2668/2668], Total_loss: 0.0078
val on: imagenet_ai_0508_adm
ai accu: 0.6639999747276306
nature accu:0.9988332986831665
val on:imagenet_ai_0508_adm, Epoch:1, Accuracy:0.831416666507721
val on: imagenet_ai_0419_biggan
ai accu: 0.4659999907016754
nature accu:0.9990000128746033
val on:imagenet_ai_0419_biggan, Epoch:1, Accuracy:0.7325000166893005
val on: imagenet_glide
ai accu: 0.8865000009536743
nature accu:0.9993333220481873
val on:imagenet_glide, Epoch:1, Accuracy:0.9429166316986084
val on: imagenet_midjourney
ai accu: 0.41366666555404663
nature accu:0.9990000128746033
val on:imagenet_midjourney, Epoch:1, Accuracy:0.706333339214325
val on: imagenet_ai_0419_sdv4
ai accu: 0.9438333511352539
nature accu:0.9986666440963745
val on:imagenet_ai_0419_sdv4, Epoch:1, Accuracy:0.9712499976158142
val on: imagenet_ai_0424_sdv5
ai accu: 0.9415000677108765
nature accu:0.9987500309944153
val on:imagenet_ai_0424_sdv5, Epoch:1, Accuracy:0.9701250195503235
val on: imagenet_ai_0419_vqdm
ai accu: 0.6673333048820496
nature accu:0.9990000128746033
val on:imagenet_ai_0419_vqdm, Epoch:1, Accuracy:0.8331666588783264
val on: imagenet_ai_0424_wukong
ai accu: 0.906000018119812
nature accu:0.9984999895095825
val on:imagenet_ai_0424_wukong, Epoch:1, Accuracy:0.9522500038146973
Save state_dict successfully! Best epoch:1.
Epoch:1,Accuracy:0.8715999722480774, bestEpoch:1, bestAccu:0.8715999722480774
2024-09-02 04:02:15.532555 Epoch [002/030], Step [0001/2668], Total_loss: 0.0018
2024-09-02 04:03:25.832017 Epoch [002/030], Step [0200/2668], Total_loss: 0.0013
2024-09-02 04:04:37.444299 Epoch [002/030], Step [0400/2668], Total_loss: 0.0199
2024-09-02 04:05:49.186013 Epoch [002/030], Step [0600/2668], Total_loss: 0.0018
2024-09-02 04:07:00.680278 Epoch [002/030], Step [0800/2668], Total_loss: 0.0295
2024-09-02 04:08:12.786045 Epoch [002/030], Step [1000/2668], Total_loss: 0.0202
2024-09-02 04:09:23.332381 Epoch [002/030], Step [1200/2668], Total_loss: 0.0064
2024-09-02 04:10:33.434542 Epoch [002/030], Step [1400/2668], Total_loss: 0.0012
2024-09-02 04:11:45.286376 Epoch [002/030], Step [1600/2668], Total_loss: 0.0047
2024-09-02 04:12:55.833789 Epoch [002/030], Step [1800/2668], Total_loss: 0.0004
2024-09-02 04:14:05.886483 Epoch [002/030], Step [2000/2668], Total_loss: 0.0004
2024-09-02 04:15:20.932485 Epoch [002/030], Step [2200/2668], Total_loss: 0.0129
2024-09-02 04:16:32.546587 Epoch [002/030], Step [2400/2668], Total_loss: 0.0014
2024-09-02 04:17:40.785952 Epoch [002/030], Step [2600/2668], Total_loss: 0.0016
2024-09-02 04:18:04.212228 Epoch [002/030], Step [2668/2668], Total_loss: 0.0005
val on: imagenet_ai_0508_adm
ai accu: 0.6504999995231628
nature accu:0.996666669845581
val on:imagenet_ai_0508_adm, Epoch:2, Accuracy:0.8235833048820496
val on: imagenet_ai_0419_biggan
ai accu: 0.4713333249092102
nature accu:0.9976666569709778
val on:imagenet_ai_0419_biggan, Epoch:2, Accuracy:0.734499990940094
val on: imagenet_glide
ai accu: 0.9441666603088379
nature accu:0.9975000023841858
val on:imagenet_glide, Epoch:2, Accuracy:0.9708333015441895
val on: imagenet_midjourney
ai accu: 0.5588333010673523
nature accu:0.996666669845581
val on:imagenet_midjourney, Epoch:2, Accuracy:0.7777500152587891
val on: imagenet_ai_0419_sdv4
ai accu: 0.9666666388511658
nature accu:0.996999979019165
val on:imagenet_ai_0419_sdv4, Epoch:2, Accuracy:0.9818333387374878
val on: imagenet_ai_0424_sdv5
ai accu: 0.9673750400543213
nature accu:0.9970000386238098
val on:imagenet_ai_0424_sdv5, Epoch:2, Accuracy:0.9821875691413879
val on: imagenet_ai_0419_vqdm
ai accu: 0.593500018119812
nature accu:0.997166633605957
val on:imagenet_ai_0419_vqdm, Epoch:2, Accuracy:0.7953333258628845
val on: imagenet_ai_0424_wukong
ai accu: 0.9131666421890259
nature accu:0.996666669845581
val on:imagenet_ai_0424_wukong, Epoch:2, Accuracy:0.9549166560173035
Save state_dict successfully! Best epoch:2.
Epoch:2,Accuracy:0.8817999958992004, bestEpoch:2, bestAccu:0.8817999958992004
2024-09-02 04:28:56.633326 Epoch [003/030], Step [0001/2668], Total_loss: 0.0184
2024-09-02 04:30:06.936751 Epoch [003/030], Step [0200/2668], Total_loss: 0.0022
2024-09-02 04:31:20.985741 Epoch [003/030], Step [0400/2668], Total_loss: 0.0005
2024-09-02 04:32:33.093164 Epoch [003/030], Step [0600/2668], Total_loss: 0.0001
2024-09-02 04:33:43.500684 Epoch [003/030], Step [0800/2668], Total_loss: 0.0693
2024-09-02 04:34:54.646423 Epoch [003/030], Step [1000/2668], Total_loss: 0.0018
2024-09-02 04:36:08.239284 Epoch [003/030], Step [1200/2668], Total_loss: 0.0008
2024-09-02 04:37:19.485977 Epoch [003/030], Step [1400/2668], Total_loss: 0.0031
2024-09-02 04:38:29.785971 Epoch [003/030], Step [1600/2668], Total_loss: 0.0002
2024-09-02 04:39:40.833176 Epoch [003/030], Step [1800/2668], Total_loss: 0.0008
2024-09-02 04:40:52.033917 Epoch [003/030], Step [2000/2668], Total_loss: 0.0008
2024-09-02 04:42:02.365677 Epoch [003/030], Step [2200/2668], Total_loss: 0.0056
2024-09-02 04:43:14.034129 Epoch [003/030], Step [2400/2668], Total_loss: 0.0588
2024-09-02 04:44:24.532816 Epoch [003/030], Step [2600/2668], Total_loss: 0.0283
2024-09-02 04:44:47.420071 Epoch [003/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.6654999852180481
nature accu:0.9991666674613953
val on:imagenet_ai_0508_adm, Epoch:3, Accuracy:0.8323333263397217
val on: imagenet_ai_0419_biggan
ai accu: 0.6328333020210266
nature accu:0.9991666674613953
val on:imagenet_ai_0419_biggan, Epoch:3, Accuracy:0.8159999847412109
val on: imagenet_glide
ai accu: 0.9014999866485596
nature accu:0.9988332986831665
val on:imagenet_glide, Epoch:3, Accuracy:0.950166642665863
val on: imagenet_midjourney
ai accu: 0.5133333206176758
nature accu:0.9988332986831665
val on:imagenet_midjourney, Epoch:3, Accuracy:0.7560833096504211
val on: imagenet_ai_0419_sdv4
ai accu: 0.9771666526794434
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:3, Accuracy:0.9884166717529297
val on: imagenet_ai_0424_sdv5
ai accu: 0.9743750691413879
nature accu:0.9982500672340393
val on:imagenet_ai_0424_sdv5, Epoch:3, Accuracy:0.9863125681877136
val on: imagenet_ai_0419_vqdm
ai accu: 0.7436666488647461
nature accu:0.9986666440963745
val on:imagenet_ai_0419_vqdm, Epoch:3, Accuracy:0.8711666464805603
val on: imagenet_ai_0424_wukong
ai accu: 0.9463333487510681
nature accu:0.9986666440963745
val on:imagenet_ai_0424_wukong, Epoch:3, Accuracy:0.9724999666213989
Save state_dict successfully! Best epoch:3.
Epoch:3,Accuracy:0.9002099633216858, bestEpoch:3, bestAccu:0.9002099633216858
2024-09-02 04:55:28.269620 Epoch [004/030], Step [0001/2668], Total_loss: 0.0006
2024-09-02 04:57:11.532117 Epoch [004/030], Step [0200/2668], Total_loss: 0.0002
2024-09-02 04:58:52.186364 Epoch [004/030], Step [0400/2668], Total_loss: 0.0008
2024-09-02 05:00:50.286133 Epoch [004/030], Step [0600/2668], Total_loss: 0.0002
2024-09-02 05:02:18.193084 Epoch [004/030], Step [0800/2668], Total_loss: 0.0003
2024-09-02 05:03:39.234423 Epoch [004/030], Step [1000/2668], Total_loss: 0.0008
2024-09-02 05:04:55.247993 Epoch [004/030], Step [1200/2668], Total_loss: 0.0018
2024-09-02 05:06:24.609319 Epoch [004/030], Step [1400/2668], Total_loss: 0.0000
2024-09-02 05:07:50.234484 Epoch [004/030], Step [1600/2668], Total_loss: 0.0345
2024-09-02 05:09:12.946412 Epoch [004/030], Step [1800/2668], Total_loss: 0.0013
2024-09-02 05:10:29.832025 Epoch [004/030], Step [2000/2668], Total_loss: 0.0108
2024-09-02 05:11:42.837488 Epoch [004/030], Step [2200/2668], Total_loss: 0.0011
2024-09-02 05:12:54.237292 Epoch [004/030], Step [2400/2668], Total_loss: 0.0005
2024-09-02 05:14:05.285870 Epoch [004/030], Step [2600/2668], Total_loss: 0.1391
2024-09-02 05:14:30.479185 Epoch [004/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.6178333163261414
nature accu:0.9990000128746033
val on:imagenet_ai_0508_adm, Epoch:4, Accuracy:0.8084166646003723
val on: imagenet_ai_0419_biggan
ai accu: 0.5924999713897705
nature accu:0.9988332986831665
val on:imagenet_ai_0419_biggan, Epoch:4, Accuracy:0.7956666350364685
val on: imagenet_glide
ai accu: 0.9151666760444641
nature accu:0.9986666440963745
val on:imagenet_glide, Epoch:4, Accuracy:0.9569166302680969
val on: imagenet_midjourney
ai accu: 0.5214999914169312
nature accu:0.9984999895095825
val on:imagenet_midjourney, Epoch:4, Accuracy:0.7599999904632568
val on: imagenet_ai_0419_sdv4
ai accu: 0.9754999876022339
nature accu:0.9993333220481873
val on:imagenet_ai_0419_sdv4, Epoch:4, Accuracy:0.987416684627533
val on: imagenet_ai_0424_sdv5
ai accu: 0.9737500548362732
nature accu:0.9987500309944153
val on:imagenet_ai_0424_sdv5, Epoch:4, Accuracy:0.9862500429153442
val on: imagenet_ai_0419_vqdm
ai accu: 0.7339999675750732
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:4, Accuracy:0.8667500019073486
val on: imagenet_ai_0424_wukong
ai accu: 0.953499972820282
nature accu:0.9990000128746033
val on:imagenet_ai_0424_wukong, Epoch:4, Accuracy:0.9762499928474426
Epoch:4,Accuracy:0.8959699869155884, bestEpoch:3, bestAccu:0.9002099633216858
2024-09-02 05:25:45.735166 Epoch [005/030], Step [0001/2668], Total_loss: 0.0083
2024-09-02 05:26:54.185905 Epoch [005/030], Step [0200/2668], Total_loss: 0.0049
2024-09-02 05:28:03.409357 Epoch [005/030], Step [0400/2668], Total_loss: 0.0180
2024-09-02 05:29:11.721932 Epoch [005/030], Step [0600/2668], Total_loss: 0.0005
2024-09-02 05:30:21.423233 Epoch [005/030], Step [0800/2668], Total_loss: 0.0007
2024-09-02 05:31:29.786048 Epoch [005/030], Step [1000/2668], Total_loss: 0.0418
2024-09-02 05:32:39.793858 Epoch [005/030], Step [1200/2668], Total_loss: 0.0032
2024-09-02 05:33:49.625158 Epoch [005/030], Step [1400/2668], Total_loss: 0.0012
2024-09-02 05:34:58.834560 Epoch [005/030], Step [1600/2668], Total_loss: 0.0001
2024-09-02 05:36:08.886166 Epoch [005/030], Step [1800/2668], Total_loss: 0.0005
2024-09-02 05:37:18.033446 Epoch [005/030], Step [2000/2668], Total_loss: 0.0518
2024-09-02 05:38:27.485895 Epoch [005/030], Step [2200/2668], Total_loss: 0.0013
2024-09-02 05:39:36.419297 Epoch [005/030], Step [2400/2668], Total_loss: 0.0001
2024-09-02 05:40:45.232556 Epoch [005/030], Step [2600/2668], Total_loss: 0.0009
2024-09-02 05:41:07.909290 Epoch [005/030], Step [2668/2668], Total_loss: 0.0015
val on: imagenet_ai_0508_adm
ai accu: 0.6735000014305115
nature accu:0.9990000128746033
val on:imagenet_ai_0508_adm, Epoch:5, Accuracy:0.8362500071525574
val on: imagenet_ai_0419_biggan
ai accu: 0.6318333148956299
nature accu:0.9988332986831665
val on:imagenet_ai_0419_biggan, Epoch:5, Accuracy:0.8153333067893982
val on: imagenet_glide
ai accu: 0.9416666626930237
nature accu:0.9991666674613953
val on:imagenet_glide, Epoch:5, Accuracy:0.9704166650772095
val on: imagenet_midjourney
ai accu: 0.6066666841506958
nature accu:0.9990000128746033
val on:imagenet_midjourney, Epoch:5, Accuracy:0.8028333187103271
val on: imagenet_ai_0419_sdv4
ai accu: 0.984333336353302
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:5, Accuracy:0.9919166564941406
val on: imagenet_ai_0424_sdv5
ai accu: 0.98375004529953
nature accu:0.999125063419342
val on:imagenet_ai_0424_sdv5, Epoch:5, Accuracy:0.991437554359436
val on: imagenet_ai_0419_vqdm
ai accu: 0.7138333320617676
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:5, Accuracy:0.8566666841506958
val on: imagenet_ai_0424_wukong
ai accu: 0.9546666741371155
nature accu:0.9993333220481873
val on:imagenet_ai_0424_wukong, Epoch:5, Accuracy:0.9769999980926514
Save state_dict successfully! Best epoch:5.
Epoch:5,Accuracy:0.9086799621582031, bestEpoch:5, bestAccu:0.9086799621582031
2024-09-02 05:51:39.585760 Epoch [006/030], Step [0001/2668], Total_loss: 0.0003
2024-09-02 05:52:47.986196 Epoch [006/030], Step [0200/2668], Total_loss: 0.0272
2024-09-02 05:53:56.733096 Epoch [006/030], Step [0400/2668], Total_loss: 0.0002
2024-09-02 05:55:06.101004 Epoch [006/030], Step [0600/2668], Total_loss: 0.0001
2024-09-02 05:56:15.249498 Epoch [006/030], Step [0800/2668], Total_loss: 0.0000
2024-09-02 05:57:23.885996 Epoch [006/030], Step [1000/2668], Total_loss: 0.0203
2024-09-02 05:58:34.029080 Epoch [006/030], Step [1200/2668], Total_loss: 0.0003
2024-09-02 05:59:43.386116 Epoch [006/030], Step [1400/2668], Total_loss: 0.0007
2024-09-02 06:00:53.232779 Epoch [006/030], Step [1600/2668], Total_loss: 0.0001
2024-09-02 06:02:02.632206 Epoch [006/030], Step [1800/2668], Total_loss: 0.0015
2024-09-02 06:03:12.829935 Epoch [006/030], Step [2000/2668], Total_loss: 0.0052
2024-09-02 06:04:20.634423 Epoch [006/030], Step [2200/2668], Total_loss: 0.0010
2024-09-02 06:05:29.036402 Epoch [006/030], Step [2400/2668], Total_loss: 0.0002
2024-09-02 06:06:37.436102 Epoch [006/030], Step [2600/2668], Total_loss: 0.0001
2024-09-02 06:07:00.197851 Epoch [006/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.4661666750907898
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:6, Accuracy:0.7329999804496765
val on: imagenet_ai_0419_biggan
ai accu: 0.4178333282470703
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:6, Accuracy:0.7089166641235352
val on: imagenet_glide
ai accu: 0.7319999933242798
nature accu:1.0
val on:imagenet_glide, Epoch:6, Accuracy:0.8659999966621399
val on: imagenet_midjourney
ai accu: 0.4698333144187927
nature accu:1.0
val on:imagenet_midjourney, Epoch:6, Accuracy:0.7349166870117188
val on: imagenet_ai_0419_sdv4
ai accu: 0.9616666436195374
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:6, Accuracy:0.9807499647140503
val on: imagenet_ai_0424_sdv5
ai accu: 0.9610000252723694
nature accu:0.999750018119812
val on:imagenet_ai_0424_sdv5, Epoch:6, Accuracy:0.9803750514984131
val on: imagenet_ai_0419_vqdm
ai accu: 0.6246666312217712
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:6, Accuracy:0.812250018119812
val on: imagenet_ai_0424_wukong
ai accu: 0.9038333296775818
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:6, Accuracy:0.9518333077430725
Epoch:6,Accuracy:0.8513799905776978, bestEpoch:5, bestAccu:0.9086799621582031
2024-09-02 06:17:29.133235 Epoch [007/030], Step [0001/2668], Total_loss: 0.0042
2024-09-02 06:18:37.408011 Epoch [007/030], Step [0200/2668], Total_loss: 0.0004
2024-09-02 06:19:45.927823 Epoch [007/030], Step [0400/2668], Total_loss: 0.0280
2024-09-02 06:20:55.886181 Epoch [007/030], Step [0600/2668], Total_loss: 0.0002
2024-09-02 06:22:05.034370 Epoch [007/030], Step [0800/2668], Total_loss: 0.0014
2024-09-02 06:23:13.685939 Epoch [007/030], Step [1000/2668], Total_loss: 0.0025
2024-09-02 06:24:22.387621 Epoch [007/030], Step [1200/2668], Total_loss: 0.0050
2024-09-02 06:25:31.648561 Epoch [007/030], Step [1400/2668], Total_loss: 0.0014
2024-09-02 06:26:40.066707 Epoch [007/030], Step [1600/2668], Total_loss: 0.0088
2024-09-02 06:27:49.033556 Epoch [007/030], Step [1800/2668], Total_loss: 0.0001
2024-09-02 06:28:56.786336 Epoch [007/030], Step [2000/2668], Total_loss: 0.0006
2024-09-02 06:30:06.832167 Epoch [007/030], Step [2200/2668], Total_loss: 0.0115
2024-09-02 06:31:14.686184 Epoch [007/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 06:32:24.134227 Epoch [007/030], Step [2600/2668], Total_loss: 0.0004
2024-09-02 06:32:46.567943 Epoch [007/030], Step [2668/2668], Total_loss: 0.0006
val on: imagenet_ai_0508_adm
ai accu: 0.6959999799728394
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:7, Accuracy:0.8477500081062317
val on: imagenet_ai_0419_biggan
ai accu: 0.64083331823349
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:7, Accuracy:0.8204166293144226
val on: imagenet_glide
ai accu: 0.8728333115577698
nature accu:0.9996666312217712
val on:imagenet_glide, Epoch:7, Accuracy:0.9362499713897705
val on: imagenet_midjourney
ai accu: 0.5579999685287476
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:7, Accuracy:0.7789166569709778
val on: imagenet_ai_0419_sdv4
ai accu: 0.9649999737739563
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:7, Accuracy:0.9824166297912598
val on: imagenet_ai_0424_sdv5
ai accu: 0.968375027179718
nature accu:0.999500036239624
val on:imagenet_ai_0424_sdv5, Epoch:7, Accuracy:0.9839375615119934
val on: imagenet_ai_0419_vqdm
ai accu: 0.7901666760444641
nature accu:0.9996666312217712
val on:imagenet_ai_0419_vqdm, Epoch:7, Accuracy:0.8949166536331177
val on: imagenet_ai_0424_wukong
ai accu: 0.9393333196640015
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:7, Accuracy:0.9696666598320007
Epoch:7,Accuracy:0.9050700068473816, bestEpoch:5, bestAccu:0.9086799621582031
2024-09-02 06:43:14.932524 Epoch [008/030], Step [0001/2668], Total_loss: 0.0004
2024-09-02 06:44:22.432588 Epoch [008/030], Step [0200/2668], Total_loss: 0.0002
2024-09-02 06:45:30.086253 Epoch [008/030], Step [0400/2668], Total_loss: 0.0127
2024-09-02 06:46:40.333140 Epoch [008/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 06:47:49.285775 Epoch [008/030], Step [0800/2668], Total_loss: 0.0000
2024-09-02 06:48:58.149630 Epoch [008/030], Step [1000/2668], Total_loss: 0.0006
2024-09-02 06:50:07.033888 Epoch [008/030], Step [1200/2668], Total_loss: 0.0006
2024-09-02 06:51:17.600324 Epoch [008/030], Step [1400/2668], Total_loss: 0.0000
2024-09-02 06:52:26.185933 Epoch [008/030], Step [1600/2668], Total_loss: 0.0000
2024-09-02 06:53:35.285962 Epoch [008/030], Step [1800/2668], Total_loss: 0.0001
2024-09-02 06:54:44.041420 Epoch [008/030], Step [2000/2668], Total_loss: 0.0012
2024-09-02 06:55:52.286155 Epoch [008/030], Step [2200/2668], Total_loss: 0.0003
2024-09-02 06:57:00.401160 Epoch [008/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 06:58:09.786154 Epoch [008/030], Step [2600/2668], Total_loss: 0.0007
2024-09-02 06:58:32.531666 Epoch [008/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.6553333401679993
nature accu:0.9981666803359985
val on:imagenet_ai_0508_adm, Epoch:8, Accuracy:0.8267499804496765
val on: imagenet_ai_0419_biggan
ai accu: 0.7303333282470703
nature accu:0.9990000128746033
val on:imagenet_ai_0419_biggan, Epoch:8, Accuracy:0.8646666407585144
val on: imagenet_glide
ai accu: 0.9038333296775818
nature accu:0.9991666674613953
val on:imagenet_glide, Epoch:8, Accuracy:0.9514999985694885
val on: imagenet_midjourney
ai accu: 0.5856666564941406
nature accu:0.9993333220481873
val on:imagenet_midjourney, Epoch:8, Accuracy:0.7925000190734863
val on: imagenet_ai_0419_sdv4
ai accu: 0.984666645526886
nature accu:0.9979999661445618
val on:imagenet_ai_0419_sdv4, Epoch:8, Accuracy:0.9913333058357239
val on: imagenet_ai_0424_sdv5
ai accu: 0.9811250567436218
nature accu:0.9986250400543213
val on:imagenet_ai_0424_sdv5, Epoch:8, Accuracy:0.9898750185966492
val on: imagenet_ai_0419_vqdm
ai accu: 0.8006666302680969
nature accu:0.9983333349227905
val on:imagenet_ai_0419_vqdm, Epoch:8, Accuracy:0.8995000123977661
val on: imagenet_ai_0424_wukong
ai accu: 0.9606666564941406
nature accu:0.9990000128746033
val on:imagenet_ai_0424_wukong, Epoch:8, Accuracy:0.9798333048820496
Save state_dict successfully! Best epoch:8.
Epoch:8,Accuracy:0.9151099920272827, bestEpoch:8, bestAccu:0.9151099920272827
2024-09-02 07:09:03.035733 Epoch [009/030], Step [0001/2668], Total_loss: 0.0001
2024-09-02 07:10:10.795456 Epoch [009/030], Step [0200/2668], Total_loss: 0.0851
2024-09-02 07:11:19.399615 Epoch [009/030], Step [0400/2668], Total_loss: 0.0027
2024-09-02 07:12:28.330817 Epoch [009/030], Step [0600/2668], Total_loss: 0.0002
2024-09-02 07:13:40.206328 Epoch [009/030], Step [0800/2668], Total_loss: 0.0027
2024-09-02 07:14:48.637605 Epoch [009/030], Step [1000/2668], Total_loss: 0.0070
2024-09-02 07:15:57.546456 Epoch [009/030], Step [1200/2668], Total_loss: 0.0001
2024-09-02 07:17:06.163744 Epoch [009/030], Step [1400/2668], Total_loss: 0.0014
2024-09-02 07:18:14.446157 Epoch [009/030], Step [1600/2668], Total_loss: 0.0000
2024-09-02 07:19:26.686168 Epoch [009/030], Step [1800/2668], Total_loss: 0.0009
2024-09-02 07:20:34.408721 Epoch [009/030], Step [2000/2668], Total_loss: 0.0015
2024-09-02 07:21:43.432503 Epoch [009/030], Step [2200/2668], Total_loss: 0.0002
2024-09-02 07:22:53.134579 Epoch [009/030], Step [2400/2668], Total_loss: 0.0004
2024-09-02 07:24:06.033225 Epoch [009/030], Step [2600/2668], Total_loss: 0.0001
2024-09-02 07:24:28.440851 Epoch [009/030], Step [2668/2668], Total_loss: 0.0019
val on: imagenet_ai_0508_adm
ai accu: 0.5696666836738586
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:9, Accuracy:0.7848333120346069
val on: imagenet_ai_0419_biggan
ai accu: 0.4898333251476288
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:9, Accuracy:0.7449166774749756
val on: imagenet_glide
ai accu: 0.9070000052452087
nature accu:1.0
val on:imagenet_glide, Epoch:9, Accuracy:0.953499972820282
val on: imagenet_midjourney
ai accu: 0.5376666784286499
nature accu:0.9996666312217712
val on:imagenet_midjourney, Epoch:9, Accuracy:0.768666684627533
val on: imagenet_ai_0419_sdv4
ai accu: 0.9866666793823242
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:9, Accuracy:0.9932500123977661
val on: imagenet_ai_0424_sdv5
ai accu: 0.9845000505447388
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:9, Accuracy:0.9921875596046448
val on: imagenet_ai_0419_vqdm
ai accu: 0.6536666750907898
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:9, Accuracy:0.8268333077430725
val on: imagenet_ai_0424_wukong
ai accu: 0.9564999938011169
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:9, Accuracy:0.9780833125114441
Epoch:9,Accuracy:0.8847599625587463, bestEpoch:8, bestAccu:0.9151099920272827
2024-09-02 07:36:18.732758 Epoch [010/030], Step [0001/2668], Total_loss: 0.0014
2024-09-02 07:37:27.185982 Epoch [010/030], Step [0200/2668], Total_loss: 0.0032
2024-09-02 07:38:37.086488 Epoch [010/030], Step [0400/2668], Total_loss: 0.0001
2024-09-02 07:39:46.731687 Epoch [010/030], Step [0600/2668], Total_loss: 0.0007
2024-09-02 07:40:55.633272 Epoch [010/030], Step [0800/2668], Total_loss: 0.0001
2024-09-02 07:42:05.333467 Epoch [010/030], Step [1000/2668], Total_loss: 0.0082
2024-09-02 07:43:14.886371 Epoch [010/030], Step [1200/2668], Total_loss: 0.0153
2024-09-02 07:44:24.634157 Epoch [010/030], Step [1400/2668], Total_loss: 0.0014
2024-09-02 07:45:34.735348 Epoch [010/030], Step [1600/2668], Total_loss: 0.0006
2024-09-02 07:46:44.585973 Epoch [010/030], Step [1800/2668], Total_loss: 0.0001
2024-09-02 07:47:52.786124 Epoch [010/030], Step [2000/2668], Total_loss: 0.0011
2024-09-02 07:49:04.937183 Epoch [010/030], Step [2200/2668], Total_loss: 0.0000
2024-09-02 07:50:21.432222 Epoch [010/030], Step [2400/2668], Total_loss: 0.0004
2024-09-02 07:51:36.633487 Epoch [010/030], Step [2600/2668], Total_loss: 0.0049
2024-09-02 07:52:05.025315 Epoch [010/030], Step [2668/2668], Total_loss: 0.0017
val on: imagenet_ai_0508_adm
ai accu: 0.6313333511352539
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:10, Accuracy:0.8154166340827942
val on: imagenet_ai_0419_biggan
ai accu: 0.6599999666213989
nature accu:0.9994999766349792
val on:imagenet_ai_0419_biggan, Epoch:10, Accuracy:0.8297500014305115
val on: imagenet_glide
ai accu: 0.9238333106040955
nature accu:0.9996666312217712
val on:imagenet_glide, Epoch:10, Accuracy:0.9617499709129333
val on: imagenet_midjourney
ai accu: 0.5485000014305115
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:10, Accuracy:0.7739999890327454
val on: imagenet_ai_0419_sdv4
ai accu: 0.9826666712760925
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:10, Accuracy:0.9910833239555359
val on: imagenet_ai_0424_sdv5
ai accu: 0.9820000529289246
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:10, Accuracy:0.9908125400543213
val on: imagenet_ai_0419_vqdm
ai accu: 0.7983333468437195
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:10, Accuracy:0.8990833163261414
val on: imagenet_ai_0424_wukong
ai accu: 0.9608333110809326
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:10, Accuracy:0.9801666736602783
Epoch:10,Accuracy:0.9086799621582031, bestEpoch:8, bestAccu:0.9151099920272827
2024-09-02 08:03:07.886189 Epoch [011/030], Step [0001/2668], Total_loss: 0.0012
2024-09-02 08:04:17.730058 Epoch [011/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 08:05:27.731320 Epoch [011/030], Step [0400/2668], Total_loss: 0.0001
2024-09-02 08:06:38.436914 Epoch [011/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 08:07:51.443904 Epoch [011/030], Step [0800/2668], Total_loss: 0.0005
2024-09-02 08:09:03.139498 Epoch [011/030], Step [1000/2668], Total_loss: 0.0005
2024-09-02 08:10:13.729822 Epoch [011/030], Step [1200/2668], Total_loss: 0.0001
2024-09-02 08:11:23.786460 Epoch [011/030], Step [1400/2668], Total_loss: 0.0002
2024-09-02 08:12:33.632581 Epoch [011/030], Step [1600/2668], Total_loss: 0.0005
2024-09-02 08:13:56.585891 Epoch [011/030], Step [1800/2668], Total_loss: 0.0002
2024-09-02 08:15:35.257713 Epoch [011/030], Step [2000/2668], Total_loss: 0.0007
2024-09-02 08:16:52.985976 Epoch [011/030], Step [2200/2668], Total_loss: 0.0005
2024-09-02 08:18:10.486053 Epoch [011/030], Step [2400/2668], Total_loss: 0.0013
2024-09-02 08:19:25.048661 Epoch [011/030], Step [2600/2668], Total_loss: 0.0035
2024-09-02 08:19:51.653231 Epoch [011/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.6069999933242798
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:11, Accuracy:0.8034166693687439
val on: imagenet_ai_0419_biggan
ai accu: 0.468833327293396
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:11, Accuracy:0.734333336353302
val on: imagenet_glide
ai accu: 0.9321666359901428
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:11, Accuracy:0.965999960899353
val on: imagenet_midjourney
ai accu: 0.5956666469573975
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:11, Accuracy:0.7975833415985107
val on: imagenet_ai_0419_sdv4
ai accu: 0.987500011920929
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:11, Accuracy:0.9935833215713501
val on: imagenet_ai_0424_sdv5
ai accu: 0.9865000247955322
nature accu:0.999500036239624
val on:imagenet_ai_0424_sdv5, Epoch:11, Accuracy:0.9930000305175781
val on: imagenet_ai_0419_vqdm
ai accu: 0.7026666402816772
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:11, Accuracy:0.8512499928474426
val on: imagenet_ai_0424_wukong
ai accu: 0.9703333377838135
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:11, Accuracy:0.984916627407074
Epoch:11,Accuracy:0.8946099877357483, bestEpoch:8, bestAccu:0.9151099920272827
2024-09-02 08:31:14.485886 Epoch [012/030], Step [0001/2668], Total_loss: 0.0000
2024-09-02 08:32:28.037105 Epoch [012/030], Step [0200/2668], Total_loss: 0.0000
2024-09-02 08:33:42.019572 Epoch [012/030], Step [0400/2668], Total_loss: 0.0012
2024-09-02 08:34:59.837176 Epoch [012/030], Step [0600/2668], Total_loss: 0.0001
2024-09-02 08:36:15.533133 Epoch [012/030], Step [0800/2668], Total_loss: 0.0003
2024-09-02 08:37:27.793056 Epoch [012/030], Step [1000/2668], Total_loss: 0.0007
2024-09-02 08:38:40.285961 Epoch [012/030], Step [1200/2668], Total_loss: 0.0002
2024-09-02 08:39:55.454749 Epoch [012/030], Step [1400/2668], Total_loss: 0.0004
2024-09-02 08:41:32.986475 Epoch [012/030], Step [1600/2668], Total_loss: 0.0009
2024-09-02 08:43:11.186095 Epoch [012/030], Step [1800/2668], Total_loss: 0.0004
2024-09-02 08:44:45.385823 Epoch [012/030], Step [2000/2668], Total_loss: 0.0001
2024-09-02 08:46:52.897755 Epoch [012/030], Step [2200/2668], Total_loss: 0.0004
2024-09-02 08:48:38.386043 Epoch [012/030], Step [2400/2668], Total_loss: 0.0003
2024-09-02 08:50:08.686248 Epoch [012/030], Step [2600/2668], Total_loss: 0.0002
2024-09-02 08:50:40.785893 Epoch [012/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.7316666841506958
nature accu:0.9993333220481873
val on:imagenet_ai_0508_adm, Epoch:12, Accuracy:0.8654999732971191
val on: imagenet_ai_0419_biggan
ai accu: 0.7786666750907898
nature accu:0.9993333220481873
val on:imagenet_ai_0419_biggan, Epoch:12, Accuracy:0.8889999985694885
val on: imagenet_glide
ai accu: 0.9583333134651184
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:12, Accuracy:0.9789166450500488
val on: imagenet_midjourney
ai accu: 0.6424999833106995
nature accu:0.9994999766349792
val on:imagenet_midjourney, Epoch:12, Accuracy:0.8209999799728394
val on: imagenet_ai_0419_sdv4
ai accu: 0.9894999861717224
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:12, Accuracy:0.9945833086967468
val on: imagenet_ai_0424_sdv5
ai accu: 0.9901250600814819
nature accu:0.999250054359436
val on:imagenet_ai_0424_sdv5, Epoch:12, Accuracy:0.994687557220459
val on: imagenet_ai_0419_vqdm
ai accu: 0.9016666412353516
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:12, Accuracy:0.9507499933242798
val on: imagenet_ai_0424_wukong
ai accu: 0.9818333387374878
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:12, Accuracy:0.9906666278839111
Save state_dict successfully! Best epoch:12.
Epoch:12,Accuracy:0.937999963760376, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 09:04:03.627692 Epoch [013/030], Step [0001/2668], Total_loss: 0.0002
2024-09-02 09:05:22.787048 Epoch [013/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 09:06:44.785987 Epoch [013/030], Step [0400/2668], Total_loss: 0.0005
2024-09-02 09:08:05.486634 Epoch [013/030], Step [0600/2668], Total_loss: 0.0002
2024-09-02 09:09:14.886036 Epoch [013/030], Step [0800/2668], Total_loss: 0.0013
2024-09-02 09:10:20.985799 Epoch [013/030], Step [1000/2668], Total_loss: 0.0001
2024-09-02 09:11:34.720932 Epoch [013/030], Step [1200/2668], Total_loss: 0.0002
2024-09-02 09:12:52.686458 Epoch [013/030], Step [1400/2668], Total_loss: 0.0023
2024-09-02 09:14:15.085910 Epoch [013/030], Step [1600/2668], Total_loss: 0.0003
2024-09-02 09:15:41.985952 Epoch [013/030], Step [1800/2668], Total_loss: 0.0006
2024-09-02 09:16:52.233433 Epoch [013/030], Step [2000/2668], Total_loss: 0.0001
2024-09-02 09:18:03.495140 Epoch [013/030], Step [2200/2668], Total_loss: 0.0010
2024-09-02 09:19:10.234085 Epoch [013/030], Step [2400/2668], Total_loss: 0.0005
2024-09-02 09:20:17.086285 Epoch [013/030], Step [2600/2668], Total_loss: 0.0050
2024-09-02 09:20:37.952466 Epoch [013/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.606333315372467
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:13, Accuracy:0.8031666874885559
val on: imagenet_ai_0419_biggan
ai accu: 0.6018333435058594
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:13, Accuracy:0.8008333444595337
val on: imagenet_glide
ai accu: 0.9004999995231628
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:13, Accuracy:0.950166642665863
val on: imagenet_midjourney
ai accu: 0.5836666822433472
nature accu:0.9996666312217712
val on:imagenet_midjourney, Epoch:13, Accuracy:0.7916666865348816
val on: imagenet_ai_0419_sdv4
ai accu: 0.9856666326522827
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:13, Accuracy:0.9927499890327454
val on: imagenet_ai_0424_sdv5
ai accu: 0.9853750467300415
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:13, Accuracy:0.9926250576972961
val on: imagenet_ai_0419_vqdm
ai accu: 0.7458333373069763
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:13, Accuracy:0.8729166388511658
val on: imagenet_ai_0424_wukong
ai accu: 0.9661666750907898
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:13, Accuracy:0.9829166531562805
Epoch:13,Accuracy:0.9021499752998352, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 09:31:39.187130 Epoch [014/030], Step [0001/2668], Total_loss: 0.0005
2024-09-02 09:33:16.986335 Epoch [014/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 09:34:24.285972 Epoch [014/030], Step [0400/2668], Total_loss: 0.0000
2024-09-02 09:35:26.186042 Epoch [014/030], Step [0600/2668], Total_loss: 0.0166
2024-09-02 09:36:27.585980 Epoch [014/030], Step [0800/2668], Total_loss: 0.0004
2024-09-02 09:37:29.185851 Epoch [014/030], Step [1000/2668], Total_loss: 0.0006
2024-09-02 09:38:30.085502 Epoch [014/030], Step [1200/2668], Total_loss: 0.0011
2024-09-02 09:39:31.386593 Epoch [014/030], Step [1400/2668], Total_loss: 0.0001
2024-09-02 09:40:41.685926 Epoch [014/030], Step [1600/2668], Total_loss: 0.0001
2024-09-02 09:42:02.086244 Epoch [014/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 09:43:33.744901 Epoch [014/030], Step [2000/2668], Total_loss: 0.0004
2024-09-02 09:45:06.509588 Epoch [014/030], Step [2200/2668], Total_loss: 0.0007
2024-09-02 09:46:41.017160 Epoch [014/030], Step [2400/2668], Total_loss: 0.0117
2024-09-02 09:47:57.786278 Epoch [014/030], Step [2600/2668], Total_loss: 0.0011
2024-09-02 09:48:28.402161 Epoch [014/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.5963333249092102
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:14, Accuracy:0.7980833053588867
val on: imagenet_ai_0419_biggan
ai accu: 0.5448333024978638
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:14, Accuracy:0.7724166512489319
val on: imagenet_glide
ai accu: 0.9329999685287476
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:14, Accuracy:0.9664166569709778
val on: imagenet_midjourney
ai accu: 0.6060000061988831
nature accu:0.9996666312217712
val on:imagenet_midjourney, Epoch:14, Accuracy:0.8028333187103271
val on: imagenet_ai_0419_sdv4
ai accu: 0.9864999651908875
nature accu:0.9993333220481873
val on:imagenet_ai_0419_sdv4, Epoch:14, Accuracy:0.9929166436195374
val on: imagenet_ai_0424_sdv5
ai accu: 0.987375020980835
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:14, Accuracy:0.9935000538825989
val on: imagenet_ai_0419_vqdm
ai accu: 0.7608333230018616
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:14, Accuracy:0.8804166316986084
val on: imagenet_ai_0424_wukong
ai accu: 0.9716666340827942
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:14, Accuracy:0.9856666326522827
Epoch:14,Accuracy:0.9028099775314331, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 10:03:17.831633 Epoch [015/030], Step [0001/2668], Total_loss: 0.0002
2024-09-02 10:04:56.486239 Epoch [015/030], Step [0200/2668], Total_loss: 0.0010
2024-09-02 10:06:33.640315 Epoch [015/030], Step [0400/2668], Total_loss: 0.0004
2024-09-02 10:08:14.186340 Epoch [015/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 10:10:03.910184 Epoch [015/030], Step [0800/2668], Total_loss: 0.0007
2024-09-02 10:11:56.175333 Epoch [015/030], Step [1000/2668], Total_loss: 0.0001
2024-09-02 10:13:58.562854 Epoch [015/030], Step [1200/2668], Total_loss: 0.0002
2024-09-02 10:16:20.690871 Epoch [015/030], Step [1400/2668], Total_loss: 0.0003
2024-09-02 10:18:51.508792 Epoch [015/030], Step [1600/2668], Total_loss: 0.0006
2024-09-02 10:21:10.288436 Epoch [015/030], Step [1800/2668], Total_loss: 0.0002
2024-09-02 10:23:11.086528 Epoch [015/030], Step [2000/2668], Total_loss: 0.0014
2024-09-02 10:25:16.601246 Epoch [015/030], Step [2200/2668], Total_loss: 0.0002
2024-09-02 10:27:18.096157 Epoch [015/030], Step [2400/2668], Total_loss: 0.0002
2024-09-02 10:29:23.086160 Epoch [015/030], Step [2600/2668], Total_loss: 0.0004
2024-09-02 10:30:03.309069 Epoch [015/030], Step [2668/2668], Total_loss: 0.0005
val on: imagenet_ai_0508_adm
ai accu: 0.5943333506584167
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:15, Accuracy:0.797166645526886
val on: imagenet_ai_0419_biggan
ai accu: 0.5568333268165588
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:15, Accuracy:0.778416633605957
val on: imagenet_glide
ai accu: 0.9160000085830688
nature accu:1.0
val on:imagenet_glide, Epoch:15, Accuracy:0.9580000042915344
val on: imagenet_midjourney
ai accu: 0.5885000228881836
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:15, Accuracy:0.7941666841506958
val on: imagenet_ai_0419_sdv4
ai accu: 0.9888333082199097
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:15, Accuracy:0.9942499995231628
val on: imagenet_ai_0424_sdv5
ai accu: 0.9898750185966492
nature accu:1.0
val on:imagenet_ai_0424_sdv5, Epoch:15, Accuracy:0.994937539100647
val on: imagenet_ai_0419_vqdm
ai accu: 0.7124999761581421
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:15, Accuracy:0.856249988079071
val on: imagenet_ai_0424_wukong
ai accu: 0.9736666679382324
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:15, Accuracy:0.9867500066757202
Epoch:15,Accuracy:0.8989899754524231, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 10:44:52.085891 Epoch [016/030], Step [0001/2668], Total_loss: 0.0141
2024-09-02 10:46:28.387247 Epoch [016/030], Step [0200/2668], Total_loss: 0.0005
2024-09-02 10:48:10.286270 Epoch [016/030], Step [0400/2668], Total_loss: 0.0005
2024-09-02 10:49:16.106823 Epoch [016/030], Step [0600/2668], Total_loss: 0.0005
2024-09-02 10:50:20.406033 Epoch [016/030], Step [0800/2668], Total_loss: 0.0000
2024-09-02 10:51:25.686461 Epoch [016/030], Step [1000/2668], Total_loss: 0.0000
2024-09-02 10:52:32.686924 Epoch [016/030], Step [1200/2668], Total_loss: 0.0000
2024-09-02 10:53:41.431216 Epoch [016/030], Step [1400/2668], Total_loss: 0.0002
2024-09-02 10:54:50.286253 Epoch [016/030], Step [1600/2668], Total_loss: 0.0000
2024-09-02 10:56:00.195060 Epoch [016/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 10:57:11.286561 Epoch [016/030], Step [2000/2668], Total_loss: 0.0002
2024-09-02 10:58:23.586146 Epoch [016/030], Step [2200/2668], Total_loss: 0.0003
2024-09-02 10:59:30.986408 Epoch [016/030], Step [2400/2668], Total_loss: 0.0001
2024-09-02 11:00:38.885762 Epoch [016/030], Step [2600/2668], Total_loss: 0.0003
2024-09-02 11:01:00.742138 Epoch [016/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.6825000047683716
nature accu:0.9994999766349792
val on:imagenet_ai_0508_adm, Epoch:16, Accuracy:0.8410000205039978
val on: imagenet_ai_0419_biggan
ai accu: 0.7196666598320007
nature accu:0.9991666674613953
val on:imagenet_ai_0419_biggan, Epoch:16, Accuracy:0.859416663646698
val on: imagenet_glide
ai accu: 0.9545000195503235
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:16, Accuracy:0.9769999980926514
val on: imagenet_midjourney
ai accu: 0.6081666350364685
nature accu:0.9991666674613953
val on:imagenet_midjourney, Epoch:16, Accuracy:0.8036666512489319
val on: imagenet_ai_0419_sdv4
ai accu: 0.9904999732971191
nature accu:0.9994999766349792
val on:imagenet_ai_0419_sdv4, Epoch:16, Accuracy:0.9950000047683716
val on: imagenet_ai_0424_sdv5
ai accu: 0.987000048160553
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:16, Accuracy:0.9934375286102295
val on: imagenet_ai_0419_vqdm
ai accu: 0.8056666851043701
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:16, Accuracy:0.9028333425521851
val on: imagenet_ai_0424_wukong
ai accu: 0.9753333330154419
nature accu:0.9994999766349792
val on:imagenet_ai_0424_wukong, Epoch:16, Accuracy:0.987416684627533
Epoch:16,Accuracy:0.9229099750518799, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 11:11:31.985952 Epoch [017/030], Step [0001/2668], Total_loss: 0.0026
2024-09-02 11:12:45.386131 Epoch [017/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 11:13:54.185831 Epoch [017/030], Step [0400/2668], Total_loss: 0.0004
2024-09-02 11:15:02.885854 Epoch [017/030], Step [0600/2668], Total_loss: 0.0003
2024-09-02 11:16:10.634228 Epoch [017/030], Step [0800/2668], Total_loss: 0.0001
2024-09-02 11:17:21.986030 Epoch [017/030], Step [1000/2668], Total_loss: 0.0000
2024-09-02 11:18:27.886085 Epoch [017/030], Step [1200/2668], Total_loss: 0.0000
2024-09-02 11:19:33.085906 Epoch [017/030], Step [1400/2668], Total_loss: 0.0002
2024-09-02 11:20:36.785780 Epoch [017/030], Step [1600/2668], Total_loss: 0.0005
2024-09-02 11:21:40.886036 Epoch [017/030], Step [1800/2668], Total_loss: 0.0005
2024-09-02 11:22:45.386121 Epoch [017/030], Step [2000/2668], Total_loss: 0.0009
2024-09-02 11:23:49.985897 Epoch [017/030], Step [2200/2668], Total_loss: 0.0001
2024-09-02 11:24:53.786188 Epoch [017/030], Step [2400/2668], Total_loss: 0.0001
2024-09-02 11:25:56.385840 Epoch [017/030], Step [2600/2668], Total_loss: 0.0005
2024-09-02 11:26:16.593319 Epoch [017/030], Step [2668/2668], Total_loss: 0.0009
val on: imagenet_ai_0508_adm
ai accu: 0.6635000109672546
nature accu:0.9996666312217712
val on:imagenet_ai_0508_adm, Epoch:17, Accuracy:0.8315833210945129
val on: imagenet_ai_0419_biggan
ai accu: 0.7481666803359985
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:17, Accuracy:0.8740000128746033
val on: imagenet_glide
ai accu: 0.9318333268165588
nature accu:0.9994999766349792
val on:imagenet_glide, Epoch:17, Accuracy:0.965666651725769
val on: imagenet_midjourney
ai accu: 0.5914999842643738
nature accu:1.0
val on:imagenet_midjourney, Epoch:17, Accuracy:0.7957499623298645
val on: imagenet_ai_0419_sdv4
ai accu: 0.9889999628067017
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:17, Accuracy:0.9944166541099548
val on: imagenet_ai_0424_sdv5
ai accu: 0.9886250495910645
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:17, Accuracy:0.9942500591278076
val on: imagenet_ai_0419_vqdm
ai accu: 0.8616666793823242
nature accu:0.9994999766349792
val on:imagenet_ai_0419_vqdm, Epoch:17, Accuracy:0.9305832982063293
val on: imagenet_ai_0424_wukong
ai accu: 0.9778333306312561
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:17, Accuracy:0.9888333082199097
Epoch:17,Accuracy:0.9247799515724182, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 11:35:28.286409 Epoch [018/030], Step [0001/2668], Total_loss: 0.0003
2024-09-02 11:36:30.307918 Epoch [018/030], Step [0200/2668], Total_loss: 0.0000
2024-09-02 11:37:31.285826 Epoch [018/030], Step [0400/2668], Total_loss: 0.0001
2024-09-02 11:38:32.632920 Epoch [018/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 11:39:33.585820 Epoch [018/030], Step [0800/2668], Total_loss: 0.0009
2024-09-02 11:40:35.286374 Epoch [018/030], Step [1000/2668], Total_loss: 0.0001
2024-09-02 11:41:36.286052 Epoch [018/030], Step [1200/2668], Total_loss: 0.0019
2024-09-02 11:42:37.786079 Epoch [018/030], Step [1400/2668], Total_loss: 0.0002
2024-09-02 11:43:40.386481 Epoch [018/030], Step [1600/2668], Total_loss: 0.0000
2024-09-02 11:44:42.285926 Epoch [018/030], Step [1800/2668], Total_loss: 0.0003
2024-09-02 11:45:49.286164 Epoch [018/030], Step [2000/2668], Total_loss: 0.0002
2024-09-02 11:46:59.786488 Epoch [018/030], Step [2200/2668], Total_loss: 0.0011
2024-09-02 11:48:04.486230 Epoch [018/030], Step [2400/2668], Total_loss: 0.0005
2024-09-02 11:49:09.686020 Epoch [018/030], Step [2600/2668], Total_loss: 0.0005
2024-09-02 11:49:29.896967 Epoch [018/030], Step [2668/2668], Total_loss: 0.0003
val on: imagenet_ai_0508_adm
ai accu: 0.6159999966621399
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:18, Accuracy:0.8079166412353516
val on: imagenet_ai_0419_biggan
ai accu: 0.5673333406448364
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:18, Accuracy:0.7835000157356262
val on: imagenet_glide
ai accu: 0.9278333187103271
nature accu:1.0
val on:imagenet_glide, Epoch:18, Accuracy:0.9639166593551636
val on: imagenet_midjourney
ai accu: 0.5771666765213013
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:18, Accuracy:0.7885000109672546
val on: imagenet_ai_0419_sdv4
ai accu: 0.9894999861717224
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:18, Accuracy:0.9945833086967468
val on: imagenet_ai_0424_sdv5
ai accu: 0.9865000247955322
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:18, Accuracy:0.9930625557899475
val on: imagenet_ai_0419_vqdm
ai accu: 0.7253333330154419
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:18, Accuracy:0.862666666507721
val on: imagenet_ai_0424_wukong
ai accu: 0.9696666598320007
nature accu:0.9996666312217712
val on:imagenet_ai_0424_wukong, Epoch:18, Accuracy:0.984666645526886
Epoch:18,Accuracy:0.9011799693107605, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 11:59:51.486379 Epoch [019/030], Step [0001/2668], Total_loss: 0.0004
2024-09-02 12:00:52.585954 Epoch [019/030], Step [0200/2668], Total_loss: 0.0004
2024-09-02 12:02:01.085773 Epoch [019/030], Step [0400/2668], Total_loss: 0.0000
2024-09-02 12:03:22.186571 Epoch [019/030], Step [0600/2668], Total_loss: 0.0010
2024-09-02 12:04:23.785965 Epoch [019/030], Step [0800/2668], Total_loss: 0.0005
2024-09-02 12:05:26.085771 Epoch [019/030], Step [1000/2668], Total_loss: 0.0057
2024-09-02 12:06:35.185740 Epoch [019/030], Step [1200/2668], Total_loss: 0.0000
2024-09-02 12:07:37.685727 Epoch [019/030], Step [1400/2668], Total_loss: 0.0004
2024-09-02 12:08:40.086054 Epoch [019/030], Step [1600/2668], Total_loss: 0.0001
2024-09-02 12:09:43.285968 Epoch [019/030], Step [1800/2668], Total_loss: 0.0007
2024-09-02 12:10:44.785741 Epoch [019/030], Step [2000/2668], Total_loss: 0.0002
2024-09-02 12:11:47.185115 Epoch [019/030], Step [2200/2668], Total_loss: 0.0000
2024-09-02 12:12:49.086459 Epoch [019/030], Step [2400/2668], Total_loss: 0.0027
2024-09-02 12:13:55.485737 Epoch [019/030], Step [2600/2668], Total_loss: 0.0002
2024-09-02 12:14:15.921355 Epoch [019/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.6241666674613953
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:19, Accuracy:0.8119999766349792
val on: imagenet_ai_0419_biggan
ai accu: 0.5945000052452087
nature accu:0.9996666312217712
val on:imagenet_ai_0419_biggan, Epoch:19, Accuracy:0.79708331823349
val on: imagenet_glide
ai accu: 0.9206666350364685
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:19, Accuracy:0.9602499604225159
val on: imagenet_midjourney
ai accu: 0.5398333072662354
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:19, Accuracy:0.7698333263397217
val on: imagenet_ai_0419_sdv4
ai accu: 0.9896666407585144
nature accu:1.0
val on:imagenet_ai_0419_sdv4, Epoch:19, Accuracy:0.9948333501815796
val on: imagenet_ai_0424_sdv5
ai accu: 0.9858750700950623
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:19, Accuracy:0.9927500486373901
val on: imagenet_ai_0419_vqdm
ai accu: 0.7954999804496765
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:19, Accuracy:0.8976666331291199
val on: imagenet_ai_0424_wukong
ai accu: 0.9763333201408386
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:19, Accuracy:0.9880833029747009
Epoch:19,Accuracy:0.9052099585533142, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 12:23:29.386391 Epoch [020/030], Step [0001/2668], Total_loss: 0.0002
2024-09-02 12:24:30.886069 Epoch [020/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 12:25:42.105118 Epoch [020/030], Step [0400/2668], Total_loss: 0.0002
2024-09-02 12:26:47.185796 Epoch [020/030], Step [0600/2668], Total_loss: 0.0007
2024-09-02 12:27:52.085742 Epoch [020/030], Step [0800/2668], Total_loss: 0.0003
2024-09-02 12:28:57.186149 Epoch [020/030], Step [1000/2668], Total_loss: 0.0003
2024-09-02 12:30:04.085819 Epoch [020/030], Step [1200/2668], Total_loss: 0.0002
2024-09-02 12:31:05.585762 Epoch [020/030], Step [1400/2668], Total_loss: 0.0005
2024-09-02 12:32:07.086780 Epoch [020/030], Step [1600/2668], Total_loss: 0.0001
2024-09-02 12:33:13.785855 Epoch [020/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 12:34:17.985880 Epoch [020/030], Step [2000/2668], Total_loss: 0.0016
2024-09-02 12:35:24.185953 Epoch [020/030], Step [2200/2668], Total_loss: 0.0175
2024-09-02 12:36:28.486026 Epoch [020/030], Step [2400/2668], Total_loss: 0.0011
2024-09-02 12:37:30.808045 Epoch [020/030], Step [2600/2668], Total_loss: 0.0005
2024-09-02 12:37:51.394190 Epoch [020/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5411666631698608
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:20, Accuracy:0.7705833315849304
val on: imagenet_ai_0419_biggan
ai accu: 0.5901666879653931
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:20, Accuracy:0.7950833439826965
val on: imagenet_glide
ai accu: 0.8984999656677246
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:20, Accuracy:0.9491666555404663
val on: imagenet_midjourney
ai accu: 0.5916666388511658
nature accu:1.0
val on:imagenet_midjourney, Epoch:20, Accuracy:0.7958333492279053
val on: imagenet_ai_0419_sdv4
ai accu: 0.9933333396911621
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:20, Accuracy:0.9965000152587891
val on: imagenet_ai_0424_sdv5
ai accu: 0.9925000667572021
nature accu:0.999750018119812
val on:imagenet_ai_0424_sdv5, Epoch:20, Accuracy:0.9961250424385071
val on: imagenet_ai_0419_vqdm
ai accu: 0.7743332982063293
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:20, Accuracy:0.8870833516120911
val on: imagenet_ai_0424_wukong
ai accu: 0.9774999618530273
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:20, Accuracy:0.9887499809265137
Epoch:20,Accuracy:0.9013399481773376, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 12:47:40.995543 Epoch [021/030], Step [0001/2668], Total_loss: 0.0015
2024-09-02 12:48:43.986756 Epoch [021/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 12:49:46.885729 Epoch [021/030], Step [0400/2668], Total_loss: 0.0001
2024-09-02 12:50:49.385831 Epoch [021/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 12:51:51.486100 Epoch [021/030], Step [0800/2668], Total_loss: 0.0000
2024-09-02 12:52:54.485999 Epoch [021/030], Step [1000/2668], Total_loss: 0.0001
2024-09-02 12:53:56.386002 Epoch [021/030], Step [1200/2668], Total_loss: 0.0110
2024-09-02 12:55:09.104785 Epoch [021/030], Step [1400/2668], Total_loss: 0.0004
2024-09-02 12:56:14.496250 Epoch [021/030], Step [1600/2668], Total_loss: 0.0000
2024-09-02 12:57:20.736101 Epoch [021/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 12:58:27.786252 Epoch [021/030], Step [2000/2668], Total_loss: 0.0002
2024-09-02 12:59:35.084736 Epoch [021/030], Step [2200/2668], Total_loss: 0.0001
2024-09-02 13:00:39.385968 Epoch [021/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 13:01:47.786029 Epoch [021/030], Step [2600/2668], Total_loss: 0.0001
2024-09-02 13:02:12.111847 Epoch [021/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5108333230018616
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:21, Accuracy:0.7554166316986084
val on: imagenet_ai_0419_biggan
ai accu: 0.39016667008399963
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:21, Accuracy:0.6950833201408386
val on: imagenet_glide
ai accu: 0.8798333406448364
nature accu:1.0
val on:imagenet_glide, Epoch:21, Accuracy:0.9399166703224182
val on: imagenet_midjourney
ai accu: 0.5801666378974915
nature accu:1.0
val on:imagenet_midjourney, Epoch:21, Accuracy:0.7900833487510681
val on: imagenet_ai_0419_sdv4
ai accu: 0.9894999861717224
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:21, Accuracy:0.9945833086967468
val on: imagenet_ai_0424_sdv5
ai accu: 0.9900000691413879
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:21, Accuracy:0.994937539100647
val on: imagenet_ai_0419_vqdm
ai accu: 0.6453333497047424
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:21, Accuracy:0.8226666450500488
val on: imagenet_ai_0424_wukong
ai accu: 0.9671666622161865
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:21, Accuracy:0.9835833311080933
Epoch:21,Accuracy:0.8769499659538269, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 13:11:47.586233 Epoch [022/030], Step [0001/2668], Total_loss: 0.0006
2024-09-02 13:12:49.994028 Epoch [022/030], Step [0200/2668], Total_loss: 0.0000
2024-09-02 13:14:01.885777 Epoch [022/030], Step [0400/2668], Total_loss: 0.0003
2024-09-02 13:15:07.586633 Epoch [022/030], Step [0600/2668], Total_loss: 0.0003
2024-09-02 13:16:09.785971 Epoch [022/030], Step [0800/2668], Total_loss: 0.0000
2024-09-02 13:17:11.485960 Epoch [022/030], Step [1000/2668], Total_loss: 0.0011
2024-09-02 13:18:14.433614 Epoch [022/030], Step [1200/2668], Total_loss: 0.0004
2024-09-02 13:19:16.086274 Epoch [022/030], Step [1400/2668], Total_loss: 0.0073
2024-09-02 13:20:17.785930 Epoch [022/030], Step [1600/2668], Total_loss: 0.0028
2024-09-02 13:21:21.785733 Epoch [022/030], Step [1800/2668], Total_loss: 0.0001
2024-09-02 13:22:22.785915 Epoch [022/030], Step [2000/2668], Total_loss: 0.0002
2024-09-02 13:23:29.984980 Epoch [022/030], Step [2200/2668], Total_loss: 0.0005
2024-09-02 13:24:35.585826 Epoch [022/030], Step [2400/2668], Total_loss: 0.0005
2024-09-02 13:25:38.584361 Epoch [022/030], Step [2600/2668], Total_loss: 0.0005
2024-09-02 13:25:58.774032 Epoch [022/030], Step [2668/2668], Total_loss: 0.0002
val on: imagenet_ai_0508_adm
ai accu: 0.5836666822433472
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:22, Accuracy:0.7917500138282776
val on: imagenet_ai_0419_biggan
ai accu: 0.4325000047683716
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:22, Accuracy:0.7162500023841858
val on: imagenet_glide
ai accu: 0.9261666536331177
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:22, Accuracy:0.9629999995231628
val on: imagenet_midjourney
ai accu: 0.6496666669845581
nature accu:1.0
val on:imagenet_midjourney, Epoch:22, Accuracy:0.824833333492279
val on: imagenet_ai_0419_sdv4
ai accu: 0.9906666278839111
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:22, Accuracy:0.9952499866485596
val on: imagenet_ai_0424_sdv5
ai accu: 0.9905000329017639
nature accu:0.999625027179718
val on:imagenet_ai_0424_sdv5, Epoch:22, Accuracy:0.995062530040741
val on: imagenet_ai_0419_vqdm
ai accu: 0.7264999747276306
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:22, Accuracy:0.8632500171661377
val on: imagenet_ai_0424_wukong
ai accu: 0.9749999642372131
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:22, Accuracy:0.987416684627533
Epoch:22,Accuracy:0.8962199687957764, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 13:35:10.485851 Epoch [023/030], Step [0001/2668], Total_loss: 0.0003
2024-09-02 13:36:12.885990 Epoch [023/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 13:37:19.286053 Epoch [023/030], Step [0400/2668], Total_loss: 0.0000
2024-09-02 13:38:26.586268 Epoch [023/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 13:39:28.785805 Epoch [023/030], Step [0800/2668], Total_loss: 0.0031
2024-09-02 13:40:30.486329 Epoch [023/030], Step [1000/2668], Total_loss: 0.0071
2024-09-02 13:41:32.485918 Epoch [023/030], Step [1200/2668], Total_loss: 0.0008
2024-09-02 13:42:34.694868 Epoch [023/030], Step [1400/2668], Total_loss: 0.0001
2024-09-02 13:43:39.485857 Epoch [023/030], Step [1600/2668], Total_loss: 0.0006
2024-09-02 13:44:43.785831 Epoch [023/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 13:45:47.086057 Epoch [023/030], Step [2000/2668], Total_loss: 0.0002
2024-09-02 13:46:50.086070 Epoch [023/030], Step [2200/2668], Total_loss: 0.0000
2024-09-02 13:47:53.985788 Epoch [023/030], Step [2400/2668], Total_loss: 0.0003
2024-09-02 13:48:58.885977 Epoch [023/030], Step [2600/2668], Total_loss: 0.0003
2024-09-02 13:49:20.746363 Epoch [023/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5768333077430725
nature accu:0.999833345413208
val on:imagenet_ai_0508_adm, Epoch:23, Accuracy:0.7883332967758179
val on: imagenet_ai_0419_biggan
ai accu: 0.5571666359901428
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:23, Accuracy:0.7785833477973938
val on: imagenet_glide
ai accu: 0.9111666679382324
nature accu:1.0
val on:imagenet_glide, Epoch:23, Accuracy:0.9555833339691162
val on: imagenet_midjourney
ai accu: 0.6159999966621399
nature accu:1.0
val on:imagenet_midjourney, Epoch:23, Accuracy:0.8079999685287476
val on: imagenet_ai_0419_sdv4
ai accu: 0.9914999604225159
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:23, Accuracy:0.9956666827201843
val on: imagenet_ai_0424_sdv5
ai accu: 0.9908750653266907
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:23, Accuracy:0.9953750371932983
val on: imagenet_ai_0419_vqdm
ai accu: 0.778333306312561
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:23, Accuracy:0.8890833258628845
val on: imagenet_ai_0424_wukong
ai accu: 0.9724999666213989
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:23, Accuracy:0.9861666560173035
Epoch:23,Accuracy:0.9034299850463867, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 13:58:30.208380 Epoch [024/030], Step [0001/2668], Total_loss: 0.0004
2024-09-02 13:59:31.886339 Epoch [024/030], Step [0200/2668], Total_loss: 0.0003
2024-09-02 14:00:33.185840 Epoch [024/030], Step [0400/2668], Total_loss: 0.0006
2024-09-02 14:01:34.188006 Epoch [024/030], Step [0600/2668], Total_loss: 0.0002
2024-09-02 14:02:35.685974 Epoch [024/030], Step [0800/2668], Total_loss: 0.0005
2024-09-02 14:03:36.985880 Epoch [024/030], Step [1000/2668], Total_loss: 0.0002
2024-09-02 14:04:38.286190 Epoch [024/030], Step [1200/2668], Total_loss: 0.0002
2024-09-02 14:05:39.732903 Epoch [024/030], Step [1400/2668], Total_loss: 0.0000
2024-09-02 14:06:41.732538 Epoch [024/030], Step [1600/2668], Total_loss: 0.0007
2024-09-02 14:07:42.985776 Epoch [024/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 14:08:44.185741 Epoch [024/030], Step [2000/2668], Total_loss: 0.0004
2024-09-02 14:09:45.885962 Epoch [024/030], Step [2200/2668], Total_loss: 0.0000
2024-09-02 14:10:46.687244 Epoch [024/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 14:11:48.333313 Epoch [024/030], Step [2600/2668], Total_loss: 0.0003
2024-09-02 14:12:08.474287 Epoch [024/030], Step [2668/2668], Total_loss: 0.0001
val on: imagenet_ai_0508_adm
ai accu: 0.5674999952316284
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:24, Accuracy:0.7837499976158142
val on: imagenet_ai_0419_biggan
ai accu: 0.4423333406448364
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:24, Accuracy:0.7210833430290222
val on: imagenet_glide
ai accu: 0.8945000171661377
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:24, Accuracy:0.9471666812896729
val on: imagenet_midjourney
ai accu: 0.5993333458900452
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:24, Accuracy:0.7995833158493042
val on: imagenet_ai_0419_sdv4
ai accu: 0.9913333058357239
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:24, Accuracy:0.9954999685287476
val on: imagenet_ai_0424_sdv5
ai accu: 0.9915000200271606
nature accu:1.0
val on:imagenet_ai_0424_sdv5, Epoch:24, Accuracy:0.9957500696182251
val on: imagenet_ai_0419_vqdm
ai accu: 0.7073333263397217
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:24, Accuracy:0.8536666631698608
val on: imagenet_ai_0424_wukong
ai accu: 0.9794999957084656
nature accu:0.999833345413208
val on:imagenet_ai_0424_wukong, Epoch:24, Accuracy:0.9896666407585144
Epoch:24,Accuracy:0.8901699781417847, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 14:21:32.489969 Epoch [025/030], Step [0001/2668], Total_loss: 0.0000
2024-09-02 14:22:35.386058 Epoch [025/030], Step [0200/2668], Total_loss: 0.0002
2024-09-02 14:23:36.686292 Epoch [025/030], Step [0400/2668], Total_loss: 0.0003
2024-09-02 14:24:38.284936 Epoch [025/030], Step [0600/2668], Total_loss: 0.0006
2024-09-02 14:25:39.007726 Epoch [025/030], Step [0800/2668], Total_loss: 0.0006
2024-09-02 14:26:40.986072 Epoch [025/030], Step [1000/2668], Total_loss: 0.0072
2024-09-02 14:27:56.506702 Epoch [025/030], Step [1200/2668], Total_loss: 0.0001
2024-09-02 14:29:05.233424 Epoch [025/030], Step [1400/2668], Total_loss: 0.0002
2024-09-02 14:30:14.385778 Epoch [025/030], Step [1600/2668], Total_loss: 0.0004
2024-09-02 14:31:21.733676 Epoch [025/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 14:32:26.886015 Epoch [025/030], Step [2000/2668], Total_loss: 0.0006
2024-09-02 14:33:31.085778 Epoch [025/030], Step [2200/2668], Total_loss: 0.0000
2024-09-02 14:34:36.286076 Epoch [025/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 14:35:39.085766 Epoch [025/030], Step [2600/2668], Total_loss: 0.0000
2024-09-02 14:35:59.587663 Epoch [025/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.6076666712760925
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:25, Accuracy:0.8038333058357239
val on: imagenet_ai_0419_biggan
ai accu: 0.6351666450500488
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:25, Accuracy:0.8175833225250244
val on: imagenet_glide
ai accu: 0.9176666736602783
nature accu:1.0
val on:imagenet_glide, Epoch:25, Accuracy:0.9588333368301392
val on: imagenet_midjourney
ai accu: 0.625
nature accu:0.999833345413208
val on:imagenet_midjourney, Epoch:25, Accuracy:0.812416672706604
val on: imagenet_ai_0419_sdv4
ai accu: 0.9918333292007446
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:25, Accuracy:0.9957500100135803
val on: imagenet_ai_0424_sdv5
ai accu: 0.9908750653266907
nature accu:1.0
val on:imagenet_ai_0424_sdv5, Epoch:25, Accuracy:0.9954375624656677
val on: imagenet_ai_0419_vqdm
ai accu: 0.8090000152587891
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:25, Accuracy:0.9045000076293945
val on: imagenet_ai_0424_wukong
ai accu: 0.9836666584014893
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:25, Accuracy:0.9918333292007446
Epoch:25,Accuracy:0.9134399890899658, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 14:45:04.385873 Epoch [026/030], Step [0001/2668], Total_loss: 0.0000
2024-09-02 14:46:05.585866 Epoch [026/030], Step [0200/2668], Total_loss: 0.0001
2024-09-02 14:47:06.785863 Epoch [026/030], Step [0400/2668], Total_loss: 0.0006
2024-09-02 14:48:09.131158 Epoch [026/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 14:49:10.385968 Epoch [026/030], Step [0800/2668], Total_loss: 0.0000
2024-09-02 14:50:11.485878 Epoch [026/030], Step [1000/2668], Total_loss: 0.0002
2024-09-02 14:51:13.286051 Epoch [026/030], Step [1200/2668], Total_loss: 0.0000
2024-09-02 14:52:15.385826 Epoch [026/030], Step [1400/2668], Total_loss: 0.0003
2024-09-02 14:53:17.085952 Epoch [026/030], Step [1600/2668], Total_loss: 0.0004
2024-09-02 14:54:18.285914 Epoch [026/030], Step [1800/2668], Total_loss: 0.0001
2024-09-02 14:55:19.785960 Epoch [026/030], Step [2000/2668], Total_loss: 0.0003
2024-09-02 14:56:21.085894 Epoch [026/030], Step [2200/2668], Total_loss: 0.0002
2024-09-02 14:57:22.285989 Epoch [026/030], Step [2400/2668], Total_loss: 0.0005
2024-09-02 14:58:22.885754 Epoch [026/030], Step [2600/2668], Total_loss: 0.0002
2024-09-02 14:58:42.766307 Epoch [026/030], Step [2668/2668], Total_loss: 0.0062
val on: imagenet_ai_0508_adm
ai accu: 0.534500002861023
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:26, Accuracy:0.7672500014305115
val on: imagenet_ai_0419_biggan
ai accu: 0.42366665601730347
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:26, Accuracy:0.7118332982063293
val on: imagenet_glide
ai accu: 0.8996666669845581
nature accu:1.0
val on:imagenet_glide, Epoch:26, Accuracy:0.949833333492279
val on: imagenet_midjourney
ai accu: 0.5896666646003723
nature accu:1.0
val on:imagenet_midjourney, Epoch:26, Accuracy:0.7948333024978638
val on: imagenet_ai_0419_sdv4
ai accu: 0.9933333396911621
nature accu:0.9996666312217712
val on:imagenet_ai_0419_sdv4, Epoch:26, Accuracy:0.9965000152587891
val on: imagenet_ai_0424_sdv5
ai accu: 0.9916250705718994
nature accu:1.0
val on:imagenet_ai_0424_sdv5, Epoch:26, Accuracy:0.9958125352859497
val on: imagenet_ai_0419_vqdm
ai accu: 0.6631666421890259
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:26, Accuracy:0.8315833210945129
val on: imagenet_ai_0424_wukong
ai accu: 0.9818333387374878
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:26, Accuracy:0.9909166693687439
Epoch:26,Accuracy:0.8844599723815918, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 15:07:43.585890 Epoch [027/030], Step [0001/2668], Total_loss: 0.0000
2024-09-02 15:08:43.486131 Epoch [027/030], Step [0200/2668], Total_loss: 0.0006
2024-09-02 15:09:44.186196 Epoch [027/030], Step [0400/2668], Total_loss: 0.0002
2024-09-02 15:10:44.686012 Epoch [027/030], Step [0600/2668], Total_loss: 0.0002
2024-09-02 15:11:45.208846 Epoch [027/030], Step [0800/2668], Total_loss: 0.0005
2024-09-02 15:12:45.685786 Epoch [027/030], Step [1000/2668], Total_loss: 0.0042
2024-09-02 15:13:46.687552 Epoch [027/030], Step [1200/2668], Total_loss: 0.0004
2024-09-02 15:14:46.886270 Epoch [027/030], Step [1400/2668], Total_loss: 0.0007
2024-09-02 15:15:47.785826 Epoch [027/030], Step [1600/2668], Total_loss: 0.0004
2024-09-02 15:16:47.886114 Epoch [027/030], Step [1800/2668], Total_loss: 0.0007
2024-09-02 15:17:48.986266 Epoch [027/030], Step [2000/2668], Total_loss: 0.0000
2024-09-02 15:18:48.886843 Epoch [027/030], Step [2200/2668], Total_loss: 0.0005
2024-09-02 15:19:49.286100 Epoch [027/030], Step [2400/2668], Total_loss: 0.0201
2024-09-02 15:20:50.485997 Epoch [027/030], Step [2600/2668], Total_loss: 0.0000
2024-09-02 15:21:10.192970 Epoch [027/030], Step [2668/2668], Total_loss: 0.0008
val on: imagenet_ai_0508_adm
ai accu: 0.5820000171661377
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:27, Accuracy:0.7910000085830688
val on: imagenet_ai_0419_biggan
ai accu: 0.5879999995231628
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:27, Accuracy:0.793999969959259
val on: imagenet_glide
ai accu: 0.9116666316986084
nature accu:1.0
val on:imagenet_glide, Epoch:27, Accuracy:0.9558333158493042
val on: imagenet_midjourney
ai accu: 0.5871666669845581
nature accu:0.9996666312217712
val on:imagenet_midjourney, Epoch:27, Accuracy:0.7934166789054871
val on: imagenet_ai_0419_sdv4
ai accu: 0.9928333163261414
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:27, Accuracy:0.9963333010673523
val on: imagenet_ai_0424_sdv5
ai accu: 0.9926250576972961
nature accu:1.0
val on:imagenet_ai_0424_sdv5, Epoch:27, Accuracy:0.9963125586509705
val on: imagenet_ai_0419_vqdm
ai accu: 0.8019999861717224
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:27, Accuracy:0.9009999632835388
val on: imagenet_ai_0424_wukong
ai accu: 0.9819999933242798
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:27, Accuracy:0.9909999966621399
Epoch:27,Accuracy:0.9061200022697449, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 15:30:10.786024 Epoch [028/030], Step [0001/2668], Total_loss: 0.0000
2024-09-02 15:31:10.785820 Epoch [028/030], Step [0200/2668], Total_loss: 0.0002
2024-09-02 15:32:11.786051 Epoch [028/030], Step [0400/2668], Total_loss: 0.0000
2024-09-02 15:33:12.885798 Epoch [028/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 15:34:13.786187 Epoch [028/030], Step [0800/2668], Total_loss: 0.0002
2024-09-02 15:35:13.885979 Epoch [028/030], Step [1000/2668], Total_loss: 0.0004
2024-09-02 15:36:14.486085 Epoch [028/030], Step [1200/2668], Total_loss: 0.0006
2024-09-02 15:37:15.185883 Epoch [028/030], Step [1400/2668], Total_loss: 0.0000
2024-09-02 15:38:16.686457 Epoch [028/030], Step [1600/2668], Total_loss: 0.0004
2024-09-02 15:39:16.685970 Epoch [028/030], Step [1800/2668], Total_loss: 0.0000
2024-09-02 15:40:17.286019 Epoch [028/030], Step [2000/2668], Total_loss: 0.0003
2024-09-02 15:41:17.787036 Epoch [028/030], Step [2200/2668], Total_loss: 0.0001
2024-09-02 15:42:18.986240 Epoch [028/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 15:43:19.485777 Epoch [028/030], Step [2600/2668], Total_loss: 0.0000
2024-09-02 15:43:39.295528 Epoch [028/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.590666651725769
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:28, Accuracy:0.7953333258628845
val on: imagenet_ai_0419_biggan
ai accu: 0.6211666464805603
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:28, Accuracy:0.8105833530426025
val on: imagenet_glide
ai accu: 0.9331666827201843
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:28, Accuracy:0.9664999842643738
val on: imagenet_midjourney
ai accu: 0.6430000066757202
nature accu:0.9996666312217712
val on:imagenet_midjourney, Epoch:28, Accuracy:0.8213333487510681
val on: imagenet_ai_0419_sdv4
ai accu: 0.9943333268165588
nature accu:1.0
val on:imagenet_ai_0419_sdv4, Epoch:28, Accuracy:0.997166633605957
val on: imagenet_ai_0424_sdv5
ai accu: 0.9935000538825989
nature accu:1.0
val on:imagenet_ai_0424_sdv5, Epoch:28, Accuracy:0.9967500567436218
val on: imagenet_ai_0419_vqdm
ai accu: 0.7906666398048401
nature accu:0.999833345413208
val on:imagenet_ai_0419_vqdm, Epoch:28, Accuracy:0.8952499628067017
val on: imagenet_ai_0424_wukong
ai accu: 0.984333336353302
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:28, Accuracy:0.9921666383743286
Epoch:28,Accuracy:0.912880003452301, bestEpoch:12, bestAccu:0.937999963760376
2024-09-02 15:52:38.713065 Epoch [029/030], Step [0001/2668], Total_loss: 0.0003
2024-09-02 15:53:39.485967 Epoch [029/030], Step [0200/2668], Total_loss: 0.0004
2024-09-02 15:54:40.386011 Epoch [029/030], Step [0400/2668], Total_loss: 0.0000
2024-09-02 15:55:40.985974 Epoch [029/030], Step [0600/2668], Total_loss: 0.0001
2024-09-02 15:56:41.786014 Epoch [029/030], Step [0800/2668], Total_loss: 0.0002
2024-09-02 15:57:42.585813 Epoch [029/030], Step [1000/2668], Total_loss: 0.0005
2024-09-02 15:58:42.785815 Epoch [029/030], Step [1200/2668], Total_loss: 0.0000
2024-09-02 15:59:43.385843 Epoch [029/030], Step [1400/2668], Total_loss: 0.0004
2024-09-02 16:00:44.185949 Epoch [029/030], Step [1600/2668], Total_loss: 0.0002
2024-09-02 16:01:44.886114 Epoch [029/030], Step [1800/2668], Total_loss: 0.0002
2024-09-02 16:02:45.485791 Epoch [029/030], Step [2000/2668], Total_loss: 0.0001
2024-09-02 16:03:45.985839 Epoch [029/030], Step [2200/2668], Total_loss: 0.0012
2024-09-02 16:04:46.485901 Epoch [029/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 16:05:46.985959 Epoch [029/030], Step [2600/2668], Total_loss: 0.0000
2024-09-02 16:06:06.793661 Epoch [029/030], Step [2668/2668], Total_loss: 0.0000
val on: imagenet_ai_0508_adm
ai accu: 0.5759999752044678
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:29, Accuracy:0.7879999876022339
val on: imagenet_ai_0419_biggan
ai accu: 0.5516666769981384
nature accu:1.0
val on:imagenet_ai_0419_biggan, Epoch:29, Accuracy:0.7758333086967468
val on: imagenet_glide
ai accu: 0.9313333034515381
nature accu:0.999833345413208
val on:imagenet_glide, Epoch:29, Accuracy:0.965583324432373
val on: imagenet_midjourney
ai accu: 0.6549999713897705
nature accu:1.0
val on:imagenet_midjourney, Epoch:29, Accuracy:0.8274999856948853
val on: imagenet_ai_0419_sdv4
ai accu: 0.9941666722297668
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:29, Accuracy:0.996999979019165
val on: imagenet_ai_0424_sdv5
ai accu: 0.9930000305175781
nature accu:0.9998750686645508
val on:imagenet_ai_0424_sdv5, Epoch:29, Accuracy:0.9964375495910645
val on: imagenet_ai_0419_vqdm
ai accu: 0.7566666603088379
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:29, Accuracy:0.878333330154419
val on: imagenet_ai_0424_wukong
ai accu: 0.9803333282470703
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:29, Accuracy:0.9901666641235352
Epoch:29,Accuracy:0.9061200022697449, bestEpoch:12, bestAccu:0.937999963760376
# Epoch 30
2024-09-02 16:15:07.085961 Epoch [030/030], Step [0001/2668], Total_loss: 0.0007
2024-09-02 16:16:07.385753 Epoch [030/030], Step [0200/2668], Total_loss: 0.0005
2024-09-02 16:17:07.785785 Epoch [030/030], Step [0400/2668], Total_loss: 0.0000
2024-09-02 16:18:08.905426 Epoch [030/030], Step [0600/2668], Total_loss: 0.0000
2024-09-02 16:19:09.785979 Epoch [030/030], Step [0800/2668], Total_loss: 0.0002
2024-09-02 16:20:10.186018 Epoch [030/030], Step [1000/2668], Total_loss: 0.0003
2024-09-02 16:21:10.486009 Epoch [030/030], Step [1200/2668], Total_loss: 0.0002
2024-09-02 16:22:10.585934 Epoch [030/030], Step [1400/2668], Total_loss: 0.0000
2024-09-02 16:23:11.085770 Epoch [030/030], Step [1600/2668], Total_loss: 0.0002
2024-09-02 16:24:11.685875 Epoch [030/030], Step [1800/2668], Total_loss: 0.0002
2024-09-02 16:25:12.185779 Epoch [030/030], Step [2000/2668], Total_loss: 0.0001
2024-09-02 16:26:12.085845 Epoch [030/030], Step [2200/2668], Total_loss: 0.0000
2024-09-02 16:27:12.385817 Epoch [030/030], Step [2400/2668], Total_loss: 0.0000
2024-09-02 16:28:12.485869 Epoch [030/030], Step [2600/2668], Total_loss: 0.0002
2024-09-02 16:28:32.145913 Epoch [030/030], Step [2668/2668], Total_loss: 0.0000
## adm
val on: imagenet_ai_0508_adm
ai accu: 0.5895000100135803
nature accu:1.0
val on:imagenet_ai_0508_adm, Epoch:30, Accuracy:0.7947499752044678
## biggan
val on: imagenet_ai_0419_biggan
ai accu: 0.559499979019165
nature accu:0.999833345413208
val on:imagenet_ai_0419_biggan, Epoch:30, Accuracy:0.7796666622161865
## glide
val on: imagenet_glide
ai accu: 0.9326666593551636
nature accu:1.0
val on:imagenet_glide, Epoch:30, Accuracy:0.9663333296775818
## midjourney
val on: imagenet_midjourney
ai accu: 0.6536666750907898
nature accu:1.0
val on:imagenet_midjourney, Epoch:30, Accuracy:0.8268333077430725
## sdv4
val on: imagenet_ai_0419_sdv4
ai accu: 0.9944999814033508
nature accu:0.999833345413208
val on:imagenet_ai_0419_sdv4, Epoch:30, Accuracy:0.997166633605957
## sdv5
val on: imagenet_ai_0424_sdv5
ai accu: 0.9931250214576721
nature accu:0.999750018119812
val on:imagenet_ai_0424_sdv5, Epoch:30, Accuracy:0.9964375495910645
## vqdm
val on: imagenet_ai_0419_vqdm
ai accu: 0.7506666779518127
nature accu:1.0
val on:imagenet_ai_0419_vqdm, Epoch:30, Accuracy:0.875333309173584
## wukong
val on: imagenet_ai_0424_wukong
ai accu: 0.9826666712760925
nature accu:1.0
val on:imagenet_ai_0424_wukong, Epoch:30, Accuracy:0.9913333058357239
## mean
Epoch:30,Accuracy:0.9071999788284302, bestEpoch:12, bestAccu:0.937999963760376
