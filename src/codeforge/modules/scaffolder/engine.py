"""
محرك القوالب البسيط - الإصدار النظيف
"""

import os
import shutil
from pathlib import Path
from typing import Dict, Any, List


class TemplateEngine:
    """محرك القوالب الأساسي"""
    
    def __init__(self):
        """التهيئة البسيطة"""
        self.templates_dir = Path(__file__).parent.parent.parent / "templates"
        print(f"📂 مجلد القوالب: {self.templates_dir}")
    
    def get_templates(self) -> List[str]:
        """الحصول على القوالب المتاحة"""
        templates = []
        if self.templates_dir.exists():
            for item in self.templates_dir.iterdir():
                if item.is_dir():
                    templates.append(item.name)
        return templates
    
    def create_project(self, template_name: str, project_name: str, data: Dict[str, Any] = None) -> bool:
        """إنشاء مشروع جديد"""
        if data is None:
            data = {}
        
        print(f"🚀 جاري إنشاء '{project_name}'...")
        
        # المسارات
        template_path = self.templates_dir / template_name
        project_path = Path.cwd() / project_name
        
        # التحقق
        if not template_path.exists():
            print(f"❌ القالب '{template_name}' غير موجود")
            return False
        
        if project_path.exists():
            print(f"❌ '{project_name}' موجود مسبقاً")
            return False
        
        try:
            # 1. نسخ القالب
            shutil.copytree(template_path, project_path)
            print(f"📋 تم نسخ القالب")
            
            # 2. معالجة الملفات البسيطة
            self._process_files(project_path, data)
            
            print(f"✅ تم: {project_path}")
            return True
            
        except Exception as e:
            print(f"❌ خطأ: {e}")
            if project_path.exists():
                shutil.rmtree(project_path)
            return False
    
    def _process_files(self, project_path: Path, data: Dict[str, Any]):
        """معالجة الملفات البسيطة"""
        # بيانات افتراضية
        default_data = {
            "project_name": project_path.name,
            "author": "CodeForge"
        }
        data = {**default_data, **data}
        
        # معالجة جميع الملفات .txt و .md و .py
        for ext in ['.txt', '.md', '.py']:
            for file_path in project_path.rglob(f"*{ext}"):
                self._replace_in_file(file_path, data)
    
    def _replace_in_file(self, file_path: Path, data: Dict[str, Any]):
        """استبدال النصوص البسيطة في الملف"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # استبدال بسيط
            for key, value in data.items():
                placeholder = f"{{{key}}}"
                content = content.replace(placeholder, str(value))
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"   ✨ معالجة: {file_path.name}")
            
        except Exception as e:
            print(f"   ⚠️  خطأ في {file_path.name}: {e}")


# اختبار بسيط مباشر
if __name__ == "__main__":
    print("=" * 50)
    print("🧪 اختبار TemplateEngine - الإصدار النظيف")
    print("=" * 50)
    
    engine = TemplateEngine()
    
    templates = engine.get_templates()
    print(f"📁 القوالب: {templates}")
    
    if "python_basic" in templates:
        print("\n🔧 جاري الاختبار...")
        success = engine.create_project(
            template_name="python_basic",
            project_name="my_test_project",
            data={
                "author": "المطور",
                "year": "2024"
            }
        )
        
        if success:
            print("\n🎉 نجح الاختبار!")
            print("يمكنك فتح مجلد: my_test_project")
        else:
            print("\n⚠️  فشل الاختبار")
    else:
        print("\n📝 لا يوجد قالب 'python_basic' بعد")
        print("سأنشئه لك...")
        
        # إنشاء قالب بسيط تلقائياً
        template_dir = engine.templates_dir / "python_basic"
        template_dir.mkdir(exist_ok=True)
        
        # إنشاء ملفات بسيطة
        (template_dir / "README.md").write_text("# {project_name}\n\nبواسطة {author} - {year}")
        (template_dir / "main.py").write_text('print("مرحباً في {project_name}!")')
        
        print("✅ تم إنشاء قالب بسيط")
        print("🔁 جرب تشغيل الملف مرة أخرى")