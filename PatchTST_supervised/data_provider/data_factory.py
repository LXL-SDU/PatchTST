import pandas as pd
import os
from data_provider.data_loader import Dataset_ETT_hour, Dataset_ETT_minute, Dataset_Custom, Dataset_Pred
from torch.utils.data import DataLoader

data_dict = {
    'ETTh1': Dataset_ETT_hour,
    'ETTh2': Dataset_ETT_hour,
    'ETTm1': Dataset_ETT_minute,
    'ETTm2': Dataset_ETT_minute,
    'custom': Dataset_Custom,
}


def data_provider(args, flag):
    Data = data_dict[args.data]
    timeenc = 0 if args.embed != 'timeF' else 1

    if flag == 'test':
        shuffle_flag = False
        drop_last = True
        batch_size = args.batch_size
        freq = args.freq
    elif flag == 'pred':
        shuffle_flag = False
        drop_last = False
        batch_size = 1
        freq = args.freq
        Data = Dataset_Pred
    else:
        shuffle_flag = True
        drop_last = True
        batch_size = args.batch_size
        freq = args.freq

    data_set = Data(
        root_path=args.root_path,
        data_path=args.data_path,
        flag=flag,
        size=[args.seq_len, args.label_len, args.pred_len],
        features=args.features,
        target=args.target,
        timeenc=timeenc,
        freq=freq
    )
    print(flag, len(data_set))
    if hasattr(data_set, 'scaler'):
        mean = data_set.scaler.mean_
        var = data_set.scaler.var_
        mean_df = pd.DataFrame(mean.reshape(1, -1))
        var_df = pd.DataFrame(var.reshape(1, -1))
        mean_path = os.path.join(args.root_path, f'{flag}_mean.csv')
        var_path = os.path.join(args.root_path, f'{flag}_var.csv')
        mean_df.to_csv(mean_path, index=False)
        var_df.to_csv(var_path, index=False)
        print(f"Mean saved to {mean_path}")
        print(f"Variance saved to {var_path}")

        # 保存标准化后的数据
    if hasattr(data_set, 'data_x'):
        scaled_data_df = pd.DataFrame(data_set.data_x)
        scaled_data_path = os.path.join(args.root_path, f'{flag}_scaled_data.csv')
        scaled_data_df.to_csv(scaled_data_path, index=False)
        print(f"Scaled data saved to {scaled_data_path}")
    data_loader = DataLoader(
        data_set,
        batch_size=batch_size,
        shuffle=shuffle_flag,
        num_workers=args.num_workers,
        drop_last=drop_last)
    return data_set, data_loader
