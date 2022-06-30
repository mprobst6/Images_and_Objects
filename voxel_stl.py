from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.primitives import generateMaterials

if __name__ == "__main__":
    sponge = [
        [
            [1,1,1],
            [1,0,0],
            [1,0,0]
        ],
        [
            [1,1,1],
            [1,0,0],
            [1,0,0]
        ],
        [
            [1,1,1],
            [1,0,0],
            [1,0,0]
        ],
        [
            [1,1,1],
            [1,0,0],
            [1,0,0]
        ],
        [
            [1,1,1],
            [1,0,0],
            [1,0,0]
        ]
    ]
    model = VoxelModel(sponge,generateMaterials(4))
    mesh = Mesh.fromVoxelModel(model)
    mesh.export('mesh.stl')

