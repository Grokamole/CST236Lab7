"""
Joseph Miller
CST236 - Lab 2
Test for source.source1.shape_checker
"""
import sys
from unittest import TestCase
from source.source1.shape_checker import get_triangle_type, get_square_type
from source.source1.shape_checker import get_quadrilateral_type
from test.plugins.ReqTracer import requirements

class TestGetTriangleTypeValid(TestCase):
    '''
    This class tests get_triangle_type for valid cases.
    '''
    @requirements(['#0001', '#0002'])
    def test_triangle_equil_all_int(self):
        '''
        This tests for an equilateral triangle with integers.
        '''
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_triangle_equil_all_float(self):
        '''
        This tests for an equilateral triangle with floats.
        '''
        result = get_triangle_type(2.0, 2.0, 2.0)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_triangle_equil_tuple(self):
        '''
        This tests for an equilateral triangle with a tuple.
        '''
        result = get_triangle_type((3, 3, 3))
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_triangle_equil_list(self):
        '''
        This tests for an equilateral triangle with a list.
        '''
        result = get_triangle_type([4, 4, 4])
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001'])
    def test_triangle_equil_dict(self):
        '''
        This tests for an equilateral triangle with a dictionary.
        '''
        result = get_triangle_type({"a":5, "b":5, "c":5})
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_triangle_scal_all_int(self):
        '''
        This tests for a scalene triangle with integers.
        '''
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_triangle_scal_all_float(self):
        '''
        This tests for a scalene triangle with floats.
        '''
        result = get_triangle_type(3.0, 2.0, 1.0)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_triangle_scal_tuple(self):
        '''
        This tests for a scalene triangle with a tuple.
        '''
        result = get_triangle_type((3, 4, 5))
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_triangle_scal_list(self):
        '''
        This tests for a scalene triangle with a list.
        '''
        result = get_triangle_type([5, 6, 7])
        self.assertEqual(result, 'scalene')

    @requirements(['#0001'])
    def test_triangle_scal_dict(self):
        '''
        This tests for a scalene triangle with a dictionary.
        '''
        result = get_triangle_type({"a":8, "b":9, "c":10})
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_triangle_isos_all_int(self):
        '''
        This tests for an isosceles triangle with integers.
        '''
        result = get_triangle_type(2, 2, 3)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_triangle_isos_all_float(self):
        '''
        This tests for an isosceles triangle with floats.
        '''
        result = get_triangle_type(3.0, 3.0, 4.0)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_triangle_isos_tuple(self):
        '''
        This tests for an isosceles triangle with a tuple.
        '''
        result = get_triangle_type((1, 1, 10))
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_triangle_isos_list(self):
        '''
        This tests for an isosceles triangle with a list.
        '''
        result = get_triangle_type([4, 4, 5])
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_triangle_isos_dict(self):
        '''
        This tests for an isosceles triangle with a dictionary.
        '''
        result = get_triangle_type({"a":6, "b":6, "c":7})
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001'])
    def test_triangle_mix_use_types(self):
        '''
        This tests for a triangle using mixed integers and floats.
        '''
        result = get_triangle_type(2, 3.45678, 2)
        self.assertEqual(result, 'isosceles')

class TestGetTriangleTypeInvalid(TestCase):
    '''
    This class tests get_triangle_type for invalid cases.
    '''
    def test_triangle_mix_unuse_list(self):
        '''
        This tests for an invalid triangle with a list and other types.
        '''
        result = get_triangle_type([1, 1, 1], 3.45678, 2)
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_unuse_tuple(self):
        '''
        This tests for an invalid triangle with a tuple and other types.
        '''
        result = get_triangle_type((1, 1, 1), 3.45678, 2)
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_inc_tup_sml(self):
        '''
        This tests for an invalid triangle with less than three tuple elements.
        '''
        result = get_triangle_type((1, 1))
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_inc_tup_lrg(self):
        '''
        This tests for an invalid triangle with more than three tuple
        elements.
        '''
        result = get_triangle_type((1, 1, 1, 1))
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_inc_list_sm(self):
        '''
        This tests for an invalid triangle with less than three list elements.
        '''
        result = get_triangle_type([1, 1])
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_inc_list_lg(self):
        '''
        This tests for an invalid triangle with more than three list elements.
        '''
        result = get_triangle_type([1, 1, 1, 1])
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_inc_dict_sm(self):
        '''
        This tests for an invalid triangle with less than three dict elements.
        '''
        result = get_triangle_type({1:1, 2:1})
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_inc_dict_lg(self):
        '''
        This tests for an invalid triangle with more than three dict elements.
        '''
        result = get_triangle_type({1:1, 2:1, 3:1, 4:1})
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_unuse_int(self):
        '''
        This tests for an invalid triangle with integers and partly
        non-float/integer elements.
        '''
        result = get_triangle_type(2, 2, [1, 1, 1])
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_unuse_float(self):
        '''
        This tests for an invalid triangle with floats and partly
        non-float/integer elements.
        '''
        result = get_triangle_type(2.5, 2, [1, 1, 1])
        self.assertEqual(result, 'invalid')

    def test_triangle_mix_unuse_dict(self):
        '''
        This tests for an invalid triangle with a dictionary and other
        elements.
        '''
        result = get_triangle_type({"a":1, "b":1, "c":1}, 3.45678, 2)
        self.assertEqual(result, 'invalid')

    def test_triangle_zero_value_side(self):
        '''
        This tests for an invalid triangle with a side value of 0.
        '''
        result = get_triangle_type(2, 2, 0)
        self.assertEqual(result, 'invalid')

    def test_triangle_neg_value_side(self):
        '''
        This tests for an invalid triangle with a negative side value.
        '''
        result = get_triangle_type(3, 3, (-sys.maxint - 1))
        self.assertEqual(result, 'invalid')

    def test_triangle_largest_int(self):
        '''
        This tests for an valid triangle with the maximum int size.
        '''
        result = get_triangle_type(sys.maxint, sys.maxint, sys.maxint)
        self.assertEqual(result, 'equilateral')


class TestGetSquareType(TestCase):
    '''
    This class tests get_square_type for errors.
    '''
    def test_square_all_int(self):
        '''
        This tests squares using all integers.
        '''
        result = get_square_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_square_all_float(self):
        '''
        This tests squares using all float.
        '''
        result = get_square_type(3.0, 3.0, 3.0, 3.0)
        self.assertEqual(result, 'square')

    def test_square_tuple(self):
        '''
        This tests squares using a tuple.
        '''
        result = get_square_type((4, 4, 4, 4))
        self.assertEqual(result, 'square')

    def test_square_list(self):
        '''
        This tests squares using a list.
        '''
        result = get_square_type([4, 4, 4, 4])
        self.assertEqual(result, 'square')

    def test_square_dict(self):
        '''
        This tests squares using a dictionary.
        '''
        result = get_square_type({"left":6, "top":6, "right":6, "bottom":6})
        self.assertEqual(result, 'square')

    def test_rectangle_all_int(self):
        '''
        This tests rectangles using all integers.
        '''
        result = get_square_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_rectangle_all_float(self):
        '''
        This tests rectangles using all floats.
        '''
        result = get_square_type(3.0, 4.0, 3.0, 4.0)
        self.assertEqual(result, 'rectangle')

    def test_rectangle_tuple(self):
        '''
        This tests rectangles using a tuple.
        '''
        result = get_square_type((4, 2, 4, 2))
        self.assertEqual(result, 'rectangle')

    def test_rectangle_list(self):
        '''
        This tests rectangles using a list.
        '''
        result = get_square_type([4, 2, 4, 2])
        self.assertEqual(result, 'rectangle')

    def test_rectangle_dict(self):
        '''
        This tests rectangles using a dictionary.
        '''
        result = get_square_type({"left":7, "top":6, "right":7, "bottom":6})
        self.assertEqual(result, 'rectangle')

    def test_square_mixed_types(self):
        '''
        This tests rectangles using mixed types.
        '''
        result = get_square_type(3.0, 3, 3, 3.0)
        self.assertEqual(result, 'square')

    def test_invalid_rect_off_sides(self):
        '''
        This tests rectangles using invalid sides.
        '''
        result = get_square_type(1, 2, 3, 4)
        self.assertEqual(result, 'invalid')

    def test_invalid_rect_neg_sides(self):
        '''
        This tests rectangles using negative sides.
        '''
        result = get_square_type((-sys.maxint - 1), 2, (-sys.maxint - 1), 2)
        self.assertEqual(result, 'invalid')

    def test_invalid_rect_max_int(self):
        '''
        This tests rectangles using a maximum integer value.
        '''
        result = get_square_type(sys.maxint, 2, sys.maxint, 2)
        self.assertEqual(result, 'rectangle')

class TestGetQuadrilateralTypeValid(TestCase):
    '''
    This class tests get_quadrilateral_type for valid values.
    '''
    @requirements(['#0003', '#0004', '#0005'])
    def test_quad_rect_all_int(self):
        '''
        This tests for a quadrilateral rectangle using all integers.
        '''
        result = get_quadrilateral_type(2, 3, 2, 3, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_quad_rect_all_float(self):
        '''
        This tests for a quadrilateral rectangle using all floats.
        '''
        result = get_quadrilateral_type(2.0, 3.0, 2.0, 3.0, \
                                        90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'rectangle')

    def test_quad_rect_tuple(self):
        '''
        This tests for a quadrilateral rectangle using a tuple.
        '''
        result = get_quadrilateral_type((2.0, 3.0, 2.0, 3.0, \
                                         90.0, 90.0, 90.0, 90.0))
        self.assertEqual(result, 'rectangle')

    def test_quad_rect_list(self):
        '''
        This tests for a quadrilateral rectangle using a list.
        '''
        result = get_quadrilateral_type([2.0, 3.0, 2.0, 3.0, \
                                         90.0, 90.0, 90.0, 90.0])
        self.assertEqual(result, 'rectangle')

    def test_quad_rect_dict(self):
        '''
        This tests for a quadrilateral rectangle using a dictionary.
        '''
        result = get_quadrilateral_type({1:2, 2:3, 3:2, 4:3, \
                                         5:90, 6:90, 7:90, 8:90})
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_all_int(self):
        '''
        This tests for a quadrilateral square using all integers.
        '''
        result = get_quadrilateral_type(2, 2, 2, 2, \
                                        90, 90, 90, 90)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_square_all_flt(self):
        '''
        This tests for a quadrilateral square using all floats.
        '''
        result = get_quadrilateral_type(2.0, 2.0, 2.0, 2.0, \
                                        90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'square')

    def test_get_quad_square_tuple(self):
        '''
        This tests for a quadrilateral square using a tuple.
        '''
        result = get_quadrilateral_type((2.0, 2.0, 2.0, 2.0, \
                                         90.0, 90.0, 90.0, 90.0))
        self.assertEqual(result, 'square')

    def test_get_quad_square_dict(self):
        '''
        This tests for a quadrilateral square using a dictionary.
        '''
        result = get_quadrilateral_type({1:2, 2:2, 3:2, 4:2, \
                                         5:90, 6:90, 7:90, 8:90})
        self.assertEqual(result, 'square')

    def test_get_quad_square_list(self):
        '''
        This tests for a quadrilateral square using a list.
        '''
        result = get_quadrilateral_type([2.0, 2.0, 2.0, 2.0, \
                                         90.0, 90.0, 90.0, 90.0])
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhomb_all_int(self):
        '''
        This tests for a quadrilateral rhombus using all integers.
        '''
        result = get_quadrilateral_type(2, 2, 2, 2, 45, 135, 90, 90)
        self.assertEqual(result, 'rhombus')

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_quad_rhomb_all_float(self):
        '''
        This tests for a quadrilateral rhombus using all floats.
        '''
        result = get_quadrilateral_type(2.0, 2.0, 2.0, 2.0, \
                                        44.9, 135.1, 90.0, 90.0)
        self.assertEqual(result, 'rhombus')

    def test_get_quad_rhomb_tuple(self):
        '''
        This tests for a quadrilateral rhombus using a tuple.
        '''
        result = get_quadrilateral_type((2, 2, 2, 2, 45, 135, 90, 90))
        self.assertEqual(result, 'rhombus')

    def test_get_quad_rhomb_list(self):
        '''
        This tests for a quadrilateral rhombus using a list.
        '''
        result = get_quadrilateral_type([2, 2, 2, 2, 45, 135, 90, 90])
        self.assertEqual(result, 'rhombus')

    def test_get_quad_rhomb_dict(self):
        '''
        This tests for a quadrilateral rhombus using a dictionary.
        '''
        result = get_quadrilateral_type({1:2, 2:2, 3:2, 4:2, \
                                         5:89, 6:91, 7:90, 8:90})
        self.assertEqual(result, 'rhombus')

    def test_quad_mixed_types(self):
        '''
        This tests for a quadrilateral square using integers and floats.
        '''
        result = get_quadrilateral_type(2, 2, 2.0, 2.0, \
                                        90.0, 90.0, 90.0, 90.0)
        self.assertEqual(result, 'square')

    def test_quad_max_int(self):
        '''
        This tests for a quad rectangle using maximum integer sides.
        '''
        result = get_quadrilateral_type(sys.maxint, 2, sys.maxint, 2, \
                                        90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

class TestGetQuadrilateralTypeInvalid(TestCase):
    '''
    This class tests get_quadrilateral_type for invalid values.
    '''
    def test_quad_disconnected(self):
        '''
        This tests for a disconnected quad.
        '''
        result = get_quadrilateral_type(10, 10, 10, 10, 90, 91, 90, 90)
        self.assertEqual(result, 'disconnected')

    def test_invalid_quad_neg_side(self):
        '''
        This tests for an invalid quad using negative sides.
        '''
        result = get_quadrilateral_type((-sys.maxint - 1), 1, 1, 1, \
                                        90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_invalid_quad_tuple_size(self):
        '''
        This tests for an invalid quad using an incorrect tuple size.
        '''
        result = get_quadrilateral_type((1, 2))
        self.assertEqual(result, 'invalid')

    def test_invalid_quad_mix(self):
        '''
        This tests for an invalid quad using an incorrect mix of types.
        '''
        result = get_quadrilateral_type(1, 1, 1, 1, [90, 90, 90, 90])
        self.assertEqual(result, 'invalid')

    def test_invalid_quad_mix_params(self):
        '''
        This tests for an invalid quad using an incorrect mix/amount of
        type params.
        '''
        result = get_quadrilateral_type([1, 2, 3, 4], 1, 3)
        self.assertEqual(result, 'invalid')
