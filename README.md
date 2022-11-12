# Open3D_Test
## �T�v
Open3D�̓���e�X�g/�d�l�m�F

## �Q�l�T�C�g
[Open3D�����h�L�������g](http://www.open3d.org/docs/release/getting_started.html)

## �C���X�g�[��/����m�F
- Python�̃o�[�W������3.7~3.10�ŃT�|�[�g
```shell
$ pip install open3d
```

- �o�[�W�������m�F����
```py
import open3d as o3d

print(o3d.__version__)
```

- API���N������(Python����)
```py
import open3d as o3d

mesh = o3d.geometry.TriangleMesh.create_sphere()
mesh.compute_vertex_normals()
o3d.visualization.draw(mesh, raw_mode=True)
```

- CLI����N������
```shell
$ open3d example visualization/draw
```