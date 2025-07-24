🔐 Cybersecurity Internship – FutureInterns (1 Month)
---------------------------------------------------------------------------------------------

This repository contains all the tasks I completed during my **1-month virtual internship** in the **Cyber Security track** offered by **Future Interns**. Each task was hands-on and focused on real-world cybersecurity practices including ethical hacking, log analysis, and secure development.

---

 **Task 1: Web Application Security Testing:**
 **Objective:** Identify and exploit common vulnerabilities in a sample web application.

**Vulnerabilities Exploited:**
**SQL Injection (SQLi):**  
  Used classic payloads like `' OR '1'='1` to bypass login authentication and gain unauthorized access.
 **Cross-Site Scripting (XSS):**  
  Injected JavaScript payloads such as `<script>alert('XSS')</script>` into input fields to test client-side execution.
 **Authentication Flaws:**  
  Exploited weak login/session logic to access protected user areas.

**Tools Used:**  
Burp Suite, OWASP Juice Shop, SQLMap, browser DevTools

**Deliverable:**  
Detailed security report with screenshots, findings, and mitigation strategies.

---

Task 2: Security Log Analysis using Splunk

**Objective:** Analyze real system logs using Splunk to detect suspicious activity.

**What I Did:**
- Collected system logs from my **Kali Linux** environment.
- Uploaded and indexed the logs in **Splunk Free Trial**.
- Filtered logs to identify relevant patterns and activities.
- Visualized the data using **line charts** and **pie charts** for better insight.

**Skills Gained:**  
SIEM basics, log analysis, incident detection, data visualization

**Deliverable:**  
Incident response report with analysis, insights, and charts.

---

Task 3: Secure File Sharing System (AES Encryption)

**Objective:** Build a secure portal to upload and download files with encryption.

**Features Implemented:**
- Users can upload files through a web interface.
- Uploaded files are encrypted using AES and stored securely.
- Files can be downloaded and are decrypted on the fly before being sent to the user.

**Tools & Technologies:**
Python, Flask, PyCryptodome, HTML/CSS

**Deliverable:**  
Fully working Flask app with AES encryption, a GitHub repo, and a security overview document.

---

**Summary**

During this internship, I gained practical experience in:
Ethical hacking and vulnerability exploitation
SIEM and security monitoring using Splunk
Secure coding and encryption techniques with Python

These tasks gave me real-world exposure to how cybersecurity professionals test, analyze, and secure applications and systems.

