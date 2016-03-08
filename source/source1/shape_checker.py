"""
Joseph Miller - CST236
Lab Assignment 1

:mod:`source.source1` -- Example source code
============================================

The following example code determines
    if a set of 3 sides of a triangle is
        equilateral, scalene or isosceles
    if a rectangle is a rectangle or a square
    if a parallelogram is a rectangle, square, rhombus, or disconnected
"""


# defined to get rid of magic numbers - Joe (1/12/16)
A_IDX = 0
B_IDX = 1
C_IDX = 2
LEFT_IDX = 0
TOP_IDX = 1
RIGHT_IDX = 2
BOTTOM_IDX = 3
TOP_LEFT_ANGLE_IDX = 4
TOP_RIGHT_ANGLE_IDX = 5
BOTTOM_LEFT_ANGLE_IDX = 6
BOTTOM_RIGHT_ANGLE_IDX = 7
NUM_TRIANGLE_PARAMS = 3
NUM_SQUARE_PARAMS = 4
NUM_QUADRILATERAL_PARAMS = 8

def get_triangle_type(side_a=0, side_b=0, side_c=0):
    """
    Determine if the given triangle is equilateral, scalene or isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """

    # fixed functionality and narrowed incorrect parameter detection in the
    # below if block - Joe (1/12/16)
    if (isinstance(side_a, (tuple, list))
            and len(side_a) == NUM_TRIANGLE_PARAMS):
        if (not (isinstance(side_b, int) and (side_b == 0)
                 and isinstance(side_c, int) and (side_c == 0))):
            return "invalid"
        side_c = side_a[C_IDX]
        side_b = side_a[B_IDX]
        side_a = side_a[A_IDX]

    # narrowed incorrect parameter detection in below if block - Joe (1/12/16)
    #
    # The following statements in this if block's pylint warnings are disabled
    # because pylint is not understanding that side_a can be something other
    # than an int.
    # pylint: disable=no-member
    if (isinstance(side_a, dict)
            and (len(side_a.keys()) == NUM_TRIANGLE_PARAMS)):
        if (not (isinstance(side_b, int) and (side_b == 0)
                 and isinstance(side_c, int) and (side_c == 0))):
            return "invalid"
        values = []
        # pylint: disable=no-member
        for value in side_a.values():
            values.append(value)
        side_a = values[A_IDX]
        side_b = values[B_IDX]
        side_c = values[C_IDX]

    if (not (isinstance(side_a, (int, float))
             and isinstance(side_b, (int, float))
             and isinstance(side_c, (int, float)))
            or (side_a <= 0 or side_b <= 0 or side_c <= 0)):
        return "invalid"

    if side_a == side_b and side_b == side_c:
        return "equilateral"

    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "isosceles"
    else:
        return "scalene"


def get_square_type(left=0, top=0, right=0, bottom=0):
    """
    Determine if the given rectangle is also a square

    :param left: line left
    :type left: float or int or tuple or list or dict

    :param top: line top
    :type top: float or int

    :param right: line right
    :type right: float or int

    :param bottom: line bottom
    :type bottom: float or int

    :return: "square", "rectangle", or "invalid"
    :rtype: str
    """

    # The following if blocks have many boolean expressions to cover the
    # wide variety of options that need to exist for this to work.
    # pylint: disable=too-many-boolean-expressions
    if isinstance(left, (tuple, list)):
        if ((len(left) == NUM_SQUARE_PARAMS and isinstance(top, int)
             and (top == 0) and isinstance(right, int)
             and (right == 0) and isinstance(bottom, int) and (bottom == 0))):
            top = left[TOP_IDX]
            right = left[RIGHT_IDX]
            bottom = left[BOTTOM_IDX]
            left = left[LEFT_IDX]

    # pylint: disable=too-many-boolean-expressions
    if isinstance(left, dict):
        # The following statements in this if block's pylint warnings are
        # disabled because pylint is not understanding that left can be
        # something other than an int.
        # pylint: disable=no-member
        if ((len(left.keys()) == NUM_SQUARE_PARAMS and isinstance(top, int)
             and (top == 0) and isinstance(right, int) and (right == 0)
             and isinstance(bottom, int) and (bottom == 0))):
            values = []
            # pylint: disable=no-member
            for value in left.values():
                values.append(value)
            left = values[LEFT_IDX]
            top = values[TOP_IDX]
            right = values[RIGHT_IDX]
            bottom = values[BOTTOM_IDX]

    if (isinstance(left, (int, float)) and isinstance(top, (int, float))
            and isinstance(right, (int, float))
            and isinstance(bottom, (int, float))):
        if left == top == right == bottom:
            if left > 0:
                return "square"
        elif (left == right > 0) and (top == bottom > 0):
            return "rectangle"

    return "invalid"


# The following function has many parameters to cover a wide variety of cases,
# hence the disabled pylint warning.
# pylint: disable=too-many-arguments
def get_quadrilateral_type(left=0, top=0, right=0, bottom=0, top_left_angle=0,
                           top_right_angle=0, bottom_left_angle=0,
                           bottom_right_angle=0):
    """
    Determine the type of quadrilateral

    :param left: line left
    :type left: float or int or tuple or list or dict

    :param top: line top
    :type top: float or int

    :param right: line right
    :type right: float or int

    :param bottom: line bottom
    :type bottom: float or int

    :param top_left_angle: line top_left_angle
    :type top_left_angle: float or int or tuple or list or dict

    :param top_right_angle: line top_right_angle
    :type top_right_angle: float or int

    :param bottom_left_angle: line bottom_left_angle
    :type bottom_left_angle: float or int

    :param bottom_right_angle: line bottom_right_angle
    :type bottom_right_angle: float or int

    :return: "square", "rectangle", "rhombus", "disconnected", or "invalid"
    :rtype: str
    """

    if isinstance(left, (list, tuple, dict)):
        if (not (isinstance(top, int) and (top == 0)
                 and isinstance(right, int) and (right == 0)
                 and isinstance(bottom, int) and (bottom == 0)
                 and isinstance(top_left_angle, int) and (top_left_angle == 0)
                 and isinstance(top_right_angle, int) and (top_right_angle == 0)
                 and isinstance(bottom_left_angle, int)
                 and (bottom_left_angle == 0)
                 and isinstance(bottom_right_angle, int)
                 and (bottom_right_angle == 0))):
            return "invalid"

        # The following statements in this if block's pylint warnings are
        # disabled because pylint is not understanding that left can be
        # something other than an int.
        # pylint: disable=no-member
        if isinstance(left, dict) and (len(left.keys()) == NUM_QUADRILATERAL_PARAMS):
            values = []
            # pylint: disable=no-member
            for value in left.values():
                values.append(value)
            left = values
        if (isinstance(left, (list, tuple))
                and (len(left) == NUM_QUADRILATERAL_PARAMS)):
            bottom_right_angle = left[BOTTOM_RIGHT_ANGLE_IDX]
            bottom_left_angle = left[BOTTOM_LEFT_ANGLE_IDX]
            top_right_angle = left[TOP_RIGHT_ANGLE_IDX]
            top_left_angle = left[TOP_LEFT_ANGLE_IDX]
            bottom = left[BOTTOM_IDX]
            right = left[RIGHT_IDX]
            top = left[TOP_IDX]
            left = left[LEFT_IDX]

    if (not (isinstance(left, (float, int)) and (left > 0)
             and isinstance(top, (float, int)) and (top > 0)
             and isinstance(right, (float, int)) and (right > 0)
             and isinstance(bottom, (float, int)) and (bottom > 0)
             and isinstance(top_left_angle, (float, int))
             and (top_left_angle > 0)
             and isinstance(top_right_angle, (float, int))
             and (top_right_angle > 0)
             and isinstance(bottom_left_angle, (float, int))
             and (bottom_left_angle > 0)
             and isinstance(bottom_right_angle, (float, int))
             and (bottom_right_angle > 0))):
        return "invalid"

    if ((top_left_angle + top_right_angle + bottom_left_angle +
         bottom_right_angle) == 360):
        if (top_left_angle == top_right_angle == bottom_left_angle ==
                bottom_right_angle == 90):
            if left == top == right == bottom:
                return "square"
            elif (left == right) and (top == bottom):
                return "rectangle"
        elif (left == right) and (top == bottom):
            return "rhombus"
    return "disconnected"
