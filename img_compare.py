import argparse

import numpy as np
from PIL import Image, ImageChops

from checksum import hashCal


def export_diff(img1_path, img2_path, output_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    diff_img = Image.new("RGB", img1.size, color=(0, 0, 0))

    pixels1 = img1.load()
    pixels2 = img2.load()
    pixels_diff = diff_img.load()

    width, height = img1.size

    for x in range(width):
        for y in range(height):
            if pixels1[x, y] != pixels2[x, y]:
                pixels_diff[x, y] = (255, 0, 0)
            else:
                pixels_diff[x, y] = (255, 255, 255)

    diff_img.save(output_path, "JPEG")
    hash_value = hashCal(output_path)
    print(f"Anh so sanh duoc luu tai: {output_path}\nMD5 checksum: {hash_value}")


def count_diff(img1_path, img2_path):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    diff = ImageChops.difference(img1, img2)

    diff_np = np.array(diff)

    num_diff_pixels = np.sum(np.any(diff_np != 0, axis=-1))
    print(f"Hai anh khac nhau {num_diff_pixels} pixel.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p1', '--path1', default="fakepath1.jpg", type=str, help='Duong dan anh 1')
    parser.add_argument('-p2', '--path2', default="fakepath2.jpg", type=str, help='Duong dan anh 2')
    parser.add_argument('-po', '--pathout', default="fakepathout.jpg", type=str, help='Duong dan anh 2')
    parser.add_argument('-a', '--action', default="nothing", type=str, help='Duong dan anh 2')
    args = parser.parse_args()

    if args.action == "export" or args.action.upper() == "E":
        export_diff(args.path1, args.path2, args.pathout)
    elif args.action == "count" or args.action.upper() == "C":
        count_diff(args.path1, args.path2)
    else:
        print("Success is not final, failure is not fatal: it is the courage to continue that counts. :D")
