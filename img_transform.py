import argparse

from PIL import Image

from checksum import hashCal


def crop(pathin, pathout, cw, ch):
    img = Image.open(pathin)

    crop_width = cw
    crop_height = ch

    img_width, img_height = img.size

    left = (img_width - crop_width) // 2
    top = (img_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height

    cropped_img = img.crop((left, top, right, bottom))

    cropped_img.save(pathout)

    print(f"Đã crop ảnh về kích thước {cw}x{ch}!\nMD5 checksum: {hashCal(pathout)}")


def resize(pathin, pathout, rw, rh):
    img = Image.open(pathin)
    resized_img = img.resize((rw, rh))
    resized_img.save(pathout)
    print(f"Đã resize ảnh về kích thước {rw}x{rh}!\nMD5 checksum: {hashCal(pathout)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pi', '--pathin', default="fakepathin.jpg", type=str, help='Duong dan anh input')
    parser.add_argument('-po', '--pathout', default="rotated.jpg", type=str, help='Duong dan anh output')
    parser.add_argument('-a', '--action', default="nothing", type=str,
                        help='Thao tac thuc hien: (c) - crop, (r) - resize')
    parser.add_argument('-cw', '--cropwidth', default=1890, type=int, help='Chieu ngang muon cat anh')
    parser.add_argument('-ch', '--cropheight', default=1890, type=int, help='Chieu cao muon cat anh')
    parser.add_argument('-rw', '--resizewidth', default=1890, type=int, help='Chieu ngang muon thu phong')
    parser.add_argument('-rh', '--resizeheight', default=1890, type=int, help='Chieu cao muon thu phong')
    args = parser.parse_args()
    if args.action == "crop" or args.action.upper() == "C":
        crop(args.pathin, args.pathout, args.cropwidth, args.cropheight)
    elif args.action == "resize" or args.action.upper() == "R":
        resize(args.pathin, args.pathout, args.resizewidth, args.resizeheight)
    else:
        print("Death is the wind, always by my side...")
