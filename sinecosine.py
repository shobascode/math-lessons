#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 19:12:00 2025

@author: shoba
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 17 14:29:27 2025

@author: shoba
"""

from manim import *
import numpy as np


class Intro(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        # Create axes without tick marks, starting at x = -1
        axes = Axes(
            x_range=[-1, 2 * PI, PI / 2],
            y_range=[-2, 2, 0.5],
            x_length=8,
            y_length=4,
            axis_config={
                "color": BLACK,
                "include_ticks": False,
            },
            tips=False,
        )

        # Get individual axes
        x_axis = axes.get_x_axis()
        y_axis = axes.get_y_axis()

        # Animate drawing x-axis first
        self.play(Create(x_axis), run_time=1.6)

        # Then y-axis
        self.play(Create(y_axis), run_time=1.6)

        # Plot sine and cosine
        sine_curve = axes.plot(lambda x: np.sin(x), color=BLUE)
        cosine_curve = axes.plot(lambda x: np.cos(x), color=RED)

        # Draw both curves simultaneously
        self.play(
            Create(sine_curve),
            Create(cosine_curve),
            run_time=2.25,
            rate_func=smooth
        )

        self.wait(2)


class DrawUnitCircle(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Create the circle at the origin
        circle = Circle(radius=1, color=BLUE, stroke_width=4)

        # Define the radius line (from center to right edge)
        center = circle.get_center()
        edge = circle.point_at_angle(0)  # Point to the right on the circle
        radius_line = Line(center, edge, color=BLACK, stroke_width=3)

        # Create the label "1" below the radius line
        label = Tex("1", color=BLACK).scale(0.6)
        label.next_to(radius_line, DOWN, buff=0.1)

        # Group all elements together
        circle_group = VGroup(circle, radius_line, label)

        # Draw the full scene centered
        self.play(Create(circle), run_time=1.25)
        self.wait(0.75)
        self.play(Create(radius_line), FadeIn(label), run_time=1)
        self.wait(1)
        

class DrawTriangle(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE
        
        # Define triangle points
        base = 3
        height = 2
        origin = RIGHT + DOWN * 0.5
        left_pt = origin - RIGHT * base
        top_pt = origin + UP * height

        triangle = Polygon(top_pt, left_pt, origin, color=BLACK, stroke_width=3)

        # Triangle sides for the angle
        leg1 = Line(left_pt, top_pt)
        leg2 = Line(left_pt, origin)

        # Create the angle arc
        angle_arc = Angle(leg2, leg1, radius=0.5, color=BLACK)

        # Create theta label next to arc
        theta_label = MathTex(r"\theta", color=BLACK).scale(0.6)
        label_position = angle_arc.point_from_proportion(0.85)
        theta_label.next_to(label_position, RIGHT, buff=0.2)

        # Create right-angle marker (empty square with black border)
        right_angle_marker = Square(
            side_length=0.2,
            stroke_color=BLACK,
            stroke_width=2,
            fill_opacity=0  # no fill
        )
        right_angle_marker.move_to(origin + UL * 0.1)

        # Group everything for later movement
        triangle_group = VGroup(triangle, angle_arc, theta_label, right_angle_marker)

        # Animate creation
        self.play(Create(triangle), run_time=1.5)
        self.play(Create(angle_arc), FadeIn(theta_label), FadeIn(right_angle_marker))
        self.wait(1)

        # Shift the group to the left
        self.play(triangle_group.animate.shift(LEFT * 3), run_time=1.5)
        self.wait(1)





class Radius(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Create the circle at the origin
        circle = Circle(radius=1, color=BLUE, stroke_width=4)

        # Define the radius line (from center to right edge)
        center = circle.get_center()
        edge = circle.point_at_angle(0)  # Point to the right on the circle
        radius_line = Line(center, edge, color=BLACK, stroke_width=3)

        # Create the label "1" below the radius line
        label = Tex("1", color=BLACK).scale(0.6)
        label.next_to(radius_line, DOWN, buff=0.1)

        # Group all elements together
        circle_group = VGroup(circle, radius_line, label)

        # Draw the full scene centered
        self.play(Create(circle), run_time=1.25)
        self.wait(1)
        self.play(Create(radius_line), FadeIn(label), run_time=1)
        self.wait(1)

        # Animate the group shifting to the left half of the screen
        self.play(circle_group.animate.shift(LEFT * 3), run_time=1.25)

        self.wait(1)
        
        # Define triangle points
        base = 2
        height = 1.5
        origin = RIGHT * 3 + DOWN * 0.5
        left_pt = origin - RIGHT * base
        top_pt = origin + UP * height

        triangle = Polygon(top_pt, left_pt, origin, color=BLACK, stroke_width=3)

        # Animate the triangle
        self.play(Create(triangle), run_time=1.5)
        self.wait(1)        

        # === Add angle arc and label θ next to the arc ===
        leg1 = Line(left_pt, top_pt)
        leg2 = Line(left_pt, origin)

        # Create the angle arc
        angle_arc = Angle(leg2, leg1, radius=0.3, color=BLACK)

        # Place the label next to the arc
        theta_label = MathTex(r"\theta", color=BLACK).scale(0.6)
        label_position = angle_arc.point_from_proportion(0.85)
        theta_label.next_to(label_position, RIGHT, buff=0.15)  # offset to the right of the arc center

        # Animate the arc and the label
        self.play(Create(angle_arc), FadeIn(theta_label))
        self.wait(2)

class UnitCircle(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        # Create full axes using Line
        x_axis = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2)
        y_axis = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2)

        # Animate y-axis: from bottom to top
        self.play(Create(y_axis), run_time=1.25)

        # Animate x-axis: from left to right
        self.play(Create(x_axis), run_time=1.25)

        # Draw the unit circle centered at the origin
        unit_circle = Circle(radius=1, color=BLUE, stroke_width=3)
        self.play(Create(unit_circle), run_time=2)

        self.wait(2)


class WithTriangle(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        # Create full axes using Line
        x_axis = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2)
        y_axis = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2)

        # Create the unit circle centered at the origin
        unit_circle = Circle(radius=1, color=BLUE, stroke_width=3)

        # Group axes and circle together
        full_graph = VGroup(x_axis, y_axis, unit_circle)

        # Fade in the entire graph at once
        self.play(FadeIn(full_graph), run_time=1)

        # Add a point at 60 degrees (π/3 radians)
        angle_rad = PI / 3
        x_coord = np.cos(angle_rad)
        y_coord = np.sin(angle_rad)
        point_coords = [x_coord, y_coord, 0]

        # Create the point
        point = Dot(point_coords, color=RED, radius=0.075)

        # Create the rise (vertical line) from the point to the x-axis
        rise_line = Line([x_coord, 0, 0], point_coords, color=GREEN, stroke_width=5)

        # Create the run (horizontal line) from the origin along the x-axis
        run_line = Line(ORIGIN, [x_coord, 0, 0], color=ORANGE, stroke_width=5)

        # Create the purple radius line from the origin to the point
        radius_line = Line(ORIGIN, point_coords, color=GRAY, stroke_width=5)

        # Draw the point and its label simultaneously
        self.play(Create(point), run_time=1)

        # Then animate the run (horizontal) line along the x-axis
        self.play(Create(run_line), run_time=1)

        # Then animate the rise (vertical) line
        self.play(Create(rise_line), run_time=1)
    
        # Finally, animate the purple radius line from the origin to the point
        self.play(Create(radius_line), run_time=1)

        self.wait(2)
        
class AnimateCircle(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        # Create full axes using Line
        x_axis = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2)
        y_axis = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2)

        # Create the unit circle centered at the origin
        unit_circle = Circle(radius=1, color=BLUE, stroke_width=3)

        # Add a point at 60 degrees (π/3 radians)
        start_angle = PI / 3  # Starting angle (60 degrees)
        x_coord = np.cos(start_angle)
        y_coord = np.sin(start_angle)
        point_coords = [x_coord, y_coord, 0]

        # Create the point
        point = Dot(point_coords, color=RED, radius=0.075)

        # Create the rise (vertical line) from the point to the x-axis
        rise_line = Line([x_coord, 0, 0], point_coords, color=GREEN, stroke_width=5)

        # Create the run (horizontal line) from the origin along the x-axis
        run_line = Line(ORIGIN, [x_coord, 0, 0], color=ORANGE, stroke_width=5)

        # Create the purple radius line from the origin to the point
        radius_line = Line(ORIGIN, point_coords, color=PURPLE, stroke_width=5)

        # Group axes and circle together
        full_graph = VGroup(x_axis, y_axis, unit_circle, point, rise_line, run_line, radius_line)

        # Fade in the entire graph at once
        self.play(FadeIn(full_graph), run_time=1)

        # Create the animation of the point moving counterclockwise along the unit circle
        def update_point(mob, alpha):
            # Interpolate between the starting angle (π/3) and one full rotation (2π), then back to π/3
            angle = interpolate(start_angle, start_angle + 2 * PI, alpha)  # Full circle + back to start

            # Calculate the new x and y coordinates based on the angle
            new_x = np.cos(angle)
            new_y = np.sin(angle)
            mob.move_to([new_x, new_y, 0])

            # Update the lines
            rise_line.put_start_and_end_on([new_x, 0, 0], [new_x, new_y, 0])
            run_line.put_start_and_end_on([0, 0, 0], [new_x, 0, 0])
            radius_line.put_start_and_end_on([0, 0, 0], [new_x, new_y, 0])

        # Animate the point moving counterclockwise along the circle and back to the starting position
        self.play(UpdateFromAlphaFunc(point, update_point, run_time=5))

        # Wait for a moment after the animation completes
        self.wait(2)




class CombinedSine(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        SHIFT_LEFT = LEFT * 3.5
        SHIFT_RIGHT = RIGHT * 3.5

        # ---------- UNIT CIRCLE SETUP (LEFT) ----------
        x_axis_left = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        y_axis_left = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        unit_circle = Circle(radius=1, color=GRAY, stroke_width=3).shift(SHIFT_LEFT)

        start_angle = PI / 10000  # Start very close to 0 to avoid potential division by zero
        x = np.cos(start_angle)
        y = np.sin(start_angle)
        circle_point = Dot(np.array([x, y, 0]) + SHIFT_LEFT, color=RED, radius=0.075)

        rise_line = Line(
            np.array([x, 0, 0]) + SHIFT_LEFT,
            np.array([x, y, 0]) + SHIFT_LEFT,
            color=GREEN,
            stroke_width=5
        )
        run_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x, 0, 0]) + SHIFT_LEFT,
            color=GRAY,
            stroke_width=5
        )
        radius_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x, y, 0]) + SHIFT_LEFT,
            color=GRAY,
            stroke_width=5
        )

        circle_group = VGroup(
            x_axis_left, y_axis_left, unit_circle,
            circle_point, rise_line, run_line, radius_line
        )

        # ---------- SINE GRAPH SETUP (RIGHT) ----------
        axes_right = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": BLACK},
            tips=False,
            x_axis_config={
                "numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI],
                "font_size": 28,
            },
            y_axis_config={
                "numbers_to_include": [-1, 0, 1],
                "font_size": 28,
            }
        ).shift(SHIFT_RIGHT)

        # Create custom labels for the x-axis that include pi notation
        x_labels = VGroup(
            Tex("0", font_size=28, color=BLACK).next_to(axes_right.c2p(0, 0), DOWN * 0.7),
            Tex("$\\frac{\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right.c2p(PI/2, 0), DOWN * 0.7),
            Tex("$\\pi$", font_size=28, color=BLACK).next_to(axes_right.c2p(PI, 0), DOWN * 0.7),
            Tex("$\\frac{3\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right.c2p(3*PI/2, 0), DOWN * 0.7),
            Tex("$2\\pi$", font_size=28, color=BLACK).next_to(axes_right.c2p(2*PI, 0), DOWN * 0.7),
        )

        # Create custom labels for the y-axis
        y_labels = VGroup(
            Tex("-1", font_size=28, color=BLACK).next_to(axes_right.c2p(0, -1), LEFT * 0.7),
            Tex("1", font_size=28, color=BLACK).next_to(axes_right.c2p(0, 1), LEFT * 0.7)
        )
        
        # Hide default numbers generated by axes_right for x and y axes
        for num in axes_right.get_x_axis().numbers:
            num.set_opacity(0)

        for num in axes_right.get_y_axis().numbers:
            if round(num.get_center()[1], 2) != round(axes_right.c2p(0,0)[1], 2):
                num.set_opacity(0)

        axes_right.add(x_labels, y_labels) # Add custom labels to the axes object

        sine_curve = axes_right.plot(lambda x_val: np.sin(x_val), color=GRAY)
        sine_dot = Dot(axes_right.c2p(start_angle, np.sin(start_angle)), color=RED, radius=0.075)

        self.current_angle = ValueTracker(start_angle)

        drawn_sine_curve = always_redraw(
            lambda: axes_right.plot(
                lambda val: np.sin(val) if val <= self.current_angle.get_value() else np.nan,
                color=GRAY,
                stroke_width=4
            )
        )

        animated_sine_dot = always_redraw(
            lambda: Dot(
                axes_right.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())),
                color=RED,
                radius=0.075
            )
        )

        # New: Sine rise line for the right graph, always redrawing
        sine_rise_line_right = always_redraw(
            lambda: Line(
                axes_right.c2p(self.current_angle.get_value(), 0), # Start on the x-axis
                axes_right.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())), # End at the sine point
                color=GREEN, # Matching color with the left rise line
                stroke_width=4
            )
        )

        # New: Projection line from unit circle point to sine point
        projection_line = always_redraw(
            lambda: DashedLine(
                np.array([np.cos(self.current_angle.get_value()), np.sin(self.current_angle.get_value()), 0]) + SHIFT_LEFT,
                axes_right.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())),
                color=GRAY, # Use gray to distinguish it from the "rise" lines
                stroke_width=2
            )
        )


        # Include all parts of the sine graph setup that should fade in together
        sine_group = VGroup(axes_right, x_labels, y_labels, sine_curve) # Removed sine_dot here as it's animated separately now

        # ---------- ADD TO SCENE ----------
        self.play(FadeIn(circle_group), FadeIn(sine_group), run_time=1)
        # Add the dynamically drawn parts as separate Mobjects.
        self.add(drawn_sine_curve, animated_sine_dot, sine_rise_line_right, projection_line) # Added projection_line here


        # ---------- ANIMATION FUNCTION ----------
        def update_all(mob, alpha):
            angle = interpolate(start_angle, start_angle + 2 * PI, alpha)
            self.current_angle.set_value(angle)

            cos_val = np.cos(angle)
            sin_val = np.sin(angle)

            # Update circle elements
            circle_point.move_to(np.array([cos_val, sin_val, 0]) + SHIFT_LEFT)
            rise_line.put_start_and_end_on(
                np.array([cos_val, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )
            run_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, 0, 0]) + SHIFT_LEFT
            )
            radius_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )

        # ---------- PLAY ANIMATION ----------
        self.play(
            UpdateFromAlphaFunc(circle_point, update_all, run_time=8, rate_func=linear)
        )
        self.wait(2)



class RadianUnits(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        SHIFT_LEFT = LEFT * 3.5
        SHIFT_RIGHT = RIGHT * 3.5

        # ---------- UNIT CIRCLE SETUP (LEFT) ----------
        x_axis_left = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        y_axis_left = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        unit_circle = Circle(radius=1, color=GRAY, stroke_width=3).shift(SHIFT_LEFT)

        start_angle = PI / 10000  # Start very close to 0 to avoid potential division by zero
        x = np.cos(start_angle)
        y = np.sin(start_angle)
        circle_point = Dot(np.array([x, y, 0]) + SHIFT_LEFT, color=RED, radius=0.075)

        rise_line = Line(
            np.array([x, 0, 0]) + SHIFT_LEFT,
            np.array([x, y, 0]) + SHIFT_LEFT,
            color=GREEN,
            stroke_width=5
        )
        run_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x, 0, 0]) + SHIFT_LEFT,
            color=GRAY,
            stroke_width=5
        )
        radius_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x, y, 0]) + SHIFT_LEFT,
            color=GRAY,
            stroke_width=5
        )

        # IMPORTANT FIX: Define self.current_angle BEFORE any always_redraw that uses it
        self.current_angle = ValueTracker(start_angle)


        # Arc to show angle traveled on the unit circle
        angle_arc = always_redraw(
            lambda: Arc(
                radius=1,
                start_angle=0,
                angle=self.current_angle.get_value(),
                arc_center=SHIFT_LEFT,
                color=BLUE,
                stroke_width=5
            )
        )

        circle_group = VGroup(
            x_axis_left, y_axis_left, unit_circle,
            circle_point, rise_line, run_line, radius_line
        )

        # ---------- SINE GRAPH SETUP (RIGHT) ----------
        axes_right = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": BLACK},
            tips=False,
            x_axis_config={
                "numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI],
                "font_size": 28,
            },
            y_axis_config={
                "numbers_to_include": [-1, 0, 1],
                "font_size": 28,
            }
        ).shift(SHIFT_RIGHT)

        # Create custom labels for the x-axis that include pi notation
        x_labels = VGroup(
            Tex("0", font_size=28, color=BLACK).next_to(axes_right.c2p(0, 0), DOWN * 0.7),
            Tex("$\\frac{\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right.c2p(PI/2, 0), DOWN * 0.7),
            Tex("$\\pi$", font_size=28, color=BLACK).next_to(axes_right.c2p(PI, 0), DOWN * 0.7),
            Tex("$\\frac{3\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right.c2p(3*PI/2, 0), DOWN * 0.7),
            Tex("$2\\pi$", font_size=28, color=BLACK).next_to(axes_right.c2p(2*PI, 0), DOWN * 0.7),
        )

        # Create custom labels for the y-axis
        y_labels = VGroup(
            Tex("-1", font_size=28, color=BLACK).next_to(axes_right.c2p(0, -1), LEFT * 0.7),
            Tex("1", font_size=28, color=BLACK).next_to(axes_right.c2p(0, 1), LEFT * 0.7)
        )
        
        # Hide default numbers generated by axes_right for x and y axes
        for num in axes_right.get_x_axis().numbers:
            num.set_opacity(0)

        for num in axes_right.get_y_axis().numbers:
            if round(num.get_center()[1], 2) != round(axes_right.c2p(0,0)[1], 2):
                num.set_opacity(0)

        axes_right.add(x_labels, y_labels) # Add custom labels to the axes object

        sine_curve = axes_right.plot(lambda x_val: np.sin(x_val), color=GRAY)
        sine_dot = Dot(axes_right.c2p(start_angle, np.sin(start_angle)), color=RED, radius=0.075)

        drawn_sine_curve = always_redraw(
            lambda: axes_right.plot(
                lambda val: np.sin(val) if val <= self.current_angle.get_value() else np.nan,
                color=GRAY,
                stroke_width=4
            )
        )

        animated_sine_dot = always_redraw(
            lambda: Dot(
                axes_right.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())),
                color=RED,
                radius=0.075
            )
        )

        # Sine rise line for the right graph, always redrawing
        sine_rise_line_right = always_redraw(
            lambda: Line(
                axes_right.c2p(self.current_angle.get_value(), 0), # Start on the x-axis
                axes_right.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())), # End at the sine point
                color=GREEN, # Matching color with the left rise line
                stroke_width=4
            )
        )

        # New: Blue line on the x-axis of the right graph
        # This will be updated within the update_all function
        x_axis_progress_line = Line(
            axes_right.c2p(0, 0),  # Start at the origin of the right axes
            axes_right.c2p(start_angle, 0), # Initial end point at start_angle
            color=BLUE,
            stroke_width=5
        )


        # Include all parts of the sine graph setup that should fade in together
        # Add x_axis_progress_line here so it fades in with the axes.
        sine_group = VGroup(axes_right, x_labels, y_labels, sine_curve, x_axis_progress_line)

        # ---------- ADD TO SCENE ----------
        self.play(FadeIn(circle_group), FadeIn(sine_group), run_time=1)
        # Add the dynamically drawn parts as separate Mobjects.
        self.add(drawn_sine_curve, animated_sine_dot, sine_rise_line_right, angle_arc)


        # ---------- ANIMATION FUNCTION ----------
        def update_all(mob, alpha):
            angle = interpolate(start_angle, start_angle + 2 * PI, alpha)
            self.current_angle.set_value(angle) # Update ValueTracker for always_redraws to react

            cos_val = np.cos(angle)
            sin_val = np.sin(angle)

            # Update circle elements
            circle_point.move_to(np.array([cos_val, sin_val, 0]) + SHIFT_LEFT)
            rise_line.put_start_and_end_on(
                np.array([cos_val, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )
            run_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, 0, 0]) + SHIFT_LEFT
            )
            radius_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )

            # Update the blue x-axis progress line on the right graph
            x_axis_progress_line.put_start_and_end_on(
                axes_right.c2p(0, 0),
                axes_right.c2p(angle, 0)
            )

        # ---------- PLAY ANIMATION ----------
        self.play(
            UpdateFromAlphaFunc(circle_point, update_all, run_time=8, rate_func=linear)
        )
        self.wait(2)
        
    

class CombinedCosine(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        SHIFT_LEFT = LEFT * 3.5    # Left side (unit circle)
        SHIFT_RIGHT = RIGHT * 3.5 # Right side (cosine wave)

        # ---------- UNIT CIRCLE SETUP (LEFT) ----------
        x_axis_left = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        y_axis_left = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        unit_circle = Circle(radius=1, color=GRAY, stroke_width=3).shift(SHIFT_LEFT)

        start_angle = PI / 10000  # Start very close to 0
        x_initial = np.cos(start_angle)
        y_initial = np.sin(start_angle)
        circle_point = Dot(np.array([x_initial, y_initial, 0]) + SHIFT_LEFT, color=RED, radius=0.075)

        # For cosine, the "run" line on the unit circle (x-component) will be emphasized
        rise_line = Line(
            np.array([x_initial, 0, 0]) + SHIFT_LEFT,
            np.array([x_initial, y_initial, 0]) + SHIFT_LEFT,
            color=GRAY, # This is the y-component, less emphasized for cosine
            stroke_width=5
        )
        run_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x_initial, 0, 0]) + SHIFT_LEFT,
            color=ORANGE, # This is the x-component, emphasized for cosine
            stroke_width=5
        )
        radius_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x_initial, y_initial, 0]) + SHIFT_LEFT,
            color=GRAY,
            stroke_width=5
        )

        circle_group = VGroup(
            x_axis_left, y_axis_left, unit_circle,
            circle_point, rise_line, run_line, radius_line
        )

        # ---------- COSINE GRAPH SETUP (RIGHT) ----------
        axes_right = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": BLACK},
            tips=False,
            x_axis_config={
                "numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI],
                "font_size": 28,
            },
            y_axis_config={
                "numbers_to_include": [-1, 0, 1],
                "font_size": 28,
            }
        ).shift(SHIFT_RIGHT)

        # Create custom labels for the x-axis that include pi notation
        x_labels = VGroup(
            Tex("0", font_size=28, color=BLACK).next_to(axes_right.c2p(0, 0), DOWN * 0.7),
            Tex("$\\frac{\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right.c2p(PI/2, 0), DOWN * 0.7),
            Tex("$\\pi$", font_size=28, color=BLACK).next_to(axes_right.c2p(PI, 0), DOWN * 0.7),
            Tex("$\\frac{3\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right.c2p(3*PI/2, 0), DOWN * 0.7),
            Tex("$2\\pi$", font_size=28, color=BLACK).next_to(axes_right.c2p(2*PI, 0), DOWN * 0.7),
        )

        # Create custom labels for the y-axis
        y_labels = VGroup(
            Tex("-1", font_size=28, color=BLACK).next_to(axes_right.c2p(0, -1), LEFT * 0.7),
            Tex("1", font_size=28, color=BLACK).next_to(axes_right.c2p(0, 1), LEFT * 0.7)
        )
        
        # Hide default numbers generated by axes_right for x and y axes
        for num in axes_right.get_x_axis().numbers:
            num.set_opacity(0)

        for num in axes_right.get_y_axis().numbers:
            if round(num.get_center()[1], 2) != round(axes_right.c2p(0,0)[1], 2):
                num.set_opacity(0)

        axes_right.add(x_labels, y_labels) # Add custom labels to the axes object

        # Plot the full cosine curve (will be partially drawn)
        cosine_curve = axes_right.plot(lambda x_val: np.cos(x_val), color=GRAY)

        # ValueTracker to control the animation progress
        self.current_angle = ValueTracker(start_angle)

        # The dynamically drawn part of the cosine curve
        drawn_cosine_curve = always_redraw(
            lambda: axes_right.plot(
                lambda val: np.cos(val) if val <= self.current_angle.get_value() else np.nan,
                color=GRAY, # Matching color with the run line
                stroke_width=4
            )
        )

        # The dot moving along the cosine curve
        animated_cosine_dot = always_redraw(
            lambda: Dot(
                axes_right.c2p(self.current_angle.get_value(), np.cos(self.current_angle.get_value())),
                color=RED,
                radius=0.075
            )
        )

        # Initial Cosine "rise" line for the right graph
        # This line will be explicitly updated in update_all, not always_redraw
        initial_cosine_point = axes_right.c2p(start_angle, np.cos(start_angle))
        cosine_rise_line_right = Line(
            axes_right.c2p(start_angle, 0), # Start on the x-axis
            initial_cosine_point, # End at the initial cosine point
            color=ORANGE, # Matching color with the run line from unit circle
            stroke_width=4
        )
        
        # We removed the projection_line as requested.

        # Group elements for initial fade-in.
        # Include cosine_rise_line_right here so it fades in with the axes.
        cosine_graph_elements = VGroup(axes_right, x_labels, y_labels, cosine_curve, cosine_rise_line_right)

        # ---------- ADD TO SCENE ----------
        self.play(FadeIn(circle_group), FadeIn(cosine_graph_elements), run_time=1)
        # Add the dynamically drawn parts which are managed by always_redraw
        self.add(drawn_cosine_curve, animated_cosine_dot)


        # ---------- ANIMATION FUNCTION ----------
        def update_all(mob, alpha):
            angle = interpolate(start_angle, start_angle + 2 * PI, alpha)
            self.current_angle.set_value(angle) # Update ValueTracker for always_redraws

            cos_val = np.cos(angle)
            sin_val = np.sin(angle)

            # Update circle elements
            circle_point.move_to(np.array([cos_val, sin_val, 0]) + SHIFT_LEFT)
            rise_line.put_start_and_end_on(
                np.array([cos_val, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )
            run_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, 0, 0]) + SHIFT_LEFT
            )
            radius_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )

            # Explicitly update the cosine rise line on the right graph
            cosine_rise_line_right.put_start_and_end_on(
                axes_right.c2p(angle, 0),
                axes_right.c2p(angle, cos_val)
            )

        # ---------- PLAY ANIMATION ----------
        # UpdateFromAlphaFunc will drive the update_all function, which moves the point,
        # updates the circle lines, and updates the cosine_rise_line_right.
        # The always_redraws will automatically update based on self.current_angle.
        self.play(
            UpdateFromAlphaFunc(circle_point, update_all, run_time=8, rate_func=linear)
        )
        self.wait(2)


class CircleTransform(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Step 1: Draw the unit circle centered at the origin
        unit_circle = Circle(radius=1, color=BLUE, stroke_width=3)
        self.play(Create(unit_circle), run_time=1)
        self.wait(0.3)

        # Step 2: Draw the radius line from origin to (1, 0) and label "1"
        radius_endpoint = unit_circle.point_at_angle(0)
        radius_line = Line(ORIGIN, radius_endpoint, color=BLACK, stroke_width=3)
        label = Tex("1", color=BLACK).scale(0.6)
        label.next_to(radius_line, DOWN, buff=0.1)

        self.play(Create(radius_line), FadeIn(label), run_time=1)
        self.wait(1)

        # Step 3 & 4: Create both axes and fade them in while fading out the radius line and label
        x_axis = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2)
        y_axis = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2)

        # Step 5: Create and fade in the black triangle (π/4 angle)
        theta = PI / 4
        point_on_circle = unit_circle.point_at_angle(theta)
        projection_on_x = [point_on_circle[0], 0, 0]

        hypotenuse = Line(ORIGIN, point_on_circle, color=GRAY)
        vertical_leg = Line(point_on_circle, projection_on_x, color=GRAY)
        base_leg = Line(projection_on_x, ORIGIN, color=GRAY)

        triangle = VGroup(hypotenuse, vertical_leg, base_leg)
        
        self.play(
            FadeIn(x_axis),
            FadeIn(y_axis),
            FadeOut(radius_line),
            FadeOut(label),
            FadeIn(triangle),
            run_time=1
        )


        self.wait(1)



class CombinedSineCosine(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE

        SHIFT_LEFT = LEFT * 3.5
        SHIFT_RIGHT_TOP = RIGHT * 3.5 + UP * 1.65  # Top right for sine
        SHIFT_RIGHT_BOTTOM = RIGHT * 3.5 + DOWN * 1.65  # Bottom right for cosine

        # ---------- UNIT CIRCLE SETUP (LEFT) ----------
        x_axis_left = Line(LEFT * 2.5, RIGHT * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        y_axis_left = Line(DOWN * 2.5, UP * 2.5, color=BLACK, stroke_width=2).shift(SHIFT_LEFT)
        unit_circle = Circle(radius=1, color=GRAY, stroke_width=3).shift(SHIFT_LEFT)

        start_angle = PI / 10000  # Start very close to 0 to avoid potential division by zero
        x = np.cos(start_angle)
        y = np.sin(start_angle)
        circle_point = Dot(np.array([x, y, 0]) + SHIFT_LEFT, color=RED, radius=0.075)

        rise_line = Line(
            np.array([x, 0, 0]) + SHIFT_LEFT,
            np.array([x, y, 0]) + SHIFT_LEFT,
            color=GREEN,
            stroke_width=5
        )
        run_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x, 0, 0]) + SHIFT_LEFT,
            color=ORANGE,
            stroke_width=5
        )
        radius_line = Line(
            np.array([0, 0, 0]) + SHIFT_LEFT,
            np.array([x, y, 0]) + SHIFT_LEFT,
            color=GRAY,
            stroke_width=5
        )

        circle_group = VGroup(
            x_axis_left, y_axis_left, unit_circle,
            circle_point, rise_line, run_line, radius_line
        )

        # ---------- SINE GRAPH SETUP (TOP RIGHT) ----------
        axes_right_top = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": BLACK},
            tips=False,
            x_axis_config={
                "numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI],
                "font_size": 28,
            },
            y_axis_config={
                "numbers_to_include": [-1, 0, 1],
                "font_size": 28,
            }
        ).shift(SHIFT_RIGHT_TOP)

        x_labels_top = VGroup(
            Tex("0", font_size=28, color=BLACK).next_to(axes_right_top.c2p(0, 0), DOWN * 0.7),
            Tex("$\\frac{\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right_top.c2p(PI/2, 0), DOWN * 0.7),
            Tex("$\\pi$", font_size=28, color=BLACK).next_to(axes_right_top.c2p(PI, 0), DOWN * 0.7),
            Tex("$\\frac{3\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right_top.c2p(3*PI/2, 0), DOWN * 0.7),
            Tex("$2\\pi$", font_size=28, color=BLACK).next_to(axes_right_top.c2p(2*PI, 0), DOWN * 0.7),
        )

        y_labels_top = VGroup(
            Tex("-1", font_size=28, color=BLACK).next_to(axes_right_top.c2p(0, -1), LEFT * 0.7),
            Tex("1", font_size=28, color=BLACK).next_to(axes_right_top.c2p(0, 1), LEFT * 0.7)
        )
        
        axes_right_top.add(x_labels_top, y_labels_top)

        sine_curve = axes_right_top.plot(lambda x_val: np.sin(x_val), color=GRAY)
        sine_dot = Dot(axes_right_top.c2p(start_angle, np.sin(start_angle)), color=RED, radius=0.075)

        self.current_angle = ValueTracker(start_angle)

        drawn_sine_curve = always_redraw(
            lambda: axes_right_top.plot(
                lambda val: np.sin(val) if val <= self.current_angle.get_value() else np.nan,
                color=GRAY,
                stroke_width=4
            )
        )

        animated_sine_dot = always_redraw(
            lambda: Dot(
                axes_right_top.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())),
                color=RED,
                radius=0.075
            )
        )

        sine_rise_line_right = always_redraw(
            lambda: Line(
                axes_right_top.c2p(self.current_angle.get_value(), 0),
                axes_right_top.c2p(self.current_angle.get_value(), np.sin(self.current_angle.get_value())),
                color=GREEN,
                stroke_width=4
            )
        )

        # ---------- COSINE GRAPH SETUP (BOTTOM RIGHT) ----------
        axes_right_bottom = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": BLACK},
            tips=False,
            x_axis_config={
                "numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI],
                "font_size": 28,
            },
            y_axis_config={
                "numbers_to_include": [-1, 0, 1],
                "font_size": 28,
            }
        ).shift(SHIFT_RIGHT_BOTTOM)

        x_labels_bottom = VGroup(
            Tex("0", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(0, 0), DOWN * 0.7),
            Tex("$\\frac{\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(PI/2, 0), DOWN * 0.7),
            Tex("$\\pi$", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(PI, 0), DOWN * 0.7),
            Tex("$\\frac{3\\pi}{2}$", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(3*PI/2, 0), DOWN * 0.7),
            Tex("$2\\pi$", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(2*PI, 0), DOWN * 0.7),
        )

        y_labels_bottom = VGroup(
            Tex("-1", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(0, -1), LEFT * 0.7),
            Tex("1", font_size=28, color=BLACK).next_to(axes_right_bottom.c2p(0, 1), LEFT * 0.7)
        )

        axes_right_bottom.add(x_labels_bottom, y_labels_bottom)

        cosine_curve = axes_right_bottom.plot(lambda x_val: np.cos(x_val), color=GRAY)
        cosine_dot = Dot(axes_right_bottom.c2p(start_angle, np.cos(start_angle)), color=RED, radius=0.075)

        drawn_cosine_curve = always_redraw(
            lambda: axes_right_bottom.plot(
                lambda val: np.cos(val) if val <= self.current_angle.get_value() else np.nan,
                color=GRAY,
                stroke_width=4
            )
        )

        animated_cosine_dot = always_redraw(
            lambda: Dot(
                axes_right_bottom.c2p(self.current_angle.get_value(), np.cos(self.current_angle.get_value())),
                color=RED,
                radius=0.075
            )
        )

        cosine_rise_line_right = always_redraw(
            lambda: Line(
                axes_right_bottom.c2p(self.current_angle.get_value(), 0),
                axes_right_bottom.c2p(self.current_angle.get_value(), np.cos(self.current_angle.get_value())),
                color=ORANGE,
                stroke_width=4
            )
        )

        # ---------- GROUPING FOR FADE-IN ----------
        sine_group = VGroup(axes_right_top, sine_curve)
        cosine_group = VGroup(axes_right_bottom, cosine_curve)

        # ---------- ADD TO SCENE ----------
        self.play(FadeIn(circle_group), FadeIn(sine_group), FadeIn(cosine_group), run_time=1)

        # Add the dynamically drawn parts as separate Mobjects.
        self.add(drawn_sine_curve, animated_sine_dot, sine_rise_line_right)
        self.add(drawn_cosine_curve, animated_cosine_dot, cosine_rise_line_right)

        # ---------- ANIMATION FUNCTION ----------
        def update_all(mob, alpha):
            angle = interpolate(start_angle, start_angle + 2 * PI, alpha)
            self.current_angle.set_value(angle)

            sin_val = np.sin(angle)
            cos_val = np.cos(angle)

            # Update circle elements
            circle_point.move_to(np.array([cos_val, sin_val, 0]) + SHIFT_LEFT)
            rise_line.put_start_and_end_on(
                np.array([cos_val, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )
            run_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, 0, 0]) + SHIFT_LEFT
            )
            radius_line.put_start_and_end_on(
                np.array([0, 0, 0]) + SHIFT_LEFT,
                np.array([cos_val, sin_val, 0]) + SHIFT_LEFT
            )

        # ---------- PLAY ANIMATION ----------
        self.play(
            UpdateFromAlphaFunc(circle_point, update_all, run_time=8, rate_func=linear)
        )
        self.wait(2)

