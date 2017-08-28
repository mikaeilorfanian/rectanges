class SubShape:
    
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def subtract_height(self, h):
        if self.height - h < 0:
            raise ValueError
        else:
            self.height -= h

            
class Shape:
    
    def __init__(self, sub_shapes=None):
        if sub_shapes is None:
            self.sub_shapes = list()
        else:
            self.sub_shapes = sub_shapes
        
    def add_sub_shape(self, s_s):
        self.sub_shapes.append(s_s)
            
    def subtract_min_height(self):
        min_height = self.min_height
        new_shape = Shape()
        all_new_shapes = [] # each time there's gap in the original shape
                            # all the shapes before the gap become a new Shape object
        
        for s_s in self.sub_shapes:
            s_s.subtract_height(min_height)
            
            # create new shape when there's a gap in the original shape
            if s_s.height == 0:
                # add new_shape only if it has sub shapes
                if new_shape.sub_shapes:
                    all_new_shapes.append(new_shape)
                new_shape = Shape()

            else:
                new_shape.add_sub_shape(s_s)
        
        # the last new_shape should be added to all_new_shapes
        if new_shape.sub_shapes:
            all_new_shapes.append(new_shape)
        
        return all_new_shapes

    @property
    def min_height(self):
        return min([s_s.height for s_s in self.sub_shapes])
    
    
def min_number_of_rectanges_to_cover_shape(shape):
    counter = 0
    shapes = [shape]
    
    while shapes:
        shape_to_cover = shapes.pop()
        new_shapes = shape_to_cover.subtract_min_height()
        counter += 1
        [shapes.append(new_shape) for new_shape in new_shapes if new_shape.sub_shapes]
        
    return counter
        
