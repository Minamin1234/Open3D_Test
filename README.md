# Open3D_Test
## 概要
Open3Dの動作テスト/仕様確認

## 参考サイト
[Open3D公式ドキュメント](http://www.open3d.org/docs/release/getting_started.html)

## インストール/動作確認
- Pythonのバージョンは3.7~3.10でサポート
```shell
$ pip install open3d
```

- バージョンを確認する
```py
import open3d as o3d

print(o3d.__version__)
```

- APIを起動する(Pythonから)
```py
import open3d as o3d

mesh = o3d.geometry.TriangleMesh.create_sphere()
mesh.compute_vertex_normals()
o3d.visualization.draw(mesh, raw_mode=True)
```

- CLIから起動する
```shell
$ open3d example visualization/draw
```