import argparse

from PIL import Image

from checksum import hashCal

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pi', '--pathin', default="fakepathin.jpg", type=str, help='Duong dan anh input')
    parser.add_argument('-po', '--pathout', default="rotated.jpg", type=str, help='Duong dan anh output')
    parser.add_argument('-ag', '--angle', default=69, type=int, help='Goc xoay anh')
    args = parser.parse_args()
    image = Image.open(args.pathin)

    rotated_image = image.rotate(args.angle, expand=True)

    rotated_image.save(args.pathout)
    print(f"Đã xoay ảnh một góc {args.angle} độ!\nMD5 checksum: {hashCal(args.pathout)}")
