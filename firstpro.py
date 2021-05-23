from manim import *

class AlgebraProblem(Scene):
    def construct(self):
        problem_text = Tex("试求$x$的值", tex_template=TexTemplateLibrary.ctex).shift(3*UP)
        problem_tex = MathTex(
                "x", "+",  "\dfrac{x}{1+2}",  "+",  "\dfrac{x}{1+2+3}", "+",  "\cdots",   "+",  "\dfrac{x}{1+2+ \cdots + 4041}",  "=", "4041"
                )
        problem_tex2 = MathTex(
                "x", "+",  "\dfrac{x}{1+2}",  "+",  "\dfrac{x}{1+2+3}", "+",      "\cdots",   "+",  "\dfrac{x}{1+2+ \cdots + 4041}",  "=", "4041"
                ).to_edge(UP)
        problem_tex3 = MathTex(
                "x","(","\dfrac{1}{1}" , "+",  "\dfrac{1}{1+2}",  "+",  "\dfrac{1}{1+2+3}", "+", "\cdots",   "+",  "\dfrac{1}{1+2+ \cdots + 4041}",")"  "=", "4041"
                ).to_edge(UP)
        self.play(Write(problem_tex))
        self.wait()
        self.play(Write(problem_text))
        self.wait(3)
        self.play(FadeOutAndShift(problem_text, UP))

        self.play(ReplacementTransform(problem_tex, problem_tex2))
        self.wait(1)

        self.play(problem_tex2[0][0].animate.shift(problem_tex3[0][0].get_center() -  problem_tex2[0][0].get_center()))
        self.play(problem_tex2[2][0].animate.shift(problem_tex3[0][0].get_center() -  problem_tex2[2][0].get_center()))
        self.play(problem_tex2[4][0].animate.shift(problem_tex3[0][0].get_center() -  problem_tex2[4][0].get_center()))
        self.play(problem_tex2[8][0].animate.shift(problem_tex3[0][0].get_center() -  problem_tex2[8][0].get_center()))
        self.wait(1)

        self.play(ReplacementTransform(problem_tex2, problem_tex3))
        self.wait(2)

        funct = MathTex("\sum_{k=1}^{n}k=\dfrac{n(n+1)}{2}").set_color_by_gradient(BLUE, GREEN).scale(2)
        self.play(Create(funct))
        self.play(Indicate(funct))
        self.wait(2)
        self.play(Uncreate(funct))
        
        framebox0 = SurroundingRectangle(problem_tex3[2][2], buff = .1)
        framebox1 = SurroundingRectangle(problem_tex3[4][2:5], buff = .1)
        framebox2 = SurroundingRectangle(problem_tex3[6][2:7], buff = .1)
        framebox3 = SurroundingRectangle(problem_tex3[10][2:14], buff = .1)
        
        ar0 = Arrow(start=problem_tex3[2][2].get_center()+0.1*DOWN, end = problem_tex3[2][2].get_center()+2*DOWN, color=YELLOW)
        add0 = MathTex("\sum_{k=1}^{1}k").next_to(ar0, DOWN)
        ar02 = Arrow(start=add0.get_bottom() + 0.1*DOWN, end=add0.get_bottom()+2.1*DOWN, color=GREEN)
        add02 = MathTex("\dfrac{1\cdot2}{2}").next_to(ar02, DOWN)

        ar1 = Arrow(start=problem_tex3[4][2:5].get_center()+0.1*DOWN, end=problem_tex3[4][2:5].get_center()+2*DOWN, color=YELLOW)
        add1 = MathTex("\sum_{k=1}^{2}k").next_to(ar1, DOWN)
        ar12 = Arrow(start=add1.get_bottom()+0.1*DOWN, end=add1.get_bottom()+2.1*DOWN, color=GREEN)
        add12 = MathTex("\dfrac{2\cdot3}{2}").next_to(ar12, DOWN)

        ar2 = Arrow(start=problem_tex3[6][2:7].get_center()+0.1*DOWN, end=problem_tex3[6][2:7].get_center()+2*DOWN, color=YELLOW)
        add2 = MathTex("\sum_{k=1}^{3}k").next_to(ar2, DOWN)
        ar22 = Arrow(start=add2.get_bottom()+0.1*DOWN, end=add2.get_bottom()+2.1*DOWN, color=GREEN)
        add22 = MathTex("\dfrac{3\cdot4}{2}").next_to(ar22, DOWN)

        ar3 = Arrow(start=problem_tex3[10][2:14].get_center()+0.1*DOWN, end=problem_tex3[10][2:14].get_center()+2*DOWN, color=YELLOW)
        add3 = MathTex("\sum_{k=1}^{4041}k").next_to(ar3, DOWN)
        ar32 = Arrow(start=add3.get_bottom()+0.1*DOWN, end=add3.get_bottom()+2.1*DOWN, color=GREEN)
        add32 = MathTex("\dfrac{4041\cdot4042}{2}").next_to(ar32, DOWN)
         
        group_remove = VGroup()
        group_remove.add( framebox0, framebox1, framebox2, framebox3, ar0, ar02, ar1, ar12, ar2, ar22, ar3, ar32, add0, add1, add2, add3, add02, add12, add22, add32)

        self.play(Create(framebox0))
        self.play(Create(ar0))
        self.play(Write(add0))
        self.play(Create(ar02))
        self.play(Write(add02))
        self.wait()

        self.play(Create(framebox1))
        self.play(Create(ar1))
        self.play(Write(add1))
        self.play(Create(ar12))
        self.play(Write(add12))
        self.wait()
        
        self.play(Create(framebox2))
        self.play(Create(ar2))
        self.play(Write(add2))
        self.play(Create(ar22))
        self.play(Write(add22))
        self.wait()
        

        self.play(Create(framebox3))
        self.play(Create(ar3))
        self.play(Write(add3))
        self.play(Create(ar32))
        self.play(Write(add32))
        self.wait() 

        self.play(Uncreate(group_remove))
        self.wait()
        
        pframe1 = SurroundingRectangle(problem_tex3)
        self.play(Create(pframe1))
        arrow = Arrow(start=pframe1.get_bottom(), end=pframe1.get_bottom()+2*DOWN)
        problem_tex4 =MathTex(
                "x","(","\dfrac{2}{1\cdot2}" , "+",  "\dfrac{2}{2\cdot3}",  "+",  "\dfrac{2}{3\cdot4}", "+", "\cdots",   "+",  "\dfrac{2}{4041\cdot4042}",")"  "=", "4041"
                        ).next_to(arrow, DOWN)
        self.play(Create(arrow))
        self.play(Write(problem_tex4))
        self.wait()
        problem_tex5 = MathTex(
                "2x","(","\dfrac{1}{1\cdot2}" , "+",  "\dfrac{1}{2\cdot3}",  "+",  "\dfrac{1}{3\cdot4    }", "+", "\cdots",   "+",  "\dfrac{1}{4041\cdot4042}",")"  "=", "4041"
                ).to_edge(UP)
        self.play(Uncreate(arrow), run_time=0.5)
        self.play(Uncreate(pframe1), run_time=0.5)
        self.play(Unwrite(problem_tex3), run_time=0.5)
        self.play(ReplacementTransform(problem_tex4, problem_tex5))
        self.wait()
        funct2 = MathTex("\dfrac{1}{k(k+1)}=\dfrac{1}{k}-\dfrac{1}{k+1}").scale(2).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(funct2))
        self.play(Indicate(funct2))
        self.play(Unwrite(funct2))
        self.wait()
        
        pframe2 = SurroundingRectangle(problem_tex5)
        arrow2 = Arrow(start=pframe2.get_bottom(), end=pframe2.get_bottom()+2*DOWN)
        problem_tex6 = MathTex(
                "2x","(","\dfrac{1}{1}", "-" , "\dfrac{1}{2}" , "+",  "\dfrac{1}{2}", "-", "\dfrac{1}{3}",  "+",  "\dfrac{1}{3}", "-", "\dfrac{1}{4}", "+", "\cdots",   "+",  "\dfrac{1}{4041}", "-", "\dfrac{1}{4042}",")"  "=", "4041"
                    ).next_to(arrow2, DOWN)
        self.play(Create(pframe2))
        self.play(Create(arrow2))
        self.play(Write(problem_tex6))
        self.wait()
        
        line = Line().set_angle(PI/4).set_color(RED).move_to(problem_tex6[5].get_center()).set_stroke(color=RED, width=5)
        line2 = line.copy().move_to(problem_tex6[9].get_center())
        line3 = line.copy().move_to(problem_tex6[13].get_center())
        line4 = line.copy().move_to(problem_tex6[16].get_center())
        lineGroup = VGroup(line, line2, line3, line4)
        self.play(GrowFromCenter(lineGroup))
        self.wait()
        
        pframe3 = SurroundingRectangle(problem_tex6) 
        arrow3 = Arrow(start=pframe3.get_bottom(), end=pframe3.get_bottom()+2*DOWN).set_color_by_gradient(BLUE, GREEN)
        problem_tex7 = MathTex(
                "2x(1-\dfrac{1}{4042})=4041"
                ).next_to(arrow3, DOWN)
        self.play(Create(pframe3))
        self.play(Create(arrow3))
        self.play(Write(problem_tex7))
        self.wait()

        frameGroup = VGroup(pframe2, pframe3, arrow2, arrow3, problem_tex5, problem_tex6, line, line2, line3, line4)
        self.play(FadeOutAndShift(frameGroup, DOWN))
        problem_tex8 = MathTex(
                "2x\cdot\dfrac{4041}{4042}=4041"
                ).to_edge(UP)
        self.play(ReplacementTransform(problem_tex7, problem_tex8))
        self.wait()

        pframe4 = SurroundingRectangle(problem_tex8)
        arrow4 = Arrow(start=pframe4.get_bottom(), end=pframe4.get_bottom()+2*DOWN).set_color_by_gradient(BLUE, GREEN)
        problem_tex9 = MathTex("2x=4041\cdot\dfrac{4042}{4041}").next_to(arrow4, DOWN)
        problem_tex10 = MathTex("2x= 4042").next_to(arrow4, DOWN)
        problem_tex11 = MathTex("x=2021").next_to(problem_tex10, DOWN).scale(2).set_color_by_gradient(BLUE, GREEN)
        self.play(Create(pframe4))
        self.play(Create(arrow4))
        self.play(Write(problem_tex9))
        self.wait()
        self.play(ReplacementTransform(problem_tex9, problem_tex10))
        self.play(ReplacementTransform(problem_tex10, problem_tex11))
        self.wait()

        self.play(Uncreate(pframe4))
        #self.remove(arrow4)
        self.play(ReplacementTransform(problem_tex8, problem_tex))
        solve_text = Text("Problem Solved!", gradient=(YELLOW, GREEN)).to_edge(DOWN).scale(2)
        self.play(GrowFromCenter(solve_text))
        self.wait(2)

        lastGroup2 = VGroup(problem_tex, problem_tex11, solve_text, arrow4)
        self.play(FadeOutAndShift(lastGroup2, DOWN))

        thank_text = Text("谢谢观看!", gradient=(BLUE, GREEN)).scale(3)
        self.play(FadeInFromLarge(thank_text))
        self.wait(3)
     
