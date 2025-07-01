"""
测试PDF签字部分布局
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.pdf_generator import PDFReportGenerator

def test_pdf_signature():
    """测试PDF签字部分的布局"""
    print("=== 测试PDF签字部分布局 ===")
    
    # 创建测试数据
    test_data = {
        "level": "较大",
        "detail": {
            "岗位种类是否齐全": [
                "2", "2", "4", "一般",
                "1.确定缺失哪类岗位\n2.补充缺失的岗位人员",
                "人员因素-岗位-岗位种类是否齐全",
                "管理干部、库房管理员、作业人员、警戒员、安全员、驾驶员是否齐全",
                1, 1
            ],
            "主要岗位任职年限是否超5年": [
                "2", "2", "4", "一般",
                "1.确定主要岗位任职年限\n2.更换主要岗位人员为5年以上",
                "人员因素-岗位-主要岗位任职年限是否超5年",
                "主要岗位任职年限是否超5年",
                2, 1
            ]
        },
        "report_time": "2025-07-01",
        "rwmc": "PDF签字测试任务",
        "dwmc": "测试单位"
    }
    
    # 生成PDF
    generator = PDFReportGenerator()
    pdf_path = generator.generate_risk_report(test_data)
    
    print(f"✓ PDF生成成功: {pdf_path}")
    print("请检查PDF文件中的签字部分是否符合要求：")
    print("1. 组长签字部分位于页面右侧")
    print("2. 签字在上方，日期在下方")
    print("3. 业务主管部门意见的签字部分也位于页面右侧")
    print("4. 签字在上方，日期在下方")
    
    return pdf_path

if __name__ == "__main__":
    test_pdf_signature() 