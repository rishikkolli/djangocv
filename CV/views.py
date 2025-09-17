from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rishik_cv(request):
    details = {
        "first_name" : "Rishik",
        "last_name" : "Kolli",
        "city_state" : "Brooklyn, New York",
        "phone_number" : "480-238-3232",
        "email" : "rk5129@nyu.edu",
        "linkedin" : "https://www.linkedin.com/in/rishikkolli",
        "sections": ["EDUCATION", "PROFESSIONAL EXPERIENCE", "ACADEMIC AND PROJECT EXPERIENCE", "SKILLS"],
        "companies_projectnames_typeofskill": ["CommonSpirit Health", "DocYou Enterprises LLC", "CSAA Insurance Group, a AAA Insurer", "State Farm", "Computer Science Malware Classification Capstone Project: ProDefense", "American Statistical Assocation Datafest Competition", "Washington Nationals MLB Predictive Regression Project", "Programming Languages", "OS/Database/Cloud Tools", "Skills"],
        "role": ["Associate Product Data Engineer", "React Native Developer and Software Team Lead", "Data Science Research Intern", "Cloud Software Engineer Intern", "Data Scientist"],
        "educations": [
            {
                "name": " New York University",
                "location": "Brooklyn, NY",
                "degree": "M.S. in Computer Science (GPA 4.0)",
                "date": "August 2025 - Present"
            },
            {
                "name": "Arizona State University",
                "location": "Tempe, AZ",
                "degree": "B.S. in Computer Science (GPA 3.82)",
                "date": "August 2020 - April 2024"
            }
        ],
        "experiences": [
            {
                "company": "CommonSpirit Health",
                "city": "Phoenix, AZ",
                "position": "Associate Product Data Engineer",
                "date": "June 2024 - Present",
                "bullet_points": ["Led the migration of databases and automation of scripts for nursing acute care dashboards in Tableau, transitioning from SAS to MySQL through Google BigQuery and Apache Airflow, enhancing system efficiency and mitigating data redundancy", "Migrated financial dashboards from Tableau to Qlik, integrating advanced features like drill-down dimensions and set analysis while automating data refresh schedules and configuring regional, role-based access for enhanced usability and security", "Building a new Clinical Health KPI dashboard in Looker Core/ML, leveraging advanced features such as custom LookML views, dynamic filtering, and cross-source joins to deliver actionable insights on patient outcomes and operational efficiency"],
            },
            {
                "company": "DocYou Enterprises LLC",
                "city": "Phoenix, AZ",
                "position": "React Native Developer and Software Team Lead",
                "date": "August 2022 - May 2024",
                "bullet_points": ["Constructed a dynamic web and mobile applications using React Native, PHP, and Firebase for residents to achieve ACGME accreditation, winning $16,500 at pitch competitions for future security enhancements and integration within hospitals", "Integrated visualization tools within the web application for residential supervisors to gain comprehensive insights into procedure logging, accounting for on average 20 residents, using JavaScript’s D3 and Plotly"]
            },
            {
                "company": "CSAA Insurance Group, a AAA Insurer",
                "city": "Glendale, AZ",
                "position": "Data Science Research Intern",
                "date": "May 2023 - July 2023",
                "bullet_points": ["Developed unconstrained loss models (ULM) to improve predictability of frequency and severity for different auto exposures in CSAA’s 40,861 zip codes on a three-year rolling average between 2019-2022 using AWS Sagemaker", "Aggregated neighboring zip code features from external Highway Loss Data Institute (HLDI) that accounts for 80% of private passenger market in the US to improve model performance by 2.31% compared with internal claims data", "Won 1st place in an internal innovation showcase exploring the use of smart home telematic systems to reduce water severity in Northern California home claims which accounts for 38% and 800 million of company-wide net paid losses"]
            },
            {
                "company": "State Farm",
                "city": "Tempe, AZ",
                "position": "Cloud Software Engineer Intern",
                "date": "May 2022 - December 2022",
                "bullet_points": ["Implemented a data seed vault to move on-premises data in Richardson, TX to the cloud using AWS S3 and Lambda", "Reduced data migration time by 40% through automated Lambda functions that triggered data transfers from on-premises to AWS S3, allowing for near real-time updates and minimizing manual intervention", "Integrated a data resiliency tracker that improved data recovery speed through best practices like data redundancy, versioning, and integration with AWS CloudWatch for proactive monitoring, ensuring high availability and resilience", "Established stringent bucket policies and encryption protocols, resulting in a 50% reduction in unauthorized access attempts and aligning with AWS’s best security practices for S3 "]
            }
        ],
        "project_experiences": [
            {
                "name": "Computer Science Malware Classification Capstone Project: ProDefense",
                "date": "August 2023 - May 2024",
                "bullet_points": ["Developed a machine learning model for malware detection by reverse-engineering malware binaries and extracting distinguishing features, focusing on operating system details and modules like KERNEL32.dll and specific function names", "Achieved a 99.6% F1 score by optimizing classification models through dataset augmentation and hyperparameter tuning", "Identified key patterns across malware families like SmokeLoader and ZeusBot, enhancing detection and analysis capabilities."]

            },
            {
                "name": "American Statistical Assocation Datafest Competition",
                "date": "April 2024",
                "bullet_points": ["Utilized K-mean clustering techniques, anomaly detection models, and baseline criteria to create a video flagging system that identifies ineffective video content versus learning techniques among students to inform teachers about content revisions", "Won the competition and Best Insights award among 30 teams and 3 universities competing in Arizona for performance of Isolation Forest models and recommending ways to update content in next versions of interactive course"]
            },
            {
                "name": "Washington Nationals MLB Predictive Regression Project",
                "date": "February 2024 - March 2024",
                "bullet_points": ["Initiated a project to predict the number of wins between 1998-2023 by looking at 27 features based on batting performance", "Employed multiple regression analysis with SAS to strategically narrow down analysis to fielding percentages and finish rankings to estimate wins through correlation analysis, regularization techniques, and overcoming multicollinearity issues", "Achieved a highly predictive model with adjusted R-squared value of 0.81 offering future performance optimization insights"]
            }
        ],
        "skills": {
            "programming_languages": "Python (Prof.), SQL (Prof.), R, Java, C/C++, PHP, JavaScript, D3, React Native, Matlab, SAS, React",
            "os_database_cloud_tools": "Github, AWS S3 and Lambda, Linux, Unix, AWS Sagemaker, Snowflake, Apache Airflow, Tableau",
            "skills": "Unit Testing (JUnit), Front-End, AWS (Data/Resiliency Services), Human Computer Interaction, ML, Data Visualization"
        },
        "skills_section": ["Programming Languages: ", "OS/Database/Cloud Tools: ", "Skills: "]
    }
    return render(request, "rishik_cv.html", details)
