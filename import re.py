import re

p = "Putin/huesosPutin/huesosPutin/huesosPutin/huesosPutin/huesosPutin/huesosPutin/huesosPutin/huesos"
result = re.sub("h", "P", p)
print(result)