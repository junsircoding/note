class Screen(object):
    # def __init__(self, width, height, resolution):
    #     self.__width = width
    #     self.__height = height
    #     self.resolution = self.__width * self.__height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError('worng')
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError('worng')
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
