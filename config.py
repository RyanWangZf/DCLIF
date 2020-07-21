# -*- coding: utf-8 -*-

class DefaultConfig(object):
    # model name
    model = "small"

    # data name
    data_name = "cifar10"

    # training log output dir
    result_dir = "./out"

    # random seed
    seed = 2020

    # execute on cuda devices or not
    use_gpu = True

    # hyperparameters
    batch_size = 128
    num_epoch = 50
    lr = 1e-3
    weight_decay = 0.0
    
    # if >0, then label noise is imposed on training data
    noise_ratio = 0.0

    # curriculum learning for DCLIF
    curriculum_size = 10000

    # log name
    print_opt = "DEF"

    # curriculum learning for self-paced learning
    spl = "spl"

    def parse(self, kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                raise Exception('opt has No key: {}'.format(k))
            setattr(self, k, v)

        print('*************************************************')
        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                print("{} => {}".format(k, getattr(self, k)))

        print('*************************************************')


opt = DefaultConfig()
