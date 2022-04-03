Python 定位根目录

```python
import os
import sys
server_root = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
sys.path.insert(0, os.path.join(server_root))
```