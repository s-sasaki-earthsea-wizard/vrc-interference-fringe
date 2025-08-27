"""
弱め合う干渉（Destructive Interference）のアニメーション
位相が180度ずれた2つの正弦波が重なり合って打ち消し合う様子を可視化
"""

from manim import *
import numpy as np


class DestructiveInterference(Scene):
    def construct(self):
        # 背景を黒に設定
        self.camera.background_color = BLACK
        
        # タイトル
        title = Text("弱め合う干渉", font_size=48, color=WHITE)
        title.to_edge(UP)
        subtitle = Text("位相が逆の2つの波", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)
        
        # 座標軸の設定
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": GRAY, "include_numbers": False},
        )
        axes.center()
        axes.shift(DOWN * 0.5)
        
        # x軸のラベル
        x_label = Text("Position", font_size=20, color=GRAY)
        x_label.next_to(axes.x_axis, RIGHT)
        y_label = Text("Amplitude", font_size=20, color=GRAY)
        y_label.next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 波1（青）
        wave1_func = lambda x: np.sin(x)
        wave1 = axes.plot(
            wave1_func,
            x_range=[0, 4 * PI],
            color=BLUE,
            stroke_width=2
        )
        wave1_label = Text("波1", font_size=24, color=BLUE)
        wave1_label.next_to(axes.c2p(4 * PI, wave1_func(4 * PI)), RIGHT)
        
        # 波2（緑） - 位相が180度（π）ずれている
        wave2_func = lambda x: np.sin(x + PI)  # 位相が逆
        wave2 = axes.plot(
            wave2_func,
            x_range=[0, 4 * PI],
            color=GREEN,
            stroke_width=2
        )
        wave2_label = Text("波2（逆位相）", font_size=24, color=GREEN)
        wave2_label.next_to(axes.c2p(4 * PI, wave2_func(4 * PI)), RIGHT)
        
        # 波を描画
        self.play(
            Create(wave1),
            Create(wave2),
            Write(wave1_label),
            Write(wave2_label)
        )
        self.wait(1)
        
        # 位相差を強調（シンプルなテキストのみ）
        phase_text = Text("Phase Difference: 180°", font_size=24, color=ORANGE)
        phase_text.to_edge(UP).shift(DOWN * 1.5)
        
        self.play(Write(phase_text))
        self.wait(2)
        self.play(FadeOut(phase_text))
        
        # 合成波（赤）- 振幅が0
        combined_func = lambda x: wave1_func(x) + wave2_func(x)
        combined_wave = axes.plot(
            combined_func,
            x_range=[0, 4 * PI],
            color=RED,
            stroke_width=3
        )
        combined_label = Text("合成波（振幅0）", font_size=24, color=RED)
        combined_label.to_edge(RIGHT)
        combined_label.shift(DOWN)
        
        # 元の波を薄くしてから合成波を表示
        self.play(
            wave1.animate.set_stroke(opacity=0.3),
            wave2.animate.set_stroke(opacity=0.3),
            FadeOut(wave1_label),
            FadeOut(wave2_label)
        )
        
        # 合成波が0になることを示すライン
        zero_line = axes.plot(
            lambda x: 0,
            x_range=[0, 4 * PI],
            color=RED,
            stroke_width=3
        )
        
        self.play(
            Create(zero_line),
            Write(combined_label)
        )
        
        # 打ち消し合いの説明
        cancel_text1 = Text("山と谷が", font_size=24, color=YELLOW)
        cancel_text2 = Text("打ち消し合う", font_size=24, color=YELLOW)
        cancel_text1.move_to(axes.c2p(PI/2, 1.5))
        cancel_text2.next_to(cancel_text1, DOWN)
        
        # 山と谷を示す矢印
        peak_arrow = Arrow(
            axes.c2p(PI/2, 1.3),
            axes.c2p(PI/2, 0.7),
            color=BLUE,
            buff=0
        )
        valley_arrow = Arrow(
            axes.c2p(PI/2, -1.3),
            axes.c2p(PI/2, -0.7),
            color=GREEN,
            buff=0
        )
        
        self.play(
            Write(cancel_text1),
            Write(cancel_text2),
            GrowArrow(peak_arrow),
            GrowArrow(valley_arrow)
        )
        
        self.wait(1)
        
        # アニメーション：波の動き
        self.play(
            FadeOut(cancel_text1),
            FadeOut(cancel_text2),
            FadeOut(peak_arrow),
            FadeOut(valley_arrow)
        )
        
        # 波を動かす
        t = ValueTracker(0)
        
        def update_wave1(mob):
            mob.become(
                axes.plot(
                    lambda x: np.sin(x - t.get_value()),
                    x_range=[0, 4 * PI],
                    color=BLUE,
                    stroke_width=2,
                    stroke_opacity=0.3
                )
            )
        
        def update_wave2(mob):
            mob.become(
                axes.plot(
                    lambda x: np.sin(x + PI - t.get_value()),
                    x_range=[0, 4 * PI],
                    color=GREEN,
                    stroke_width=2,
                    stroke_opacity=0.3
                )
            )
        
        def update_combined(mob):
            mob.become(
                axes.plot(
                    lambda x: 0,  # 常に0
                    x_range=[0, 4 * PI],
                    color=RED,
                    stroke_width=3
                )
            )
        
        wave1.add_updater(update_wave1)
        wave2.add_updater(update_wave2)
        zero_line.add_updater(update_combined)
        
        # 波を右に移動させる
        self.play(t.animate.set_value(2 * PI), run_time=4, rate_func=linear)
        
        # アップデーターを削除
        wave1.clear_updaters()
        wave2.clear_updaters()
        zero_line.clear_updaters()
        
        # 終了
        self.wait(1)
        
        # 説明テキスト
        explanation = Text(
            "位相が逆 → 振幅が打ち消し合う",
            font_size=32,
            color=WHITE
        )
        explanation.to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)


if __name__ == "__main__":
    # コマンドライン実行用の設定
    from manim import config
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    config.background_color = BLACK