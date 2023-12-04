from pyproj import Transformer
trans = Transformer.from_crs(2278, 4326, always_xy=True)
converted = trans.transform(3111223.07202555, 13856839.923629)
print(trans)
print(converted)