import pytest

from rectangles import min_number_of_rectanges_to_cover_shape, Shape, SubShape


class TestSubShape:
    
    def test_sub_shape_subtract_height(self):
        s_s = SubShape('a', 10)
        s_s.subtract_height(5)
        assert s_s.height == 5


    def test_subtract_height_throws_error_when_height_goes_negative(self):
        s_s = SubShape('a', 10)
        s_s.subtract_height(10)

        with pytest.raises(ValueError):
            s_s.subtract_height(1)
    

class TestShape:
    
    def test_add_sub_shape_to_shape(self):
        s = Shape()
        assert len(s.sub_shapes) == 0

        s_s = SubShape('a', 2)
        s.add_sub_shape(s_s)
        assert len(s.sub_shapes) == 1


    def test_find_sub_shape_with_lowest_height(self):
        s = Shape()
        s_s = SubShape('a', 3)
        s.add_sub_shape(s_s)
        assert s.min_height == 3

        s_s = SubShape('b', 3)
        s.add_sub_shape(s_s)
        assert s.min_height == 3

        s_s = SubShape('c', 2)
        s.add_sub_shape(s_s)
        assert s.min_height == 2

        s_s = SubShape('d', 4)
        s.add_sub_shape(s_s)
        assert s.min_height == 2

        s_s = SubShape('e', 2)
        s.add_sub_shape(s_s)
        assert s.min_height == 2

        s_s = SubShape('f', 1)
        s.add_sub_shape(s_s)
        assert s.min_height == 1

        s_s = SubShape('g', 5)
        s.add_sub_shape(s_s)
        assert s.min_height == 1
    

class TestShapeSubtractMinimumHeightMethod:
    
    def test_shape_has_only_one_sub_shape(self):
        s = Shape()
        s_s = SubShape('b', 3)
        s.add_sub_shape(s_s)
        
        s.subtract_min_height()
        assert s.sub_shapes[0].height == 0
        
    def test_shape_has_multiple_sub_shapes_with_same_height(self):
        s = Shape()
        s_s = SubShape('b', 3)
        s.add_sub_shape(s_s)
        s_s = SubShape('a', 3)
        s.add_sub_shape(s_s)
        
        s.subtract_min_height()
        assert s.sub_shapes[0].height == 0
        assert s.sub_shapes[1].height == 0
        
    def test_shape_has_multiple_sub_shapes_with_different_heights(self):
        s = Shape()
        s_s = SubShape('b', 3)
        s.add_sub_shape(s_s)
        s_s = SubShape('a', 3)
        s.add_sub_shape(s_s)
        s_s = SubShape('c', 2)
        s.add_sub_shape(s_s)
        s_s = SubShape('d', 1)
        s.add_sub_shape(s_s)
        s_s = SubShape('e', 4)
        s.add_sub_shape(s_s)
        
        s.subtract_min_height()
        assert s.sub_shapes[0].height == 2
        assert s.sub_shapes[1].height == 2
        assert s.sub_shapes[2].height == 1
        assert s.sub_shapes[3].height == 0
        assert s.sub_shapes[4].height == 3
        
    def test_method_call_results_in_creation_of_two_new_shapes(self):
        s = Shape()
        s_s = SubShape('c', 2)
        s.add_sub_shape(s_s)
        s_s = SubShape('d', 1)
        s.add_sub_shape(s_s)
        s_s = SubShape('e', 4)
        s.add_sub_shape(s_s)
        
        new_shapes = s.subtract_min_height()
        assert len(new_shapes) == 2
        
        assert len(new_shapes[0].sub_shapes) == 1
        assert len(new_shapes[1].sub_shapes) == 1
        
        assert new_shapes[0].sub_shapes[0].height == 1
        assert new_shapes[1].sub_shapes[0].height == 3
        
    def test_method_call_on_a_shape_with_wider_range_of_shapes_and_heights(self):
        a2 = SubShape('a', 2)
        b1 = SubShape('b', 1)
        c2 = SubShape('c', 2)
        d3 = SubShape('d', 3)
        e1 = SubShape('e', 1)
        f4 = SubShape('f', 4)
        g5 = SubShape('g', 5)
        h1 = SubShape('h', 1)
        i1 = SubShape('i', 1)
        j1 = SubShape('j', 1)
        k2 = SubShape('k', 2)
        l7 = SubShape('l', 7)
        s = Shape(
            [a2, b1, c2, d3, e1, f4, g5, h1, i1, j1, k2, l7]
        )
        
        new_shapes = s.subtract_min_height()
        assert len(new_shapes) == 4
        
        assert len(new_shapes[0].sub_shapes) == 1
        assert len(new_shapes[1].sub_shapes) == 2
        assert len(new_shapes[2].sub_shapes) == 2
        assert len(new_shapes[3].sub_shapes) == 2
        
        more_new_shapes = new_shapes[0].subtract_min_height()
        assert not more_new_shapes
        
        more_new_shapes = new_shapes[1].subtract_min_height()
        assert len(more_new_shapes) == 1
        
        more_new_shapes = new_shapes[2].subtract_min_height()
        assert len(more_new_shapes) == 1
        
        more_new_shapes = new_shapes[3].subtract_min_height()
        assert len(more_new_shapes) == 1
        

class TestMinNumbeOfRectangesToCoverShapeFunction:
    
    def test_shape_with_one_sub_shape(self):
        s = Shape()
        s_s = SubShape('b', 3)
        s.add_sub_shape(s_s)
        assert min_number_of_rectanges_to_cover_shape(s) == 1
        
    def test_shape_with_two_sub_shapes_of_different_height(self):
        s = Shape()
        s_s1 = SubShape('a', 2)
        s_s2 = SubShape('b', 3)
        s.add_sub_shape(s_s1)
        s.add_sub_shape(s_s2)
        
        assert min_number_of_rectanges_to_cover_shape(s) == 2
    
    def test_function_returns_correct_number_for_a_shape_with_larger_number_of_sub_shapes_and_heights(self):
        a2 = SubShape('a', 2)
        b1 = SubShape('b', 1)
        c2 = SubShape('c', 2)
        d3 = SubShape('d', 3)
        e1 = SubShape('e', 1)
        f4 = SubShape('f', 4)
        g5 = SubShape('g', 5)
        h1 = SubShape('h', 1)
        i1 = SubShape('i', 1)
        j1 = SubShape('j', 1)
        k2 = SubShape('k', 2)
        l7 = SubShape('l', 7)
        s = Shape(
            [a2, b1, c2, d3, e1, f4, g5, h1, i1, j1, k2, l7]
        )
        
        assert min_number_of_rectanges_to_cover_shape(s) == 8
        
        