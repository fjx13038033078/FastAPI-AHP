import os
import uuid
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.doctemplate import BaseDocTemplate
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

class PDFReportGenerator:
    def __init__(self):
        self.output_dir = "reports"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # 注册中文字体
        self._register_chinese_fonts()
    
    def _register_chinese_fonts(self):
        """注册中文字体"""
        try:
            # 尝试注册系统中的中文字体
            # Windows系统常见的中文字体路径
            chinese_fonts = [
                "C:/Windows/Fonts/simsun.ttc",  # 宋体
                "C:/Windows/Fonts/simhei.ttf",  # 黑体
                "C:/Windows/Fonts/msyh.ttc",    # 微软雅黑
                "C:/Windows/Fonts/simkai.ttf",  # 楷体
            ]
            
            for font_path in chinese_fonts:
                if os.path.exists(font_path):
                    if font_path.endswith('.ttc'):
                        # TTC字体需要指定子字体
                        pdfmetrics.registerFont(TTFont('SimSun', font_path, subfontIndex=0))
                        print(f"成功注册中文字体: {font_path}")
                        return 'SimSun'
                    else:
                        font_name = os.path.splitext(os.path.basename(font_path))[0]
                        pdfmetrics.registerFont(TTFont(font_name, font_path))
                        print(f"成功注册中文字体: {font_path}")
                        return font_name
            
            # 如果没有找到系统字体，尝试使用ReportLab内置的Unicode字体
            pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
            print("使用内置中文字体: STSong-Light")
            return 'STSong-Light'
            
        except Exception as e:
            print(f"字体注册失败: {e}")
            # 使用默认字体，可能会显示为方框
            return 'Helvetica'
    
    def _get_chinese_font(self):
        """获取可用的中文字体名称"""
        try:
            # 检查已注册的字体
            available_fonts = pdfmetrics.getRegisteredFontNames()
            
            # 优先选择的字体顺序
            preferred_fonts = ['SimSun', 'simhei', 'msyh', 'STSong-Light']
            
            for font in preferred_fonts:
                if font in available_fonts:
                    return font
            
            # 如果都没有，返回第一个中文字体或默认字体
            for font in available_fonts:
                if any(name in font for name in ['SimSun', 'Song', 'Hei', 'STSong']):
                    return font
            
            return 'Helvetica'
        except:
            return 'Helvetica'
    
    def generate_risk_report(self, data):
        """生成风险评估PDF报告"""
        # 生成唯一文件名
        filename = f"risk_report_{uuid.uuid4().hex[:12]}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        
        # 获取中文字体名称
        chinese_font = self._get_chinese_font()
        print(f"使用字体: {chinese_font}")
        
        # 创建PDF文档
        doc = SimpleDocTemplate(
            filepath, 
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        story = []
        
        # 获取样式
        styles = getSampleStyleSheet()
        
        # 自定义样式 - 使用中文字体
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=styles['Normal'],
            fontSize=12,
            alignment=0,  # 左对齐
            spaceAfter=6,
            fontName=chinese_font
        )
        
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Title'],
            fontSize=20,
            spaceAfter=3*cm,
            spaceBefore=6*cm,
            alignment=1,  # 居中
            fontName=chinese_font
        )
        
        date_style = ParagraphStyle(
            'DateStyle',
            parent=styles['Normal'],
            fontSize=14,
            spaceAfter=3*cm,
            alignment=1,  # 居中
            fontName=chinese_font
        )
        
        table_style = ParagraphStyle(
            'TableStyle',
            parent=styles['Normal'],
            fontSize=12,
            alignment=1,  # 居中
            fontName=chinese_font
        )
        
        section_style = ParagraphStyle(
            'SectionStyle',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            spaceBefore=20,
            fontName=chinese_font
        )
        
        content_style = ParagraphStyle(
            'ContentStyle',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=8,
            leftIndent=0.5*cm,
            fontName=chinese_font
        )
        
        # ==================== 封面页 ====================
        # 使用表格来实现精确的布局控制
        header_layout_table = Table([
            ["密级：××★××", "安全风险等级："],
            ["编号：", ""]
        ], colWidths=[8*cm, 8*cm], rowHeights=[0.8*cm, 0.8*cm])
        
        header_layout_table.setStyle(TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),   # 左列左对齐
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),  # 右列右对齐
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            # 移除所有边框
            ('BOX', (0, 0), (-1, -1), 0, colors.white),
            ('INNERGRID', (0, 0), (-1, -1), 0, colors.white),
        ]))
        story.append(header_layout_table)
        
        # 主标题
        story.append(Paragraph("安全风险评估报告", title_style))
        
        # 日期
        current_date = datetime.now()
        date_line = f"{current_date.year}&nbsp;&nbsp;&nbsp;&nbsp;年&nbsp;&nbsp;&nbsp;&nbsp;{current_date.month}&nbsp;&nbsp;&nbsp;&nbsp;月&nbsp;&nbsp;&nbsp;&nbsp;{current_date.day}&nbsp;&nbsp;&nbsp;&nbsp;日"
        story.append(Paragraph(date_line, date_style))
        
        # 底部表格
        bottom_table_data = [
            ["评估单位", data.get("dwmc", ""), "评估时间", data.get("report_time", "")],
            ["任务名称", data.get("rwmc", ""), "", ""]
        ]
        bottom_table = Table(bottom_table_data, colWidths=[3*cm, 5*cm, 3*cm, 5*cm])
        bottom_table.setStyle(TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
            ('SPAN', (1, 1), (3, 1)),  # 合并任务名称列
        ]))
        story.append(bottom_table)
        
        # 分页
        story.append(PageBreak())
        
        # ==================== 内容页 ====================
        
        # 一、评估依据
        story.append(Paragraph("一、评估依据", section_style))
        story.append(Paragraph("（列举评估所依据的相关法律法规和标准等）", content_style))
        story.append(Spacer(1, 2*cm))
        
        # 二、评估内容描述
        story.append(Paragraph("二、评估内容描述", section_style))
        story.append(Spacer(1, 2*cm))
        
        # 三、评估程序和方法
        story.append(Paragraph("三、评估程序和方法", section_style))
        story.append(Spacer(1, 2*cm))
        
        # 四、评估分析及对策建议
        story.append(Paragraph("四、评估分析及对策建议", section_style))
        
        # 为每个风险指标创建单独的评估表格
        for idx, (indicator_name, risk_info) in enumerate(data.get("detail", {}).items(), 1):
            # 创建单个风险点的评估表格
            risk_data = [
                ["", "风险点", ""],
                ["", "风险情况描述", ""],
                ["", "", "可能性等级"],
                [str(idx), "风险分析结论", "危害程度等级"],
                ["", "", "安全风险等级"],
                ["", "对策建议", ""]
            ]
            
            # 填入实际数据
            risk_data[0][2] = ""  # 风险点标题留空
            risk_data[1][1] = f"{indicator_name}"  # 风险情况描述
            risk_data[1][2] = risk_info[6]  # 指标说明
            risk_data[2][2] = risk_info[0]  # 可能性等级
            risk_data[3][2] = risk_info[1]  # 危害程度等级
            risk_data[4][2] = risk_info[3]  # 安全风险等级
            risk_data[5][1] = risk_info[4]  # 对策建议
            
            # 创建表格
            risk_table = Table(risk_data, colWidths=[1*cm, 12*cm, 3*cm])
            risk_table.setStyle(TableStyle([
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('FONTNAME', (0, 0), (-1, -1), chinese_font),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
                # 合并单元格
                ('SPAN', (0, 0), (0, 5)),  # 第一列数字列
                ('SPAN', (1, 0), (2, 0)),  # 风险点标题行
                ('SPAN', (1, 5), (2, 5)),  # 对策建议行
                # 背景色
                ('BACKGROUND', (1, 0), (2, 0), colors.lightgrey),
                ('BACKGROUND', (1, 1), (1, 1), colors.lightgrey),
                ('BACKGROUND', (1, 2), (1, 4), colors.lightgrey),
                ('BACKGROUND', (1, 5), (2, 5), colors.lightgrey),
            ]))
            
            story.append(risk_table)
            story.append(Spacer(1, 0.5*cm))
        
        # 五、评估结论
        story.append(Paragraph("五、评估结论", section_style))
        conclusion_text = f"（明确安全风险等级，可能发生事故的关键环节和关键部位等，并提出继续组织活动或者执行任务的建议，或者提出取消以及理由）<br/><br/>经评估，总体安全风险等级为：<b>{data.get('level', '')}</b>"
        story.append(Paragraph(conclusion_text, content_style))
        
        # 分页到签字页
        story.append(PageBreak())
        
        # ==================== 签字页 ====================
        story.append(Spacer(1, 8*cm))
        
        # 创建右对齐的签字样式
        right_align_style = ParagraphStyle(
            'RightAlignStyle',
            parent=styles['Normal'],
            fontSize=11,
            alignment=2,  # 右对齐
            spaceAfter=8,
            fontName=chinese_font
        )
        
        # 组长签字（右对齐，签字在上方，日期在下方）
        leader_signature = "组长（签字）：_______________"
        leader_date = "年&nbsp;&nbsp;&nbsp;&nbsp;月&nbsp;&nbsp;&nbsp;&nbsp;日"
        
        story.append(Paragraph(leader_signature, right_align_style))
        story.append(Paragraph(leader_date, right_align_style))
        story.append(Spacer(1, 2*cm))
        
        # 六、业务主管部门意见
        story.append(Paragraph("六、业务主管部门意见", section_style))
        story.append(Spacer(1, 4*cm))
        
        # 签字（盖章）（右对齐，签字在上方，日期在下方）
        department_signature = "签字（盖章）：_______________"
        department_date = "年&nbsp;&nbsp;&nbsp;&nbsp;月&nbsp;&nbsp;&nbsp;&nbsp;日"
        
        story.append(Paragraph(department_signature, right_align_style))
        story.append(Paragraph(department_date, right_align_style))
        
        # 生成PDF
        doc.build(story)
        
        return filepath 