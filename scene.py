from manim import *

class SineToCosine(Scene):
    def construct(self):
        sine = FunctionGraph(
            lambda x: np.sin(x - 3 * PI),
            color=RED,
        )

        cosine = FunctionGraph(
            lambda x: np.cos(x + 3 * PI),
            color=BLUE,
        )

        self.play(FadeIn(sine))
        self.wait()

        self.play(Transform(sine, cosine))
        self.wait()

        self.play(FadeOut(sine))
        self.wait()


class ExpToLog(Scene):
    def construct(self):
        exp = FunctionGraph(
            lambda x: np.exp(x),
            color=RED,
        )

        log = FunctionGraph(
            lambda x: np.log(x),
            x_range=(0.01, 100),
            color=GREEN,
        )

        line = FunctionGraph(
            lambda x: x,
            color=BLUE,
        )

        self.play(FadeIn(exp))
        self.wait()

        self.play(Transform(exp, line))
        self.wait()

        self.play(Transform(exp, log))
        self.wait()

        self.play(FadeOut(exp))
        self.wait()