# Remove background to white on photo

Script to remove bg from image.

Put images in img folder
# Install
pip install transparent-background

edit Remover.py

## put under:

        `elif type == 'green':
            bg = np.stack([np.ones_like(pred)] * 3, axis=-1) * [120, 255, 155]
            img = img * pred[..., np.newaxis] + bg * (1 - pred[..., np.newaxis]`

This:

        elif type == 'white':
            bg = np.stack([np.ones_like(pred)] * 3, axis=-1) * [255, 255, 255]
            img = img * pred[..., np.newaxis] + bg * (1 - pred[..., np.newaxis])



python -m  pipreqs.pipreqs --encoding utf-8  . 