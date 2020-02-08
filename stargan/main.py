import os
import sys
import argparse
from solver import Solver
from data_loader import get_loader
from torch.backends import cudnn


def str2bool(v):
    return v.lower() in ('true')

def main():
    # For fast training.
    cudnn.benchmark = True

    # Create directories if not exist.
    #if not os.path.exists(config.log_dir):
    #    os.makedirs(config.log_dir)
    #if not os.path.exists(config.model_save_dir):
    #    os.makedirs(config.model_save_dir)
    #if not os.path.exists(config.sample_dir):
    #    os.makedirs(config.sample_dir)
    #if not os.path.exists(config.result_dir):
    #    os.makedirs(config.result_dir)

    # Data loader.
    celeba_loader = None
    rafd_loader = None
    if sys.argv[1] in ['CelebA', 'Both']:
        selected_attrs = sys.argv[2]
        celeba_loader = get_loader(image_dir = '.', attr_path = 'newAttr.txt', selected_attrs = selected_attrs, mode = 'test')
    if sys.argv[1] in ['RaFD', 'Both']:
        rafd_loader = get_loader('RaFD', None, None,
                                 256, 128, 16,
                                 'RaFD', 'test', 1)
    

    # Solver for training and testing StarGAN.
    solver = Solver(celeba_loader, rafd_loader, dataset = sys.argv[1], selected_attrs = sys.argv[2])

    solver.test()


if __name__ == '__main__':
    main()