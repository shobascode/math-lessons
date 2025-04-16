#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 11:10:28 2025

@author: shoba
"""

from manim import *
import numpy as np

# test comment

class SettingScene(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Create the x-axis with a small negative extension and thin stroke
        x_axis = Line(LEFT * 0.5, RIGHT * 3, color=BLACK, stroke_width=2)

        # Create the y-axis with a small negative extension and thin stroke
        y_axis = Line(DOWN * 0.5, UP * 3, color=BLACK, stroke_width=2)

        # Draw the axes
        self.play(Create(x_axis))
        self.play(Create(y_axis))

        # Define a generic parabola function
        def generic_parabola(x):
            return 0.5 * x**2

        # Calculate the x-value where the parabola reaches the top of the y-axis
        y_max = UP * 3
        y_max_value = y_max[1]
        x_max = (2 * y_max_value)**0.5

        # Create the parabola graph, limiting x-range
        parabola_graph = FunctionGraph(
            generic_parabola,
            x_range=[0, min(3, x_max)],  # Limit to y-axis or x=3, whichever is smaller
            color=PINK,
        )

        # Draw the parabola graph
        self.play(Create(parabola_graph))

        # Calculate the middle point on the graph
        middle_x = min(3, x_max) / 2  # Middle x value within the x_range
        middle_y = generic_parabola(middle_x)
        middle_point = Dot([middle_x, middle_y, 0], color=BLACK, radius=0.07) #make dot smaller

        # Draw the middle point
        self.play(Create(middle_point))

        self.wait(2)
        
        
class Slope(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Axes setup
        screen_width = self.camera.frame_width
        screen_height = self.camera.frame_height
        axes_width = screen_width * 0.3
        axes_height = screen_height * 0.5
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=axes_width,
            y_length=axes_height,
            axis_config={"color": BLACK, "stroke_width": 2, "include_tip": False},
        )
        
        # Move axes to the left side to make room for text
        axes.shift(LEFT * 2.5)
        
        graph = axes.plot(lambda x: 2 * x, color=PURPLE, x_range=[-2.75, 2.75])
        self.play(FadeIn(axes), FadeIn(graph))
        self.wait(0.5)
        
        # Trackers
        x1_tracker = ValueTracker(1)
        x2_tracker = ValueTracker(2)
        
        # Initial positions for rise/run line creation
        x1, x2 = x1_tracker.get_value(), x2_tracker.get_value()
        y1, y2 = 2 * x1, 2 * x2
        
        # Create dots and lines
        point1 = Dot(axes.coords_to_point(x1, y1), color=BLUE)
        point2 = Dot(axes.coords_to_point(x2, y2), color=BLUE)
        rise_line = Line(
            axes.coords_to_point(x1, y1),
            axes.coords_to_point(x1, y2),
            color=ORANGE
        )
        run_line = Line(
            axes.coords_to_point(x1, y2),
            axes.coords_to_point(x2, y2),
            color=ORANGE
        )
        
        # Calculate position for labels - right of the axes
        label_reference_point = axes.get_right() + RIGHT * 1.5
        
        # Create initial fixed labels with the starting values
        initial_delta_y = 2.00  # y2 - y1 = 2*2 - 2*1 = 4 - 2 = 2
        initial_delta_x = 1.00  # x2 - x1 = 2 - 1 = 1
        initial_slope = 2.00    # delta_y / delta_x = 2/1 = 2
        
        # Initial fixed value labels
        delta_y_fixed = MathTex(f"\\Delta y = {initial_delta_y:.2f}", color=BLACK).scale(0.8)
        delta_x_fixed = MathTex(f"\\Delta x = {initial_delta_x:.2f}", color=BLACK).scale(0.8)
        slope_fixed = MathTex(f"Slope = \\frac{{\\Delta y}}{{\\Delta x}} = {initial_slope:.2f}", color=BLACK).scale(0.8)
        
        # Create labels with dynamic parts for later
        delta_y_text = MathTex("\\Delta y = ", color=BLACK).scale(0.8)
        delta_y_value = DecimalNumber(2 * x2 - 2 * x1, num_decimal_places=2, color=BLACK).scale(0.8)
        delta_y_group = VGroup(delta_y_text, delta_y_value).arrange(RIGHT)
        
        delta_x_text = MathTex("\\Delta x = ", color=BLACK).scale(0.8)
        delta_x_value = DecimalNumber(x2 - x1, num_decimal_places=2, color=BLACK).scale(0.8)
        delta_x_group = VGroup(delta_x_text, delta_x_value).arrange(RIGHT)
        
        slope_text = MathTex("Slope = \\frac{\\Delta y}{\\Delta x} = ", color=BLACK).scale(0.8)
        slope_value = DecimalNumber(self.calculate_slope(x1, x2), num_decimal_places=2, color=BLACK).scale(0.8)
        slope_group = VGroup(slope_text, slope_value).arrange(RIGHT)
        
        # Position the fixed labels first
        fixed_labels = VGroup(delta_y_fixed, delta_x_fixed, slope_fixed).arrange(DOWN, aligned_edge=LEFT)
        fixed_labels.move_to(label_reference_point, aligned_edge=LEFT)
        
        # Create a VGroup for dynamic labels (not added to scene yet)
        dynamic_labels = VGroup(delta_y_group, delta_x_group, slope_group).arrange(DOWN, aligned_edge=LEFT)
        dynamic_labels.move_to(label_reference_point, aligned_edge=LEFT)
        
        # Animate each step with fixed labels
        self.play(FadeIn(point1, point2), run_time=0.5)
        self.wait(0.5)
        self.play(Create(rise_line), FadeIn(delta_y_fixed), run_time=0.5)
        self.wait(0.5)
        self.play(Create(run_line), FadeIn(delta_x_fixed), run_time=0.5)
        self.wait(1)
        self.play(FadeIn(slope_fixed), run_time=0.5)
        self.wait(1)
        
        # Switch from fixed to dynamic labels
        self.play(
            ReplacementTransform(delta_y_fixed, delta_y_group),
            ReplacementTransform(delta_x_fixed, delta_x_group),
            ReplacementTransform(slope_fixed, slope_group),
            run_time=0.5
        )
        self.wait(0.5)
        
        # Add updaters for points and lines
        point1.add_updater(lambda m: m.move_to(axes.coords_to_point(x1_tracker.get_value(), 2 * x1_tracker.get_value())))
        point2.add_updater(lambda m: m.move_to(axes.coords_to_point(x2_tracker.get_value(), 2 * x2_tracker.get_value())))
        
        rise_line.add_updater(lambda m: m.become(Line(
            axes.coords_to_point(x1_tracker.get_value(), 2 * x1_tracker.get_value()),
            axes.coords_to_point(x1_tracker.get_value(), 2 * x2_tracker.get_value()),
            color=ORANGE
        )))
        
        run_line.add_updater(lambda m: m.become(Line(
            axes.coords_to_point(x1_tracker.get_value(), 2 * x2_tracker.get_value()),
            axes.coords_to_point(x2_tracker.get_value(), 2 * x2_tracker.get_value()),
            color=ORANGE
        )))
        
        # Add updaters for numerical values
        delta_y_value.add_updater(
            lambda m: m.set_value(2 * x2_tracker.get_value() - 2 * x1_tracker.get_value())
        )
        
        delta_x_value.add_updater(
            lambda m: m.set_value(x2_tracker.get_value() - x1_tracker.get_value())
        )
        
        slope_value.add_updater(
            lambda m: m.set_value(self.calculate_slope(x1_tracker.get_value(), x2_tracker.get_value()))
        )

        # Draw a box around the slope_value
        box = SurroundingRectangle(slope_value, color=ORANGE, buff=0.1)
        box.add_updater(lambda m: m.become(SurroundingRectangle(slope_value, color=ORANGE, buff=0.1)))

        # Animate movement with the box
        self.play(
            x1_tracker.animate.set_value(-2),
            x2_tracker.animate.set_value(1),
            Create(box),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            x1_tracker.animate.set_value(1),
            x2_tracker.animate.set_value(2),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(box))

    def calculate_slope(self, x1, x2):
        delta_y = 2 * x2 - 2 * x1
        delta_x = x2 - x1
        if delta_x != 0:
            return delta_y / delta_x
        else:
            return 0.0
    


class Curve(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Axes setup
        screen_width = self.camera.frame_width
        screen_height = self.camera.frame_height
        axes_width = screen_width * 0.3
        axes_height = screen_height * 0.5
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=axes_width,
            y_length=axes_height,
            axis_config={"color": BLACK, "stroke_width": 2, "include_tip": False},
        )
        axes.shift(LEFT * 2.5)

        # Plot the cubic curve
        cubic_graph = axes.plot(lambda x: 0.1 * x**3, color=RED, x_range=[-3.75, 3.75])
        self.play(FadeIn(axes, cubic_graph))
        self.wait(1)

        # Trackers
        x_tracker = ValueTracker(-3)
        dx_tracker = ValueTracker(0.2)  # Controls how far the two tangent points are spread

        # Helpers
        def get_y(x): return 0.1 * x**3
        def get_slope(x): return 0.3 * x**2

        # Get coordinates of a point on tangent line from center x and offset dx
        def point_coords(x0, offset):
            slope = get_slope(x0)
            y0 = get_y(x0)
            x1 = x0 + offset
            y1 = slope * (x1 - x0) + y0
            return x1, y1

        # Constant length for tangent line (in axes units)
        tangent_half_length = 1.5

        # Tangent line with constant length
        tangent_line = always_redraw(lambda: axes.plot(
            lambda x: get_slope(x_tracker.get_value()) * (x - x_tracker.get_value()) + get_y(x_tracker.get_value()),
            color=BLUE,
            x_range=[
                max(x_tracker.get_value() - tangent_half_length, -3.75),  # Ensure it starts within plot range
                min(x_tracker.get_value() + tangent_half_length, 3.75)    # Ensure it stays within plot range
            ]
        ))

        # Points on the tangent line
        point1 = always_redraw(lambda: Dot(
            axes.coords_to_point(*point_coords(x_tracker.get_value(), -dx_tracker.get_value())),
            color=YELLOW
        ))
        point2 = always_redraw(lambda: Dot(
            axes.coords_to_point(*point_coords(x_tracker.get_value(), dx_tracker.get_value())),
            color=YELLOW
        ))

        # Rise and Run lines
        rise_line = always_redraw(lambda: Line(
            axes.coords_to_point(*point_coords(x_tracker.get_value(), -dx_tracker.get_value())),
            axes.coords_to_point(
                point_coords(x_tracker.get_value(), -dx_tracker.get_value())[0],
                point_coords(x_tracker.get_value(), dx_tracker.get_value())[1]
            ),
            color=GREEN
        ))
        run_line = always_redraw(lambda: Line(
            axes.coords_to_point(
                point_coords(x_tracker.get_value(), -dx_tracker.get_value())[0],
                point_coords(x_tracker.get_value(), dx_tracker.get_value())[1]
            ),
            axes.coords_to_point(*point_coords(x_tracker.get_value(), dx_tracker.get_value())),
            color=GREEN
        ))

        # Label area
        label_reference_point = axes.get_right() + RIGHT * 1.5

        delta_y_text = MathTex("\\Delta y = ", color=BLACK).scale(0.8)
        delta_y_val = DecimalNumber(0, num_decimal_places=2, color=BLACK).scale(0.8)
        delta_y_group = VGroup(delta_y_text, delta_y_val).arrange(RIGHT)

        delta_x_text = MathTex("\\Delta x = ", color=BLACK).scale(0.8)
        delta_x_val = DecimalNumber(0, num_decimal_places=2, color=BLACK).scale(0.8)
        delta_x_group = VGroup(delta_x_text, delta_x_val).arrange(RIGHT)

        slope_text = MathTex("Slope = \\frac{\\Delta y}{\\Delta x} = ", color=BLACK).scale(0.8)
        slope_val = DecimalNumber(0, num_decimal_places=2, color=BLACK).scale(0.8)
        slope_group = VGroup(slope_text, slope_val).arrange(RIGHT)

        label_group = VGroup(delta_y_group, delta_x_group, slope_group).arrange(DOWN, aligned_edge=LEFT)
        label_group.move_to(label_reference_point, aligned_edge=LEFT)

        # Create a green rectangle around the slope value
        box = SurroundingRectangle(slope_val, color=ORANGE, buff=0.1)
        box.add_updater(lambda m: m.become(SurroundingRectangle(slope_val, color=ORANGE, buff=0.1)))

        # Updaters for delta values and slope
        delta_y_val.add_updater(lambda m: m.set_value(
            point_coords(x_tracker.get_value(), dx_tracker.get_value())[1] -
            point_coords(x_tracker.get_value(), -dx_tracker.get_value())[1]
        ))
        delta_x_val.add_updater(lambda m: m.set_value(
            point_coords(x_tracker.get_value(), dx_tracker.get_value())[0] -
            point_coords(x_tracker.get_value(), -dx_tracker.get_value())[0]
        ))
        slope_val.add_updater(lambda m: m.set_value(
            get_slope(x_tracker.get_value())
        ))

        # Show everything except the box initially
        self.play(FadeIn(tangent_line, rise_line, run_line, label_group), run_time=1)
        self.wait(0.5)

        # Animate x changing and dx changing over time, and create the box
        self.play(
            x_tracker.animate.set_value(2.5),
            dx_tracker.animate.set_value(1.25),
            Create(box),
            run_time=3
        )
        self.wait(1)

        # Reverse the animation
        self.play(
            x_tracker.animate.set_value(-3),
            dx_tracker.animate.set_value(0.3),
            run_time=3
        )
        self.wait(1)
        self.play(FadeOut(box))
        

        
class CircleDemo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        mustard_circle = Circle(color="#E1AD0E")
        self.play(Create(mustard_circle))
        
        fixed_point = Dot(mustard_circle.point_at_angle(7 * PI / 4), color=DARK_BLUE)
        self.play(Create(fixed_point))
        
        self.wait(1)
        
        line_length = 2.0
        tangent_vector = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])
        tangent_line = Line(
            start=fixed_point.get_center() + line_length * tangent_vector,
            end=fixed_point.get_center() - line_length * tangent_vector,
            color=GRAY,
            stroke_width=2
        )
        
        self.play(Create(tangent_line))
        
        dotted_tangent_line = DashedVMobject(
            tangent_line,
            num_dashes=20
        )
        self.play(Transform(tangent_line, dotted_tangent_line))
        
        self.wait(1)
        
        moving_point = Dot(mustard_circle.point_at_angle(PI / 2), color=RED)
        self.play(Create(moving_point))
        
        secant_line = always_redraw(lambda: Line(
            fixed_point.get_center() - line_length * (moving_point.get_center() - fixed_point.get_center()) / np.linalg.norm(moving_point.get_center() - fixed_point.get_center()),
            moving_point.get_center() + line_length * (moving_point.get_center() - fixed_point.get_center()) / np.linalg.norm(moving_point.get_center() - fixed_point.get_center()),
            color=RED, stroke_width=2
        ))
        
        temp_secant = Line(fixed_point.get_center(), fixed_point.get_center(), color=RED, stroke_width=2)
        self.play(Transform(temp_secant, secant_line))
        self.remove(temp_secant)
        self.add(secant_line)
        
        def update_moving_point(dot, alpha):
            initial_angle = PI / 2
            target_angle = 7 * PI / 4
            
            diff = target_angle - initial_angle
            if diff > PI:
                diff -= 2 * PI
            elif diff < -PI:
                diff += 2 * PI
            
            target_alpha = 0.999 # Adjust this to change how close it gets.
            alpha = min(alpha, target_alpha)
            
            angle = initial_angle + alpha * diff
            dot.move_to(mustard_circle.point_at_angle(angle))
        
        self.play(
            UpdateFromAlphaFunc(moving_point, update_moving_point),
            run_time=3,
            rate_func=linear
        )

        self.wait(2)
        
        
        
        