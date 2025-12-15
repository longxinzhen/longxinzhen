import streamlit as st
from datetime import datetime
import base64
st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
# 设置页面配置
st.set_page_config(
    page_title="个人简历生成器",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 注入自定义样式
st.markdown("""
<style>
    .main-header {
        font-size: 24px;
        color: #1E88E5;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 18px;
        color: #263238;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 5px;
    }
    .resume-container {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        height: 100%;
    }
    .info-label {
        font-weight: bold;
        color: #546E7A;
    }
    .form-input {
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 页面标题
st.markdown('<h1 class="main-header">📄 个人简历生成器</h1>', unsafe_allow_html=True)

# 创建两列布局
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<h3 class="section-header">个人信息表单</h3>', unsafe_allow_html=True)
    
    # 基本信息
    name = st.text_input("姓名", "龙昕臻", key="name")
    
    # 联系信息
    phone = st.text_input("电话", "1377765438", key="phone")
    email = st.text_input("邮箱", "32811@qq.com", key="email")
    
    # 个人信息
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        gender = st.radio("性别", ["男", "女", "其他"], index=0)
    with col1_2:
        birth_date = st.date_input("出生日期", datetime(2001, 6, 7))
    
    education = st.selectbox("学历", ["本科", "专科", "硕士", "博士", "其他"], index=0)
    
    # 求职信息
    job_title = st.text_input("求职意向", "软件工程师", key="job_title")
    
    exp_years = st.slider("工作经验（年）", 0, 10, 3)
    salary_expect = st.slider("期望薪资（元/月）", 5000, 50000, 15000, step=1000)
    
    # 专业技能
    st.markdown('<h4 class="section-header">专业技能</h4>', unsafe_allow_html=True)
    
    skills = {}
    skill_cols = st.columns(2)
    with skill_cols[0]:
        skills["Python"] = st.slider("Python", 0, 100, 85)
        skills["HTML/CSS"] = st.slider("HTML/CSS", 0, 100, 75)
        skills["JavaScript"] = st.slider("JavaScript", 0, 100, 65)
    with skill_cols[1]:
        skills["Java"] = st.slider("Java", 0, 100, 60)
        skills["SQL"] = st.slider("SQL", 0, 100, 80)
        skills["机器学习"] = st.slider("机器学习", 0, 100, 50)
    
    # 个人简介
    st.markdown('<h4 class="section-header">个人简介</h4>', unsafe_allow_html=True)
    intro = st.text_area(
        "",
        "本人拥有3年软件开发经验，熟悉Python、Java等编程语言，具备良好的编程习惯和问题解决能力。曾参与多个大型项目的开发与维护，具有良好的团队协作精神和沟通能力。",
        height=100
    )
    
    # 项目经验
    st.markdown('<h4 class="section-header">项目经验</h4>', unsafe_allow_html=True)
    project = st.text_area(
        "",
        "1. 电商平台重构项目：负责后端API开发，使用Python Flask框架，优化了数据库查询，使系统响应速度提升30%。\n\n2. 数据分析平台：参与数据处理模块开发，使用Pandas和NumPy进行数据清洗和分析，为业务决策提供支持。",
        height=150
    )
    
    # 上传头像
    st.markdown('<h4 class="section-header">上传头像</h4>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("选择图片", type=["jpg", "jpeg", "png"])

with col2:
    st.markdown('<h3 class="section-header">简历实时预览</h3>', unsafe_allow_html=True)
    
    # 简历容器
    with st.container():
        st.markdown('<div class="resume-container">', unsafe_allow_html=True)
        
        # 顶部信息 - 姓名和头像
        header_col1, header_col2 = st.columns([3, 1])
        with header_col1:
            st.markdown(f'<h1 style="color:#1E88E5;">{name}</h1>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size:16px;">{job_title}</p>', unsafe_allow_html=True)
        with header_col2:
            if uploaded_file is not None:
                st.image(uploaded_file, width=120, caption="个人头像")
            else:
                # 使用默认头像
                st.image("https://picsum.photos/id/1005/120/120", width=120, caption="个人头像")
        
        # 基本信息
        st.markdown('<h4 class="section-header">基本信息</h4>', unsafe_allow_html=True)
        info_col1, info_col2 = st.columns(2)
        with info_col1:
            st.markdown(f'<p><span class="info-label">性别：</span>{gender}</p>', unsafe_allow_html=True)
            st.markdown(f'<p><span class="info-label">学历：</span>{education}</p>', unsafe_allow_html=True)
            st.markdown(f'<p><span class="info-label">工作经验：</span>{exp_years}年</p>', unsafe_allow_html=True)
        with info_col2:
            st.markdown(f'<p><span class="info-label">出生日期：</span>{birth_date.strftime("%Y-%m-%d")}</p>', unsafe_allow_html=True)
            st.markdown(f'<p><span class="info-label">期望薪资：</span>{salary_expect}元/月</p>', unsafe_allow_html=True)
            st.markdown(f'<p><span class="info-label">电话：</span>{phone}</p>', unsafe_allow_html=True)
            st.markdown(f'<p><span class="info-label">邮箱：</span>{email}</p>', unsafe_allow_html=True)
        
        # 个人简介
        st.markdown('<h4 class="section-header">个人简介</h4>', unsafe_allow_html=True)
        st.markdown(f'<p>{intro}</p>', unsafe_allow_html=True)
        
        # 专业技能
        st.markdown('<h4 class="section-header">专业技能</h4>', unsafe_allow_html=True)
        for skill, level in skills.items():
            st.markdown(f'<p>{skill}</p>', unsafe_allow_html=True)
            st.progress(level)
        
        # 项目经验
        st.markdown('<h4 class="section-header">项目经验</h4>', unsafe_allow_html=True)
        st.markdown(f'<p>{project.replace("\n", "<br>")}</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# 添加底部按钮
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    if st.button("下载简历 (PDF)"):
        st.info("PDF生成功能即将上线，敬请期待！")
with col_btn2:
    if st.button("重置表单"):
        st.experimental_rerun()
