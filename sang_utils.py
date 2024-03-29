import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms

def get_celebA_loader(data_dir, batch_sizes, image_size):
    # put image data into data_loader
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])
    data_dir = 'resized_celebA'  # this path depends on your computer
    dset = datasets.ImageFolder(data_dir, transform)
    train_loader = torch.utils.data.DataLoader(dset, batch_size=batch_sizes, drop_last=True, shuffle=True)

    # confrimed input image size!
    temp = plt.imread(train_loader.dataset.imgs[0][0])
    if (temp.shape[0] != image_size) or (temp.shape[0] != image_size):
        raise ValueError('image size is not 64 x 64!')
    
    return train_loader


def get_cifar10_loader(batch_sizes, image_size):
    # put image data into data_loader
    train_loader = torch.utils.data.DataLoader(datasets.CIFAR10("../../data/mnist",
                                                                train=True,
                                                                download=True,
                                                                transform=transforms.Compose([
                                                                    transforms.Resize(image_size),
                                                                    transforms.ToTensor(),
                                                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                                                ])),
                                               batch_size=batch_sizes, drop_last=True, shuffle=True)

    # confrimed input image size!
    temp = plt.imread(train_loader.dataset.imgs[0][0])
    if (temp.shape[0] != image_size) or (temp.shape[0] != image_size):
        raise ValueError('image size is not 64 x 64!')

    return train_loader
