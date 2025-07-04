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
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.platypus.flowables import Flowable


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
        
        # 创建PDF文档 - 使用BaseDocTemplate以便自定义页面模板
        doc = BaseDocTemplate(
            filepath, 
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        
        # 创建自定义页面模板，在每页绘制边框
        def draw_page_border(canvas, doc):
            """在每页绘制页面边框的函数"""
            canvas.saveState()
            canvas.setStrokeColor(colors.black)
            canvas.setLineWidth(1)
            
            # 计算边框位置（考虑页边距）
            margin = 2*cm
            page_width = A4[0] - 2*margin  # 17cm
            page_height = A4[1] - 2*margin  # 25.7cm
            
            # 绘制页面边框
            canvas.rect(margin, margin, page_width, page_height, stroke=1, fill=0)
            canvas.restoreState()
        
        # 创建内容框架 - 移除左右内边距，让表格能真正达到页面边框
        content_frame = Frame(
            2*cm, 2*cm, 17*cm, 25.7*cm,
            leftPadding=0, rightPadding=0,
            topPadding=12, bottomPadding=0,  # 移除底部内边距
            id='content_frame'
        )
        
        # 创建页面模板
        page_template = PageTemplate(
            id='bordered_page',
            frames=[content_frame],
            onPage=draw_page_border
        )
        
        # 将页面模板添加到文档
        doc.addPageTemplates([page_template])
        story = []
        
        # 注释：页面内容宽度为17cm（A4宽度21cm - 左右边距各2cm）
        
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
            spaceAfter=2*cm,  # 减少标题后空白
            spaceBefore=4*cm,  # 减少标题前空白
            alignment=1,  # 居中
            fontName=chinese_font
        )
        
        date_style = ParagraphStyle(
            'DateStyle',
            parent=styles['Normal'],
            fontSize=14,
            spaceAfter=1*cm,  # 减少日期后空白
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
            leftIndent=12,   # 12pt左缩进
            rightIndent=12,  # 12pt右缩进
            fontName=chinese_font
        )
        
        content_style = ParagraphStyle(
            'ContentStyle',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=8,
            leftIndent=12,   # 12pt左缩进
            rightIndent=12,  # 12pt右缩进
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
        date_line = f"{current_date.year}&nbsp;年&nbsp;{current_date.month}&nbsp;月&nbsp;{current_date.day}&nbsp;日"
        story.append(Paragraph(date_line, date_style))
        
        # 计算剩余空间，让底部表格贴到页面底部
        # 页面总高度 - 顶部边距 - 头部表格高度 - 标题高度 - 日期高度 - 底部表格高度
        # A4高度：29.7cm，减去上下边距各2cm = 25.7cm可用高度
        # 调整后已用高度：头部表格(2cm) + 标题空白(4cm) + 标题(2cm) + 日期空白(2cm) + 日期(1cm) = 11cm
        # 底部表格高度约2cm，所以需要的spacer = 25.7 - 11 - 2 = 12.7cm
        remaining_space = 25.7*cm - 11*cm - 2*cm  # 约12.7cm
        story.append(Spacer(1, remaining_space))
        
        # 底部表格 - 使用页面全宽，让左右边框与页面边框重合
        bottom_table_data = [
            ["评估单位", data.get("dwmc", ""), "评估时间", data.get("report_time", "")],
            ["任务名称", data.get("rwmc", ""), "", ""]
        ]
        # 计算页面内容宽度：A4宽度(21cm) - 左右边距(各2cm) = 17cm
        content_width = 17*cm
        # 均分表格列宽，让表格填满整个内容宽度
        col_width = content_width / 4  # 4列均分
        bottom_table = Table(bottom_table_data, colWidths=[col_width, col_width, col_width, col_width])
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
        
        # ==================== 第2页：前三部分 ====================
        
        # 页面可用高度：25.7cm，每部分分配约8.5cm
        section_height = 25.7*cm / 3  # 每部分约8.5cm
        
        # 创建第1,2,3部分的内容 - 每部分各占页面的1/3
        sections_123_content = []
        
        # 一、评估依据 - 占页面1/3
        sections_123_content.extend([
            [Paragraph("一、评估依据", section_style)],
            [Paragraph("（列举评估所依据的相关法律法规和标准等）", content_style)],
            [Spacer(1, section_height - 3*cm)]  # 填充到1/3页面高度
        ])
        
        # 二、评估内容描述 - 占页面1/3
        sections_123_content.extend([
            [Paragraph("二、评估内容描述", section_style)],
            [Spacer(1, section_height - 2*cm)]  # 填充到1/3页面高度
        ])
        
        # 三、评估程序和方法 - 占页面1/3
        sections_123_content.extend([
            [Paragraph("三、评估程序和方法", section_style)],
            [Spacer(1, section_height - 2*cm)]  # 填充到1/3页面高度
        ])
        
        # 创建第1,2,3部分的表格
        sections_123_table = Table(sections_123_content, colWidths=[17*cm])
        sections_123_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            
            # 在各部分之间添加分隔线
            ('LINEBELOW', (0, 2), (-1, 2), 0.5, colors.black),   # 一、之后的分隔线
            ('LINEBELOW', (0, 4), (-1, 4), 0.5, colors.black),   # 二、之后的分隔线  
        ]))
        
        story.append(sections_123_table)
        
        # 分页到第四部分
        story.append(PageBreak())
        
        # ==================== 第3页及后续：第四部分（可变长度） ====================
        
        # 四、评估分析及对策建议 - 可变长度内容
        section_four_content = []
        
        # 添加标题
        section_four_content.append([Paragraph("四、评估分析及对策建议", section_style)])
        
        # 生成风险表格内容
        details = data.get("detail", {})
        if details:
            for idx, (indicator_name, risk_info) in enumerate(details.items(), 1):
                # 创建单个风险点的评估表格 - 采用更清晰的布局
                risk_data = [
                    ["", "风险点"],
                    [str(idx), indicator_name],  # 风险点名称
                    ["", f"风险分析结论"],
                    ["", f"可能性等级: {risk_info[0]}"],
                    ["", f"危害程度等级: {risk_info[1]}"],
                    ["", f"安全风险等级: {risk_info[3]}"],
                    ["", "对策建议"],
                    ["", risk_info[4]]  # 对策建议内容
                ]
                
                # 创建表格 - 使用页面内容宽度，让左右边框与页面边框重合
                # 页面内容宽度：A4宽度(21cm) - 左右边距(各2cm) = 17cm
                page_content_width = 17*cm
                risk_table = Table(risk_data, colWidths=[1.5*cm, page_content_width-1.5*cm])
                risk_table.setStyle(TableStyle([
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('FONTNAME', (0, 0), (-1, -1), chinese_font),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    
                    # 设置清晰的边框和网格线
                    ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
                    ('INNERGRID', (0, 0), (-1, -1), 0.75, colors.black),
                    
                    # 合并单元格
                    ('SPAN', (0, 0), (0, 1)),  # 合并序号列的前两行
                    ('SPAN', (0, 2), (0, 5)),  # 合并序号列的风险分析行
                    ('SPAN', (0, 6), (0, 7)),  # 合并序号列的对策建议行
                    
                    # 设置背景色
                    ('BACKGROUND', (0, 0), (1, 0), colors.lightgrey),  # 风险点标题行
                    ('BACKGROUND', (0, 2), (1, 2), colors.lightgrey),  # 风险分析结论标题行
                    ('BACKGROUND', (0, 6), (1, 6), colors.lightgrey),  # 对策建议标题行
                    
                    # 设置字体加粗
                    ('FONTWEIGHT', (0, 0), (1, 0), 'BOLD'),  # 风险点标题
                    ('FONTWEIGHT', (0, 2), (1, 2), 'BOLD'),  # 风险分析结论标题
                    ('FONTWEIGHT', (0, 6), (1, 6), 'BOLD'),  # 对策建议标题
                    
                    # 设置对齐方式
                    ('ALIGN', (0, 0), (0, -1), 'CENTER'),  # 序号列居中
                    ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),  # 序号列垂直居中
                    
                    # 设置内边距，确保内容不贴边
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                    ('LEFTPADDING', (0, 0), (0, -1), 4),  # 序号列左边距
                    ('RIGHTPADDING', (0, 0), (0, -1), 4), # 序号列右边距
                    ('LEFTPADDING', (1, 1), (1, 1), 12),  # 风险点名称左缩进
                    ('LEFTPADDING', (1, 3), (1, 5), 20),  # 风险等级信息左缩进
                    ('LEFTPADDING', (1, 7), (1, 7), 12),  # 对策建议内容左缩进
                ]))
                
                section_four_content.append([risk_table])
                if idx < len(details):  # 如果不是最后一个，添加间距
                    section_four_content.append([Spacer(1, 0.4*cm)])
        else:
            # 如果没有指标数据，显示提示信息
            section_four_content.append([Paragraph("暂无风险点数据", content_style)])
        
        # 创建第四部分的表格
        section_four_table = Table(section_four_content, colWidths=[17*cm])
        section_four_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        
        # 设置表格跨页属性
        section_four_table.splitByRow = 1
        section_four_table.repeatRows = 0
        section_four_table.spaceAfter = 0
        section_four_table.spaceBefore = 0
        
        story.append(section_four_table)
        
        # 分页到第五部分
        story.append(PageBreak())
        
        # ==================== 第五部分页：第五部分占上半页 ====================
        
        # 页面可用高度：25.7cm，第五部分占上半页（约12.8cm）
        section_five_height = 25.7*cm / 2
        
        # 创建第五部分内容
        section_five_content = [
            [Paragraph("五、评估结论", section_style)],
            [Paragraph(f"（明确安全风险等级，可能发生事故的关键环节和关键部位等，并提出继续组织活动或者执行任务的建议，或者提出取消以及理由）<br/><br/>经评估，总体安全风险等级为：<b>{data.get('level', '')}</b>", content_style)],
            [Spacer(1, section_five_height - 6*cm)]  # 填充到页面上半部分
        ]
        
        # 创建第五部分的表格
        section_five_table = Table(section_five_content, colWidths=[17*cm])
        section_five_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        
        # 创建右对齐的签字样式
        right_align_style = ParagraphStyle(
            'RightAlignStyle',
            parent=styles['Normal'],
            fontSize=11,
            alignment=2,  # 右对齐
            spaceAfter=8,
            leftIndent=12,   # 12pt左缩进
            rightIndent=12,  # 12pt右缩进
            fontName=chinese_font
        )
        
        # 第六部分内容 - 占页面下半部分（约12.8cm）
        section_six_content = [
            [Paragraph("组长（签字）：_______________", right_align_style)],
            [Paragraph("年&nbsp;&nbsp;&nbsp;月&nbsp;&nbsp;&nbsp;日", right_align_style)],
            [Spacer(1, 0.5*cm)],  # 小间距
            [Paragraph("六、业务主管部门意见", section_style)],
            [Spacer(1, 2*cm)],  # 意见填写空间
            [Spacer(1, section_five_height - 8*cm)],  # 填充剩余空间，推送签字到底部
            [Paragraph("签字（盖章）：_______________", right_align_style)],
            [Paragraph("年&nbsp;&nbsp;&nbsp;月&nbsp;&nbsp;&nbsp;日", right_align_style)]
        ]
        
        # 创建第六部分的表格
        section_six_table = Table(section_six_content, colWidths=[17*cm])
        section_six_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            
            # 在第六部分标题"六、业务主管部门意见"上方添加分隔线，区分第五部分和第六部分
            ('LINEABOVE', (0, 3), (-1, 3), 0.5, colors.black),
        ]))
        
        # 将第五部分和第六部分合并到一个页面中
        story.append(section_five_table)
        story.append(section_six_table)
        
        # 生成PDF
        doc.build(story)
        
        return filepath 