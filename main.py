from manim import *

class BeautifulIntro(Scene):
    def construct(self):
        # ===== OPENING: PROJECT TITLE =====
        main_title = Text("Maths & CS Algorithm", font_size=56, weight=BOLD)
        main_subtitle = Text("Visualizations", font_size=64, weight=BOLD, color=BLUE)
        main_subtitle.next_to(main_title, DOWN, buff=0.3)
        
        title_group = VGroup(main_title, main_subtitle)
        
        self.play(Write(main_title), run_time=1.5)
        self.play(Write(main_subtitle), run_time=1.5)
        self.wait(0.8)
        
        # ===== TAGLINE =====
        tagline = Text('"Seeing is Understanding"', font_size=36, color=YELLOW, slant=ITALIC)
        tagline.next_to(title_group, DOWN, buff=0.7)
        
        self.play(FadeIn(tagline, shift=UP))
        self.wait(1.2)
        
        self.play(
            FadeOut(title_group),
            FadeOut(tagline)
        )
        self.wait(0.5)
        
        # ===== VISION SECTION =====
        vision_title = Text("Project Vision", font_size=52, weight=BOLD, color=GREEN)
        self.play(Write(vision_title))
        self.wait(0.5)
        self.play(vision_title.animate.to_edge(UP))
        
        # Math Visualization
        math_text = Text("Visualize Mathematical Concepts", font_size=32)
        math_text.shift(UP * 1.5)
        
        math_icons = VGroup(
            Circle(radius=0.5, color=BLUE).shift(LEFT * 4),
            Square(side_length=0.9, color=PURPLE).shift(LEFT * 2.5),
            Triangle(color=RED).scale(0.6).shift(LEFT * 1),
            RegularPolygon(6, color=ORANGE).scale(0.5).shift(RIGHT * 0.5),
        )
        math_icons.shift(UP * 0.5)
        
        self.play(FadeIn(math_text, shift=DOWN))
        self.play(LaggedStart(*[Create(icon) for icon in math_icons], lag_ratio=0.2))
        self.wait(0.8)
        
        # CS Algorithms
        cs_text = Text("Animate CS Algorithms", font_size=32)
        cs_text.shift(DOWN * 1)
        
        # Sorting visualization bars
        bars = VGroup(*[
            Rectangle(height=0.3 + i*0.3, width=0.4, color=BLUE, fill_opacity=0.7)
            for i in range(5)
        ]).arrange(RIGHT, buff=0.2).shift(DOWN * 2)
        
        self.play(FadeIn(cs_text, shift=DOWN))
        self.play(LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.1))
        
        # Animate sorting
        self.play(
            bars[4].animate.shift(LEFT * 1.6),
            bars[3].animate.shift(LEFT * 0.6),
            bars[2].animate.shift(RIGHT * 0.2),
            bars[1].animate.shift(RIGHT * 0.8),
            bars[0].animate.shift(RIGHT * 1.6),
            run_time=1.5
        )
        self.wait(0.8)
        
        # Clear vision section
        self.play(
            FadeOut(vision_title),
            FadeOut(math_text),
            FadeOut(math_icons),
            FadeOut(cs_text),
            FadeOut(bars)
        )
        self.wait(0.5)
        
        # ===== TARGET AUDIENCE =====
        audience_title = Text("Built For", font_size=48, weight=BOLD, color=PINK)
        audience_title.to_edge(UP)
        
        audience_items = VGroup(
            Text("🎓 Students", font_size=36),
            Text("👩‍🏫 Educators", font_size=36),
            Text("💻 Developers", font_size=36),
            Text("🧠 Visual Learners", font_size=36)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(audience_title))
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT) for item in audience_items], lag_ratio=0.3))
        self.wait(1.5)
        
        self.play(
            FadeOut(audience_title),
            FadeOut(audience_items)
        )
        self.wait(0.5)
        
        # ===== OPEN SOURCE MESSAGE =====
        opensource_title = Text("Open Source Learning", font_size=52, weight=BOLD, color=TEAL)
        opensource_subtitle = Text("Community Driven • Visual Education", font_size=32, color=GRAY)
        opensource_subtitle.next_to(opensource_title, DOWN, buff=0.4)
        
        self.play(Write(opensource_title))
        self.play(FadeIn(opensource_subtitle))
        self.wait(1.5)
        
        self.play(
            FadeOut(opensource_title),
            FadeOut(opensource_subtitle)
        )
        self.wait(0.5)
        
        # ===== FINAL MESSAGE =====
        final_line1 = Text("Making Maths & Algorithms", font_size=42)
        final_line2 = Text("Beautiful, Visual & Intuitive", font_size=48, weight=BOLD, color=BLUE)
        final_line2.next_to(final_line1, DOWN, buff=0.4)
        
        final_group = VGroup(final_line1, final_line2)
        
        self.play(FadeIn(final_line1, shift=UP))
        self.play(Write(final_line2))
        self.wait(1)
        
        # Closing animation with shapes
        closing_shapes = VGroup(
            Circle(radius=0.4, color=BLUE, fill_opacity=0.5),
            Square(side_length=0.7, color=GREEN, fill_opacity=0.5),
            Triangle(color=RED, fill_opacity=0.5).scale(0.5),
        ).arrange(RIGHT, buff=1).shift(DOWN * 1.5)
        
        self.play(LaggedStart(*[Create(shape) for shape in closing_shapes], lag_ratio=0.2))
        self.play(
            Rotate(closing_shapes[0], angle=2*PI),
            closing_shapes[1].animate.scale(1.3),
            closing_shapes[2].animate.shift(UP * 0.5 + DOWN * 0.5),
            run_time=2
        )
        
        # Final tagline
        final_tagline = Text("Let's Learn Together 🚀✨", font_size=40, color=YELLOW)
        final_tagline.shift(DOWN * 2.8)
        
        self.play(FadeIn(final_tagline, shift=UP))
        self.wait(2)
        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)
