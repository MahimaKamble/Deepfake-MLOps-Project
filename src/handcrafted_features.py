import numpy as np
from skimage.feature import local_binary_pattern, hog
from skimage.color import rgb2gray
from scipy.stats import skew, kurtosis

# Parameters
LBP_POINTS = 8
LBP_RADIUS = 1
HOG_PIXELS_PER_CELL = (8, 8)
HOG_CELLS_PER_BLOCK = (2, 2)

def extract_handcrafted_features(img):

    # Convert to grayscale
    gray = rgb2gray(img)

    # LBP Features
    lbp = local_binary_pattern(
        gray,
        LBP_POINTS,
        LBP_RADIUS,
        method="uniform"
    )

    lbp_hist, _ = np.histogram(
        lbp.ravel(),
        bins=np.arange(0, LBP_POINTS + 3),
        density=True
    )

    # HOG Features
    hog_features = hog(
        gray,
        pixels_per_cell=HOG_PIXELS_PER_CELL,
        cells_per_block=HOG_CELLS_PER_BLOCK,
        feature_vector=True
    )

    # Color Moments
    color_feats = []

    for i in range(img.shape[2]):

        channel = img[:, :, i].ravel()

        color_feats.extend([
            np.mean(channel),
            np.std(channel),
            skew(channel),
            kurtosis(channel)
        ])

    # Combine handcrafted features
    features = np.concatenate([
        lbp_hist,
        hog_features,
        color_feats
    ])

    return features