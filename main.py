from manim import *

class BeautifulIntro(Scene):
    def construct(self):
        title = Text("Manim Animation", font_size=72)
        subtitle = Text("Math + Code = Magic", font_size=36).next_to(title, DOWN)

        circle = Circle(color=BLUE).shift(LEFT * 3)
        square = Square(color=GREEN).shift(RIGHT * 3)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.5)

        self.play(Create(circle), Create(square))
        self.play(
            circle.animate.shift(RIGHT * 3),
            square.animate.shift(LEFT * 3),
            run_time=2
        )

        self.play(
            Transform(circle, square.copy()),
            FadeOut(square),
            FadeOut(title),
            FadeOut(subtitle),
        )

        final_text = Text("Beautiful Animations", font_size=60)
        self.play(Write(final_text))
        self.wait(2)
