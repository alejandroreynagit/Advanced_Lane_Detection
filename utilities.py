import os
from datetime import datetime
import cv2
import matplotlib.pyplot as plt

def get_time():
    '''Obtain current time
    '''
    
    ts = str(datetime.now()).split(' ')
    date = ''.join(ts[0].split('-'))
    hour = ''.join(ts[1].split(':'))
    date_s = date + '_' + hour
    return date_s

def hsv_display(img, output_dir):
    '''Extract HSV channels
    '''
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    H = hsv[:,:,0]
    S = hsv[:,:,1]
    V = hsv[:,:,2]

    fig, (ax1, ax2,ax3,ax4) = plt.subplots(1, 4, figsize=(20, 9))
    fig.tight_layout()
    ax1.imshow(H,cmap='gray')
    ax1.set_title('H', fontsize=30)
    ax2.imshow(S, cmap='gray')
    ax2.set_title('S', fontsize=30)
    ax3.imshow(V, cmap='gray')
    ax3.set_title('V', fontsize=30)
    ax4.imshow(hsv, cmap='gray')
    ax4.set_title('HSV', fontsize=30)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    plt.show()
    
    fig.savefig(os.path.join(output_dir,'Thresh_HSV.png'), transparent=True)
    
    return H, S, V, hsv

def hls_display(img, output_dir):
    '''Extract HLS channels
    '''
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    H = hls[:,:,0]
    L = hls[:,:,1]
    S = hls[:,:,2]

    fig, (ax1, ax2,ax3,ax4) = plt.subplots(1, 4, figsize=(20, 9))
    fig.tight_layout()
    ax1.imshow(H,cmap='gray')
    ax1.set_title('H', fontsize=30)
    ax2.imshow(L, cmap='gray')
    ax2.set_title('L', fontsize=30)
    ax3.imshow(S, cmap='gray')
    ax3.set_title('S', fontsize=30)
    ax4.imshow(hls, cmap='gray')
    ax4.set_title('HLS', fontsize=30)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    
    fig.savefig(os.path.join(output_dir,'Thresh_HLS.png'), transparent=True)
    
    return H, L, S, hls

def rgb_display(img, output_dir):
    '''Extract RGB channels
    '''
    
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

    fig = plt.figure(figsize=(20, 9))
    fig.tight_layout()
    plt.subplot(141)
    plt.imshow(R,cmap='gray')
    plt.title('R', fontsize=30)
    plt.subplot(142)
    plt.imshow(G, cmap='gray')
    plt.title('G', fontsize=30)
    plt.subplot(143)
    plt.imshow(B, cmap='gray')
    plt.title('B', fontsize=30)
    plt.subplot(144)
    plt.imshow(img, cmap='gray')
    plt.title('RGB', fontsize=30)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    
    fig.savefig(os.path.join(output_dir,'Thresh_RGB.png'), transparent=True)
    
    return R, G, B, img

def lab_display(img, output_dir):
    '''Extract LAB channels
    '''
    
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l = lab[:,:,0]
    a = lab[:,:,1]
    b = lab[:,:,2]

    fig, (ax1, ax2,ax3,ax4) = plt.subplots(1, 4, figsize=(20, 9))
    fig.tight_layout()
    ax1.imshow(l,cmap='gray')
    ax1.set_title('L', fontsize=30)
    ax2.imshow(a, cmap='gray')
    ax2.set_title('A', fontsize=30)
    ax3.imshow(b, cmap='gray')
    ax3.set_title('B', fontsize=30)
    ax4.imshow(lab, cmap='gray')
    ax4.set_title('LAB', fontsize=30)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    
    fig.savefig(os.path.join(output_dir,'Thresh_LAB.png'), transparent=True)
    
    return l, a, b, lab