"""
強め合う干渉（Constructive Interference）のアニメーション
2つの同位相の正弦波が重なり合って振幅が2倍になる様子を可視化
"""

from manim import *
import numpy as np


class ConstructiveInterference(Scene):
    def construct(self):
        # 背景を黒に設定
        self.camera.background_color = BLACK
        
        # タイトル
        title = Text("強め合う干渉", font_size=48, color=WHITE)
        title.to_edge(UP)
        subtitle = Text("同位相の2つの波", font_size=24, color=GRAY)
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
        
        # 波2（緑）
        wave2_func = lambda x: np.sin(x)  # 同位相
        wave2 = axes.plot(
            wave2_func,
            x_range=[0, 4 * PI],
            color=GREEN,
            stroke_width=2
        )
        wave2_label = Text("波2", font_size=24, color=GREEN)
        wave2_label.next_to(axes.c2p(4 * PI, wave2_func(4 * PI)), RIGHT)
        wave2_label.shift(DOWN * 0.5)
        
        # 波を描画
        self.play(
            Create(wave1),
            Create(wave2),
            Write(wave1_label),
            Write(wave2_label)
        )
        self.wait(1)
        
        # 合成波（赤）- 振幅が2倍
        combined_func = lambda x: wave1_func(x) + wave2_func(x)
        combined_wave = axes.plot(
            combined_func,
            x_range=[0, 4 * PI],
            color=RED,
            stroke_width=3
        )
        combined_label = Text("合成波（振幅2倍）", font_size=24, color=RED)
        combined_label.next_to(axes.c2p(4 * PI, combined_func(4 * PI)), RIGHT)
        
        # 元の波を薄くしてから合成波を表示
        self.play(
            wave1.animate.set_stroke(opacity=0.3),
            wave2.animate.set_stroke(opacity=0.3),
            FadeOut(wave1_label),
            FadeOut(wave2_label)
        )
        self.play(
            Create(combined_wave),
            Write(combined_label)
        )
        
        # 振幅の強調
        amplitude_arrow = DoubleArrow(
            axes.c2p(PI/2, 0),
            axes.c2p(PI/2, 2),
            color=YELLOW,
            buff=0
        )
        amplitude_text = Text("Amplitude = 2x", font_size=20, color=YELLOW)
        amplitude_text.next_to(amplitude_arrow, LEFT)
        
        self.play(
            GrowArrow(amplitude_arrow),
            Write(amplitude_text)
        )
        
        # アニメーション：波の動き
        self.wait(1)
        
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
                    lambda x: np.sin(x - t.get_value()),
                    x_range=[0, 4 * PI],
                    color=GREEN,
                    stroke_width=2,
                    stroke_opacity=0.3
                )
            )
        
        def update_combined(mob):
            mob.become(
                axes.plot(
                    lambda x: 2 * np.sin(x - t.get_value()),
                    x_range=[0, 4 * PI],
                    color=RED,
                    stroke_width=3
                )
            )
        
        wave1.add_updater(update_wave1)
        wave2.add_updater(update_wave2)
        combined_wave.add_updater(update_combined)
        
        # 波を右に移動させる
        self.play(t.animate.set_value(2 * PI), run_time=4, rate_func=linear)
        
        # アップデーターを削除
        wave1.clear_updaters()
        wave2.clear_updaters()
        combined_wave.clear_updaters()
        
        # 終了
        self.wait(1)
        
        # 説明テキスト
        explanation = Text(
            "位相が同じ → 振幅が足し算される",
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