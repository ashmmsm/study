rom PIL import Image, ImageFilter

with Image.open('maus.jpg') as picture:
    print('Размер', picture.size)
    print('Формат', picture.format)
    print('Тип', picture.mode)
    picture.show()

    gray = picture.convert('L')
    gray.save('black_maus.jpg')
    
    blur = picture.filter(ImageFilter.BLUR)
    blur.save('blur_maus.jpg')

    rotate = picture.transpose(Image.FLIP_LEFT_RIGHT)
    rotate.save('rotate_maus.jpg')

a = int(input('Введите число'))
b = int(input('Введите число'))

try:
    print('Разность чисел:', a/b)
except:
    print('На ноль делить нельзя')

print()
