import bpy

def get_data_bone(name):
    return bpy.context.active_object.data.bones.get(name)
    
    
def set_bone_layer(databone, layer_idx, multi=False):
    if databone == None:      
        return
        
    databone.layers[layer_idx] = True
    if multi:
        return
        
    for i, lay in enumerate(databone.layers):
        if i != layer_idx:
            databone.layers[i] = False