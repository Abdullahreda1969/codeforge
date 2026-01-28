@'
# دليل استعادة CodeForge

## إذا فقدت المشروع:

### 1. من GitHub:
```bash
git clone https://github.com/Abdullahreda1969/codeforge.git
cd codeforge
python cli_main.py version
2. إذا ضاع GitHub أيضاً:
ابحث عن النسخة المحلية في: C:\Backups\

أو على Google Drive/OneDrive

معلومات المشروع:
الإصدار: 0.1.0

آخر تحديث: $(Get-Date)

المطور: عبدالله رضا
'@ | Out-File -FilePath "RESTORE_GUIDE.md" -Encoding UTF8

git add RESTORE_GUIDE.md
git commit -m "إضافة دليل الاستعادة"
git push

text

### **2. أضف ملف `PROJECT_INFO.json`:**
```json
{
  "project": "CodeForge",
  "version": "0.1.0",
  "author": "Abdullah Reda",
  "github": "https://github.com/Abdullahreda1969/codeforge",
  "last_backup": "$(Get-Date -Format 'yyyy-MM-dd HH:mm')"
}
🚀 الخطوة التالية (اختياري):
1. تحسين ملف README.md على GitHub:
markdown
# CodeForge 🚀

أداة لإنشاء وإدارة المشاريع البرمجية.

## المميزات
- إنشاء مشاريع Python جاهزة
- استبدال تلقائي للمتغيرات
- واجهة CLI سهلة

## الاستخدام
```bash
python cli_main.py create python_basic myapp --author "اسمك"
التثبيت
bash
git clone https://github.com/Abdullahreda1969/codeforge.git
cd codeforge
pip install -r requirements.txt
text

### **2. إضافة License (اختياري):**
```powershell
# ملف MIT License بسيط
@'
MIT License

Copyright (c) $(Get-Date -Format 'yyyy') Abdullah Reda

Permission is hereby granted...
'@ | Out-File -FilePath "LICENSE" -Encoding UTF8
